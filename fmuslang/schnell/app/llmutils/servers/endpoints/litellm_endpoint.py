import sys, os, platform, time, copy, re, asyncio, inspect
import threading, ast
import shutil, random, traceback, requests
from datetime import datetime, timedelta, timezone
from typing import Optional, List, Callable, Dict
from typing import Literal
import secrets, subprocess
import hashlib, uuid
import warnings
import importlib
import inspect
from textwrap import dedent
import json
import backoff

import fastapi
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import (
    StreamingResponse,
    FileResponse,
    ORJSONResponse,
    JSONResponse,
)
from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
    Depends,
    Header,
    Response,
    Form,
    UploadFile,
    File,
)
from fastapi.security.api_key import APIKeyHeader

import schnell.app.llmutils.langchainutils.proxy.litellm as litellm
from schnell.app.llmutils.langchainutils.proxy.litellm.proxy.utils import (
    PrismaClient,
    DBClient,
    get_instance_fn,
    ProxyLogging,
    _cache_user_row,
    send_email,
    get_logging_payload,
    reset_budget,
    hash_token,
    html_form,
    _read_request_body,
    _is_valid_team_configs,
    _is_user_proxy_admin,
    _is_projected_spend_over_limit,
    _get_projected_spend_over_limit,
    update_spend,
    encrypt_value,
    decrypt_value,
)
from schnell.app.llmutils.langchainutils.proxy.litellm._logging import verbose_router_logger, verbose_proxy_logger

from schnell.app.llmutils.langchainutils.proxy.litellm.proxy.auth.handle_jwt import JWTHandler
from schnell.app.llmutils.langchainutils.proxy.litellm.proxy.auth.auth_checks import (
    common_checks,
    get_end_user_object,
    get_org_object,
    get_team_object,
    get_user_object,
    allowed_routes_check,
    get_actual_routes,
)
from schnell.app.llmutils.langchainutils.proxy.litellm.proxy._types import (
    # LiteLLMBase,
    LiteLLM_UpperboundKeyGenerateParams,
    LiteLLMRoutes,
    LiteLLM_JWTAuth,
    LiteLLMPromptInjectionParams,
    ProxyChatCompletionRequest,
    ModelInfoDelete,
    ModelInfo,
    BlockUsers,
    ModelParams,
    GenerateRequestBase,
    GenerateKeyRequest,
    GenerateKeyResponse,
    UpdateKeyRequest,
    KeyRequest,
    LiteLLM_ModelTable,
    NewUserRequest,
    NewUserResponse,
    UpdateUserRequest,
    NewEndUserRequest,
    Member,
    TeamBase,
    NewTeamRequest,
    TeamMemberAddRequest,
    TeamMemberDeleteRequest,
    UpdateTeamRequest,
    DeleteTeamRequest,
    BlockTeamRequest,
    LiteLLM_TeamTable,
    TeamRequest,
    LiteLLM_BudgetTable,
    NewOrganizationRequest,
    LiteLLM_OrganizationTable,
    NewOrganizationResponse,
    OrganizationRequest,
    BudgetRequest,
    KeyManagementSystem,
    KeyManagementSettings,
    TeamDefaultSettings,
    DynamoDBArgs,
    ConfigGeneralSettings,
    ConfigYAML,
    LiteLLM_VerificationToken,
    LiteLLM_VerificationTokenView,
    UserAPIKeyAuth,
    LiteLLM_Config,
    LiteLLM_UserTable,
    LiteLLM_EndUserTable,
    LiteLLM_SpendLogs,
    LiteLLM_ErrorLogs,
    LiteLLM_SpendLogs_ResponseObject,
)
from schnell.app.llmutils.langchainutils.proxy.litellm.caching import DualCache, RedisCache
from schnell.app.llmutils.langchainutils.proxy.litellm._version import version
from schnell.app.llmutils.langchainutils.proxy.litellm.proxy.hooks.prompt_injection_detection import _OPTIONAL_PromptInjectionDetection
from schnell.app.printutils import indah4
from schnell.app.llmutils.langchainutils.proxy.litellm.llms.custom_httpx.httpx_handler import HTTPHandler
from schnell.app.llmutils.langchainutils.proxy.litellm.proxy.proxy_server import (
    _get_bearer_token,
    _has_user_setup_sso,
    _get_pydantic_json_dict,
    ProxyException,
    UserAPIKeyCacheTTLEnum,
    SpecialModelNames,
    CommonProxyErrors,
    ProxyConfig,
    select_data_generator,
    on_backoff,
    parse_cache_control,
    save_worker_config,
)


router = APIRouter()
origins = ["*"]


api_key_header = APIKeyHeader(
    name="Authorization",
    auto_error=False,
    description="Bearer token"
)


from schnell.app.llmutils.langchainutils.llm_config import get_active_model
# user_model = "gemini/gemini-pro" # None
user_model = "gemini/gemini-1.5-flash" # None
# user_model = get_active_model()  # gemini-1.5-flash-latest => harusnya gemini/gemini-1.5-flash utk gaya litellm
# schnell.app.llmutils.langchainutils.proxy.litellm.exceptions.BadRequestError: LLM Provider NOT provided. Pass in the LLM provider you are trying to call.
# You passed model=gemini-1.5-flash-latest
#  Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers
# An error occurred: LLM Provider NOT provided. Pass in the LLM provider you are trying to call. You passed model=gemini-1.5-flash-latest
#  Pass model as E.g. For 'Huggingface' inference endpoints pass in `completion(model='huggingface/starcoder',..)` Learn more: https://docs.litellm.ai/docs/providers

#   Debug this by setting `--debug`, e.g. `litellm --model gpt-3.5-turbo --debug`
# ERROR:backoff:Giving up chat_completion(...) after 1 tries (schnell.app.llmutils.langchainutils.proxy.litellm.proxy.proxy_server.ProxyException)
# INFO:     ::1:54128 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error

user_api_base = None
user_debug = False
user_max_tokens = None
user_request_timeout = 600 # None
user_temperature = None
user_telemetry = True
user_config = None
user_headers = None
user_config_file_path = f"config_{int(time.time())}.yaml"
local_logging = True  # writes logs to a local api_log.json file for debugging
experimental = False
#### GLOBAL VARIABLES ####
llm_router: Optional[litellm.Router] = None
llm_model_list: Optional[list] = None
general_settings: dict = {}
log_file = "api_log.json"
worker_config = None
master_key = None
otel_logging = False
prisma_client: Optional[PrismaClient] = None
custom_db_client: Optional[DBClient] = None
user_api_key_cache = DualCache()
redis_usage_cache: Optional[RedisCache] = (
    None  # redis cache used for tracking spend, tpm/rpm limits
)
user_custom_auth = None
user_custom_key_generate = None
use_background_health_checks = None
use_queue = False
health_check_interval = None
health_check_results = {}
queue: List = []
litellm_proxy_budget_name = "litellm-proxy-budget"
litellm_proxy_admin_name = "default_user_id"
ui_access_mode: Literal["admin", "all"] = "all"
proxy_budget_rescheduler_min_time = 597
proxy_budget_rescheduler_max_time = 605
proxy_batch_write_at = 10  # in seconds
litellm_master_key_hash = None
disable_spend_logs = False
jwt_handler = JWTHandler()
prompt_injection_detection_obj: Optional[_OPTIONAL_PromptInjectionDetection] = None
store_model_in_db: bool = False
### INITIALIZE GLOBAL LOGGING OBJECT ###
proxy_logging_obj = ProxyLogging(user_api_key_cache=user_api_key_cache)
### REDIS QUEUE ###
async_result = None
celery_app_conn = None
celery_fn = None  # Redis Queue for handling requests
### DB WRITER ###
db_writer_client: Optional[HTTPHandler] = None
### logger ###
proxy_config = ProxyConfig()


async def user_api_key_auth(
    request: Request, api_key: str = fastapi.Security(api_key_header)
) -> UserAPIKeyAuth:

    global master_key, prisma_client, llm_model_list, user_custom_auth, custom_db_client, general_settings

    try:
        if isinstance(api_key, str):
            passed_in_key = api_key
            api_key = _get_bearer_token(api_key=api_key)

        ### USER-DEFINED AUTH FUNCTION ###
        if user_custom_auth is not None:
            response = await user_custom_auth(request=request, api_key=api_key)
            return UserAPIKeyAuth.model_validate(response)

        ### LITELLM-DEFINED AUTH FUNCTION ###
        #### IF JWT ####
        # LiteLLM supports using JWTs.
        # Enable this in proxy config, by setting
        # ```
        # general_settings:
        #     enable_jwt_auth: true
        # ```

        route: str = request.url.path

        if route in LiteLLMRoutes.public_routes.value:
            # check if public endpoint
            return UserAPIKeyAuth()

        if general_settings.get("enable_jwt_auth", False) == True:
            is_jwt = jwt_handler.is_jwt(token=api_key)
            verbose_proxy_logger.debug("is_jwt: %s", is_jwt)
            if is_jwt:
                # check if valid token
                valid_token = await jwt_handler.auth_jwt(token=api_key)
                # get scopes
                scopes = jwt_handler.get_scopes(token=valid_token)

                # check if admin
                is_admin = jwt_handler.is_admin(scopes=scopes)
                # if admin return
                if is_admin:
                    # check allowed admin routes
                    is_allowed = allowed_routes_check(
                        user_role="proxy_admin",
                        user_route=route,
                        litellm_proxy_roles=jwt_handler.litellm_jwtauth,
                    )
                    if is_allowed:
                        return UserAPIKeyAuth()
                    else:
                        allowed_routes = (
                            jwt_handler.litellm_jwtauth.admin_allowed_routes
                        )
                        actual_routes = get_actual_routes(allowed_routes=allowed_routes)
                        raise Exception(
                            f"Admin not allowed to access this route. Route={route}, Allowed Routes={actual_routes}"
                        )
                # get team id
                team_id = jwt_handler.get_team_id(token=valid_token, default_value=None)

                if team_id is None:
                    raise Exception(
                        f"No team id passed in. Field checked in jwt token - '{jwt_handler.litellm_jwtauth.team_id_jwt_field}'"
                    )
                # check allowed team routes
                is_allowed = allowed_routes_check(
                    user_role="team",
                    user_route=route,
                    litellm_proxy_roles=jwt_handler.litellm_jwtauth,
                )
                if is_allowed == False:
                    allowed_routes = jwt_handler.litellm_jwtauth.team_allowed_routes
                    actual_routes = get_actual_routes(allowed_routes=allowed_routes)
                    raise Exception(
                        f"Team not allowed to access this route. Route={route}, Allowed Routes={actual_routes}"
                    )

                # check if team in db
                team_object = await get_team_object(
                    team_id=team_id,
                    prisma_client=prisma_client,
                    user_api_key_cache=user_api_key_cache,
                )

                # [OPTIONAL] track spend for an org id - `LiteLLM_OrganizationTable`
                org_id = jwt_handler.get_org_id(token=valid_token, default_value=None)
                if org_id is not None:
                    _ = await get_org_object(
                        org_id=org_id,
                        prisma_client=prisma_client,
                        user_api_key_cache=user_api_key_cache,
                    )
                # [OPTIONAL] track spend against an internal employee - `LiteLLM_UserTable`
                user_object = None
                user_id = jwt_handler.get_user_id(token=valid_token, default_value=None)
                if user_id is not None:
                    # get the user object
                    user_object = await get_user_object(
                        user_id=user_id,
                        prisma_client=prisma_client,
                        user_api_key_cache=user_api_key_cache,
                    )
                    # save the user object to cache
                    await user_api_key_cache.async_set_cache(
                        key=user_id, value=user_object
                    )
                # [OPTIONAL] track spend against an external user - `LiteLLM_EndUserTable`
                end_user_object = None
                end_user_id = jwt_handler.get_end_user_id(
                    token=valid_token, default_value=None
                )
                if end_user_id is not None:
                    # get the end-user object
                    end_user_object = await get_end_user_object(
                        end_user_id=end_user_id,
                        prisma_client=prisma_client,
                        user_api_key_cache=user_api_key_cache,
                    )

                global_proxy_spend = None
                if litellm.max_budget > 0:  # user set proxy max budget
                    # check cache
                    global_proxy_spend = await user_api_key_cache.async_get_cache(
                        key="{}:spend".format(litellm_proxy_admin_name)
                    )
                    if global_proxy_spend is None and prisma_client is not None:
                        # get from db
                        sql_query = """SELECT SUM(spend) as total_spend FROM "MonthlyGlobalSpend";"""

                        response = await prisma_client.db.query_raw(query=sql_query)

                        global_proxy_spend = response[0]["total_spend"]

                        await user_api_key_cache.async_set_cache(
                            key="{}:spend".format(litellm_proxy_admin_name),
                            value=global_proxy_spend,
                            ttl=UserAPIKeyCacheTTLEnum.global_proxy_spend.value,
                        )
                    if global_proxy_spend is not None:
                        user_info = {
                            "user_id": litellm_proxy_admin_name,
                            "max_budget": litellm.max_budget,
                            "spend": global_proxy_spend,
                            "user_email": "",
                        }
                        asyncio.create_task(
                            proxy_logging_obj.budget_alerts(
                                user_max_budget=litellm.max_budget,
                                user_current_spend=global_proxy_spend,
                                type="user_and_proxy_budget",
                                user_info=user_info,
                            )
                        )

                # get the request body
                request_data = await _read_request_body(request=request)

                # run through common checks
                _ = common_checks(
                    request_body=request_data,
                    team_object=team_object,
                    user_object=user_object,
                    end_user_object=end_user_object,
                    general_settings=general_settings,
                    global_proxy_spend=global_proxy_spend,
                    route=route,
                )
                # save team object in cache
                await user_api_key_cache.async_set_cache(
                    key=team_object.team_id, value=team_object
                )

                # return UserAPIKeyAuth object
                return UserAPIKeyAuth(
                    api_key=None,
                    team_id=team_object.team_id,
                    team_tpm_limit=team_object.tpm_limit,
                    team_rpm_limit=team_object.rpm_limit,
                    team_models=team_object.models,
                    user_role="app_owner",
                    user_id=user_id,
                    org_id=org_id,
                )
        #### ELSE ####
        if master_key is None:
            if isinstance(api_key, str):
                return UserAPIKeyAuth(api_key=api_key)
            else:
                return UserAPIKeyAuth()
        elif api_key is None:  # only require api key if master key is set
            raise Exception("No api key passed in.")
        elif api_key == "":
            # missing 'Bearer ' prefix
            raise Exception(
                f"Malformed API Key passed in. Ensure Key has `Bearer ` prefix. Passed in: {passed_in_key}"
            )

        if route == "/user/auth":
            if general_settings.get("allow_user_auth", False) == True:
                return UserAPIKeyAuth()
            else:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="'allow_user_auth' not set or set to False",
                )

        ### CHECK IF ADMIN ###
        # note: never string compare api keys, this is vulenerable to a time attack. Use secrets.compare_digest instead
        ### CHECK IF ADMIN ###
        # note: never string compare api keys, this is vulenerable to a time attack. Use secrets.compare_digest instead
        ## Check CACHE
        valid_token = user_api_key_cache.get_cache(key=hash_token(api_key))
        if (
            valid_token is not None
            and isinstance(valid_token, UserAPIKeyAuth)
            and valid_token.user_role == "proxy_admin"
        ):
            return valid_token

        try:
            is_master_key_valid = secrets.compare_digest(api_key, master_key)
        except Exception as e:
            is_master_key_valid = False

        if is_master_key_valid:
            _user_api_key_obj = UserAPIKeyAuth(
                api_key=master_key,
                user_role="proxy_admin",
                user_id=litellm_proxy_admin_name,
            )
            await user_api_key_cache.async_set_cache(
                key=hash_token(master_key), value=_user_api_key_obj
            )

            return _user_api_key_obj
        if isinstance(
            api_key, str
        ):  # if generated token, make sure it starts with sk-.
            assert api_key.startswith("sk-")  # prevent token hashes from being used

        if (
            prisma_client is None and custom_db_client is None
        ):  # if both master key + user key submitted, and user key != master key, and no db connected, raise an error
            raise Exception("No connected db.")

        ## check for cache hit (In-Memory Cache)
        original_api_key = api_key  # (Patch: For DynamoDB Backwards Compatibility)
        if api_key.startswith("sk-"):
            api_key = hash_token(token=api_key)
        valid_token = user_api_key_cache.get_cache(key=api_key)
        if valid_token is None:
            ## check db
            verbose_proxy_logger.debug("api key: %s", api_key)
            if prisma_client is not None:
                valid_token = await prisma_client.get_data(
                    token=api_key, table_name="combined_view"
                )
            elif custom_db_client is not None:
                try:
                    valid_token = await custom_db_client.get_data(
                        key=api_key, table_name="key"
                    )
                except:
                    # (Patch: For DynamoDB Backwards Compatibility)
                    valid_token = await custom_db_client.get_data(
                        key=original_api_key, table_name="key"
                    )
            verbose_proxy_logger.debug("Token from db: %s", valid_token)
        elif valid_token is not None:
            verbose_proxy_logger.debug("API Key Cache Hit!")
        user_id_information = None
        if valid_token:
            # Got Valid Token from Cache, DB
            # Run checks for
            # 1. If token can call model
            # 2. If user_id for this token is in budget
            # 3. If 'user' passed to /chat/completions, /embeddings endpoint is in budget
            # 4. If token is expired
            # 5. If token spend is under Budget for the token
            # 6. If token spend per model is under budget per model
            # 7. If token spend is under team budget
            # 8. If team spend is under team budget

            request_data = await _read_request_body(
                request=request
            )  # request data, used across all checks. Making this easily available

            # Check 1. If token can call model
            _model_alias_map = {}
            if (
                hasattr(valid_token, "team_model_aliases")
                and valid_token.team_model_aliases is not None
            ):
                _model_alias_map = {
                    **valid_token.aliases,
                    **valid_token.team_model_aliases,
                }
            else:
                _model_alias_map = {**valid_token.aliases}
            litellm.model_alias_map = _model_alias_map
            config = valid_token.config
            if config != {}:
                model_list = config.get("model_list", [])
                llm_model_list = model_list
                verbose_proxy_logger.debug(
                    f"\n new llm router model list {llm_model_list}"
                )
            if (
                len(valid_token.models) == 0
            ):  # assume an empty model list means all models are allowed to be called
                pass
            elif (
                isinstance(valid_token.models, list)
                and "all-team-models" in valid_token.models
            ):
                # Do not do any validation at this step
                # the validation will occur when checking the team has access to this model
                pass
            else:
                try:
                    data = await request.json()
                except json.JSONDecodeError:
                    data = {}  # Provide a default value, such as an empty dictionary
                model = data.get("model", None)
                if model in litellm.model_alias_map:
                    model = litellm.model_alias_map[model]

                ## check if model in allowed model names
                verbose_proxy_logger.debug(
                    f"LLM Model List pre access group check: {llm_model_list}"
                )
                from collections import defaultdict

                access_groups = defaultdict(list)
                if llm_model_list is not None:
                    for m in llm_model_list:
                        for group in m.get("model_info", {}).get("access_groups", []):
                            model_name = m["model_name"]
                            access_groups[group].append(model_name)

                models_in_current_access_groups = []
                if (
                    len(access_groups) > 0
                ):  # check if token contains any model access groups
                    for idx, m in enumerate(
                        valid_token.models
                    ):  # loop token models, if any of them are an access group add the access group
                        if m in access_groups:
                            # if it is an access group we need to remove it from valid_token.models
                            models_in_group = access_groups[m]
                            models_in_current_access_groups.extend(models_in_group)

                # Filter out models that are access_groups
                filtered_models = [
                    m for m in valid_token.models if m not in access_groups
                ]

                filtered_models += models_in_current_access_groups
                verbose_proxy_logger.debug(
                    f"model: {model}; allowed_models: {filtered_models}"
                )
                if (
                    model is not None
                    and model not in filtered_models
                    and "*" not in filtered_models
                ):
                    raise ValueError(
                        f"API Key not allowed to access model. This token can only access models={valid_token.models}. Tried to access {model}"
                    )
                valid_token.models = filtered_models
                verbose_proxy_logger.debug(
                    f"filtered allowed_models: {filtered_models}; valid_token.models: {valid_token.models}"
                )

            # Check 2. If user_id for this token is in budget
            if valid_token.user_id is not None:
                user_id_list = [valid_token.user_id]
                for id in user_id_list:
                    value = user_api_key_cache.get_cache(key=id)
                    if value is not None:
                        if user_id_information is None:
                            user_id_information = []
                        user_id_information.append(value)
                if user_id_information is None or (
                    isinstance(user_id_information, list)
                    and len(user_id_information) < 1
                ):
                    if prisma_client is not None:
                        user_id_information = await prisma_client.get_data(
                            user_id_list=[
                                valid_token.user_id,
                            ],
                            table_name="user",
                            query_type="find_all",
                        )
                        for _id in user_id_information:
                            await user_api_key_cache.async_set_cache(
                                key=_id["user_id"],
                                value=_id,
                                ttl=UserAPIKeyCacheTTLEnum.user_information_cache.value,
                            )
                    if custom_db_client is not None:
                        user_id_information = await custom_db_client.get_data(
                            key=valid_token.user_id, table_name="user"
                        )

                verbose_proxy_logger.debug(
                    f"user_id_information: {user_id_information}"
                )

                if user_id_information is not None:
                    if isinstance(user_id_information, list):
                        ## Check if user in budget
                        for _user in user_id_information:
                            if _user is None:
                                continue
                            assert isinstance(_user, dict)
                            # check if user is admin #

                            # Token exists, not expired now check if its in budget for the user
                            user_max_budget = _user.get("max_budget", None)
                            user_current_spend = _user.get("spend", None)

                            verbose_proxy_logger.debug(
                                f"user_id: {_user.get('user_id', None)}; user_max_budget: {user_max_budget}; user_current_spend: {user_current_spend}"
                            )

                            if (
                                user_max_budget is not None
                                and user_current_spend is not None
                            ):
                                asyncio.create_task(
                                    proxy_logging_obj.budget_alerts(
                                        user_max_budget=user_max_budget,
                                        user_current_spend=user_current_spend,
                                        type="user_and_proxy_budget",
                                        user_info=_user,
                                    )
                                )

                                _user_id = _user.get("user_id", None)
                                if user_current_spend > user_max_budget:
                                    raise Exception(
                                        f"ExceededBudget: User {_user_id} has exceeded their budget. Current spend: {user_current_spend}; Max Budget: {user_max_budget}"
                                    )
                    else:
                        # Token exists, not expired now check if its in budget for the user
                        user_max_budget = getattr(
                            user_id_information, "max_budget", None
                        )
                        user_current_spend = getattr(user_id_information, "spend", None)

                        if (
                            user_max_budget is not None
                            and user_current_spend is not None
                        ):
                            asyncio.create_task(
                                proxy_logging_obj.budget_alerts(
                                    user_max_budget=user_max_budget,
                                    user_current_spend=user_current_spend,
                                    type="user_budget",
                                    user_info=user_id_information,
                                )
                            )

                            if user_current_spend > user_max_budget:
                                raise Exception(
                                    f"ExceededBudget: User {valid_token.user_id} has exceeded their budget. Current spend: {user_current_spend}; Max Budget: {user_max_budget}"
                                )

            # Check 3. If token is expired
            if valid_token.expires is not None:
                current_time = datetime.now(timezone.utc)
                expiry_time = datetime.fromisoformat(valid_token.expires)
                if (
                    expiry_time.tzinfo is None
                    or expiry_time.tzinfo.utcoffset(expiry_time) is None
                ):
                    expiry_time = expiry_time.replace(tzinfo=timezone.utc)
                verbose_proxy_logger.debug(
                    f"Checking if token expired, expiry time {expiry_time} and current time {current_time}"
                )
                if expiry_time < current_time:
                    # Token exists but is expired.
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail=f"Authentication Error - Expired Key. Key Expiry time {expiry_time} and current time {current_time}",
                    )

            # Check 4. Token Spend is under budget
            if valid_token.spend is not None and valid_token.max_budget is not None:
                asyncio.create_task(
                    proxy_logging_obj.budget_alerts(
                        user_max_budget=valid_token.max_budget,
                        user_current_spend=valid_token.spend,
                        type="token_budget",
                        user_info=valid_token,
                    )
                )

                if valid_token.spend >= valid_token.max_budget:
                    raise Exception(
                        f"ExceededTokenBudget: Current spend for token: {valid_token.spend}; Max Budget for Token: {valid_token.max_budget}"
                    )

            # Check 5. Token Model Spend is under Model budget
            max_budget_per_model = valid_token.model_max_budget

            if (
                max_budget_per_model is not None
                and isinstance(max_budget_per_model, dict)
                and len(max_budget_per_model) > 0
            ):
                current_model = request_data.get("model")
                ## GET THE SPEND FOR THIS MODEL
                twenty_eight_days_ago = datetime.now() - timedelta(days=28)
                model_spend = await prisma_client.db.litellm_spendlogs.group_by(
                    by=["model"],
                    sum={"spend": True},
                    where={
                        "AND": [
                            {"api_key": valid_token.token},
                            {"startTime": {"gt": twenty_eight_days_ago}},
                            {"model": current_model},
                        ]
                    },
                )
                if (
                    len(model_spend) > 0
                    and max_budget_per_model.get(current_model, None) is not None
                ):
                    if (
                        model_spend[0]["model"] == current_model
                        and model_spend[0]["_sum"]["spend"]
                        >= max_budget_per_model[current_model]
                    ):
                        current_model_spend = model_spend[0]["_sum"]["spend"]
                        current_model_budget = max_budget_per_model[current_model]
                        raise Exception(
                            f"ExceededModelBudget: Current spend for model: {current_model_spend}; Max Budget for Model: {current_model_budget}"
                        )
            # Check 6. Token spend is under Team budget
            if (
                valid_token.spend is not None
                and hasattr(valid_token, "team_max_budget")
                and valid_token.team_max_budget is not None
            ):
                asyncio.create_task(
                    proxy_logging_obj.budget_alerts(
                        user_max_budget=valid_token.team_max_budget,
                        user_current_spend=valid_token.spend,
                        type="token_budget",
                        user_info=valid_token,
                    )
                )

                if valid_token.spend >= valid_token.team_max_budget:
                    raise Exception(
                        f"ExceededTokenBudget: Current spend for token: {valid_token.spend}; Max Budget for Team: {valid_token.team_max_budget}"
                    )

            # Check 7. Team spend is under Team budget
            if (
                hasattr(valid_token, "team_spend")
                and valid_token.team_spend is not None
                and hasattr(valid_token, "team_max_budget")
                and valid_token.team_max_budget is not None
            ):
                asyncio.create_task(
                    proxy_logging_obj.budget_alerts(
                        user_max_budget=valid_token.team_max_budget,
                        user_current_spend=valid_token.team_spend,
                        type="token_budget",
                        user_info=valid_token,
                    )
                )

                if valid_token.team_spend >= valid_token.team_max_budget:
                    raise Exception(
                        f"ExceededTokenBudget: Current Team Spend: {valid_token.team_spend}; Max Budget for Team: {valid_token.team_max_budget}"
                    )

            # Check 8: Additional Common Checks across jwt + key auth
            _team_obj = LiteLLM_TeamTable(
                team_id=valid_token.team_id,
                max_budget=valid_token.team_max_budget,
                spend=valid_token.team_spend,
                tpm_limit=valid_token.team_tpm_limit,
                rpm_limit=valid_token.team_rpm_limit,
                blocked=valid_token.team_blocked,
                models=valid_token.team_models,
            )

            user_api_key_cache.set_cache(
                key=valid_token.team_id, value=_team_obj
            )  # save team table in cache - used for tpm/rpm limiting - tpm_rpm_limiter.py

            _end_user_object = None
            if "user" in request_data:
                _end_user_object = await get_end_user_object(
                    end_user_id=request_data["user"],
                    prisma_client=prisma_client,
                    user_api_key_cache=user_api_key_cache,
                )

            global_proxy_spend = None
            if (
                litellm.max_budget > 0 and prisma_client is not None
            ):  # user set proxy max budget
                # check cache
                global_proxy_spend = await user_api_key_cache.async_get_cache(
                    key="{}:spend".format(litellm_proxy_admin_name)
                )
                if global_proxy_spend is None:
                    # get from db
                    sql_query = """SELECT SUM(spend) as total_spend FROM "MonthlyGlobalSpend";"""

                    response = await prisma_client.db.query_raw(query=sql_query)

                    global_proxy_spend = response[0]["total_spend"]
                    await user_api_key_cache.async_set_cache(
                        key="{}:spend".format(litellm_proxy_admin_name),
                        value=global_proxy_spend,
                        ttl=UserAPIKeyCacheTTLEnum.global_proxy_spend.value,
                    )

                if global_proxy_spend is not None:
                    user_info = {
                        "user_id": litellm_proxy_admin_name,
                        "max_budget": litellm.max_budget,
                        "spend": global_proxy_spend,
                        "user_email": "",
                    }
                    asyncio.create_task(
                        proxy_logging_obj.budget_alerts(
                            user_max_budget=litellm.max_budget,
                            user_current_spend=global_proxy_spend,
                            type="user_and_proxy_budget",
                            user_info=user_info,
                        )
                    )
            _ = common_checks(
                request_body=request_data,
                team_object=_team_obj,
                user_object=None,
                end_user_object=_end_user_object,
                general_settings=general_settings,
                global_proxy_spend=global_proxy_spend,
                route=route,
            )
            # Token passed all checks
            api_key = valid_token.token

            # Add hashed token to cache
            await user_api_key_cache.async_set_cache(
                key=api_key,
                value=valid_token,
                ttl=UserAPIKeyCacheTTLEnum.key_information_cache.value,
            )
            valid_token_dict = _get_pydantic_json_dict(valid_token)
            valid_token_dict.pop("token", None)

            if _end_user_object is not None:
                valid_token_dict["allowed_model_region"] = (
                    _end_user_object.allowed_model_region
                )

            """
            asyncio create task to update the user api key cache with the user db table as well

            This makes the user row data accessible to pre-api call hooks.
            """
            if custom_db_client is not None:
                asyncio.create_task(
                    _cache_user_row(
                        user_id=valid_token.user_id,
                        cache=user_api_key_cache,
                        db=custom_db_client,
                    )
                )

            if not _is_user_proxy_admin(user_id_information):  # if non-admin
                if route in LiteLLMRoutes.openai_routes.value:
                    pass
                elif (
                    route in LiteLLMRoutes.info_routes.value
                ):  # check if user allowed to call an info route
                    if route == "/key/info":
                        # check if user can access this route
                        query_params = request.query_params
                        key = query_params.get("key")
                        if key is not None and hash_token(token=key) != api_key:
                            raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="user not allowed to access this key's info",
                            )
                    elif route == "/user/info":
                        # check if user can access this route
                        query_params = request.query_params
                        user_id = query_params.get("user_id")
                        verbose_proxy_logger.debug(
                            f"user_id: {user_id} & valid_token.user_id: {valid_token.user_id}"
                        )
                        if user_id != valid_token.user_id:
                            raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="key not allowed to access this user's info",
                            )
                    elif route == "/model/info":
                        # /model/info just shows models user has access to
                        pass
                    elif route == "/team/info":
                        # check if key can access this team's info
                        query_params = request.query_params
                        team_id = query_params.get("team_id")
                        if team_id != valid_token.team_id:
                            raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="key not allowed to access this team's info",
                            )
                elif (
                    _has_user_setup_sso()
                    and route in LiteLLMRoutes.sso_only_routes.value
                ):
                    pass
                else:
                    user_role = "unknown"
                    user_id = "unknown"
                    if user_id_information is not None and isinstance(
                        user_id_information, list
                    ):
                        _user = user_id_information[0]
                        user_role = _user.get("user_role", {}).get(
                            "user_role", "unknown"
                        )
                        user_id = _user.get("user_id", "unknown")
                    raise Exception(
                        f"Only proxy admin can be used to generate, delete, update info for new keys/users/teams. Route={route}. Your role={user_role}. Your user_id={user_id}"
                    )

        # check if token is from litellm-ui, litellm ui makes keys to allow users to login with sso. These keys can only be used for LiteLLM UI functions
        # sso/login, ui/login, /key functions and /user functions
        # this will never be allowed to call /chat/completions
        token_team = getattr(valid_token, "team_id", None)

        if token_team is not None and token_team == "litellm-dashboard":
            # this token is only used for managing the ui
            allowed_routes = [
                "/sso",
                "/login",
                "/key/generate",
                "/key/update",
                "/key/info",
                "/config",
                "/spend",
                "/user",
                "/model/info",
                "/v2/model/info",
                "/v2/key/info",
                "/models",
                "/v1/models",
                "/global/spend",
                "/global/spend/logs",
                "/global/spend/keys",
                "/global/spend/models",
                "/global/predict/spend/logs",
                "/health/services",
            ]
            # check if the current route startswith any of the allowed routes
            if (
                route is not None
                and isinstance(route, str)
                and any(
                    route.startswith(allowed_route) for allowed_route in allowed_routes
                )
            ):
                # Do something if the current route starts with any of the allowed routes
                pass
            else:
                if user_id_information is not None and _is_user_proxy_admin(
                    user_id_information
                ):
                    return UserAPIKeyAuth(
                        api_key=api_key, user_role="proxy_admin", **valid_token_dict
                    )
                elif (
                    _has_user_setup_sso()
                    and route in LiteLLMRoutes.sso_only_routes.value
                ):
                    return UserAPIKeyAuth(
                        api_key=api_key, user_role="app_owner", **valid_token_dict
                    )
                else:
                    raise Exception(
                        f"This key is made for LiteLLM UI, Tried to access route: {route}. Not allowed"
                    )
        if valid_token is None:
            # No token was found when looking up in the DB
            raise Exception("Invalid token passed")
        if valid_token_dict is not None:
            return UserAPIKeyAuth(api_key=api_key, **valid_token_dict)
        else:
            raise Exception()
    except Exception as e:
        traceback.print_exc()
        if isinstance(e, HTTPException):
            raise ProxyException(
                message=getattr(e, "detail", f"Authentication Error({str(e)})"),
                type="auth_error",
                param=getattr(e, "param", "None"),
                code=getattr(e, "status_code", status.HTTP_401_UNAUTHORIZED),
            )
        elif isinstance(e, ProxyException):
            raise e
        raise ProxyException(
            message="Authentication Error, " + str(e),
            type="auth_error",
            param=getattr(e, "param", "None"),
            code=status.HTTP_401_UNAUTHORIZED,
        )


@router.post("/v1/chat/completions",
    dependencies=[Depends(user_api_key_auth)],
    tags=["chat/completions"],
)
@router.post("/chat/completions",
    dependencies=[Depends(user_api_key_auth)],
    tags=["chat/completions"],
)
@router.post("/engines/{model:path}/chat/completions",
    dependencies=[Depends(user_api_key_auth)],
    tags=["chat/completions"],
)
@router.post("/openai/deployments/{model:path}/chat/completions",
    dependencies=[Depends(user_api_key_auth)],
    tags=["chat/completions"],
)  # azure compatible endpoint
@backoff.on_exception(
    backoff.expo,
    Exception,  # base exception to catch for the backoff
    max_tries=litellm.num_retries or 3,  # maximum number of retries
    max_time=litellm.request_timeout or 60,  # maximum total time to retry for
    on_backoff=on_backoff,  # specifying the function to call on backoff
    giveup=lambda e: not (
        isinstance(e, ProxyException)
        and getattr(e, "message", None) is not None
        and isinstance(e.message, str)
        and "Max parallel request limit reached" in e.message
    ),  # the result of the logical expression is on the second position
)
async def chat_completion(
    request: Request,
    fastapi_response: Response,
    model: Optional[str] = None,
    user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),
):
    global general_settings, user_debug, proxy_logging_obj, llm_model_list
    indah4(f"/v1/chat/completions: {request}.", warna='cyan')
    data = {}

    from schnell.app.llmutils.langchainutils.proxy.litellm.settings import debug_litellm

    try:
        indah4(f"""chat_completion #1
        general_settings = {general_settings}
        user_debug = {user_debug}
        proxy_logging_obj = {proxy_logging_obj}
        llm_model_list = {llm_model_list}
        """, warna='red')

        body = await request.body()
        body_str = body.decode()

        try:

            indah4(f"chat_completion #2, body_str={body_str}", warna='cyan')

            data = ast.literal_eval(body_str)

        except:
            data = json.loads(body_str)

        if debug_litellm:
            indah4("chat_completion #3", warna='cyan')

        # Azure OpenAI only: check if user passed api-version
        query_params = dict(request.query_params)

        if debug_litellm:
            indah4(f"chat_completion #4, query_params={query_params}", warna='cyan')

        if "api-version" in query_params:
            data["api_version"] = query_params["api-version"]

        if debug_litellm:
            indah4("chat_completion #5", warna='cyan')

        # Include original request and headers in the data
        data["proxy_server_request"] = {
            "url": str(request.url),
            "method": request.method,
            "headers": dict(request.headers),
            "body": copy.copy(data),  # use copy instead of deepcopy
        }

        if debug_litellm:
            indah4(f"chat_completion #6, data={data}", warna='cyan')

        ## Cache Controls
        headers = request.headers
        verbose_proxy_logger.debug("Request Headers: %s", headers)
        cache_control_header = headers.get("Cache-Control", None)
        if cache_control_header:
            cache_dict = parse_cache_control(cache_control_header)
            data["ttl"] = cache_dict.get("s-maxage")

        if debug_litellm:
            indah4("chat_completion #7", warna='cyan')

        verbose_proxy_logger.debug("receiving data: %s", data)

        data["model"] = (
            general_settings.get("completion_model", None)  # server default
            or user_model  # model name passed via cli args
            or model  # for azure deployments
            or data["model"]  # default passed in http request
        )

        if debug_litellm:
            indah4(f"chat_completion #8, data={data}", warna='cyan')

        # users can pass in 'user' param to /chat/completions. Don't override it
        if data.get("user", None) is None and user_api_key_dict.user_id is not None:
            # if users are using user_api_key_auth, set `user` in `data`
            data["user"] = user_api_key_dict.user_id

        if debug_litellm:
            indah4("chat_completion #9", warna='cyan')

        if "metadata" not in data:
            data["metadata"] = {}
        data["metadata"]["user_api_key"] = user_api_key_dict.api_key
        data["metadata"]["user_api_key_alias"] = getattr(user_api_key_dict, "key_alias", None)
        data["metadata"]["user_api_key_user_id"] = user_api_key_dict.user_id
        data["metadata"]["user_api_key_org_id"] = user_api_key_dict.org_id
        data["metadata"]["user_api_key_team_id"] = getattr(user_api_key_dict, "team_id", None)
        data["metadata"]["user_api_key_team_alias"] = getattr(user_api_key_dict, "team_alias", None)
        data["metadata"]["user_api_key_metadata"] = user_api_key_dict.metadata
        _headers = dict(request.headers)
        _headers.pop("authorization", None)  # do not store the original `sk-..` api key in the db
        data["metadata"]["headers"] = _headers
        data["metadata"]["endpoint"] = str(request.url)

        if debug_litellm:
            indah4(f"chat_completion #10, data={data}", warna='cyan')

        ### TEAM-SPECIFIC PARAMS ###
        if user_api_key_dict.team_id is not None:
            team_config = await proxy_config.load_team_config(
                team_id=user_api_key_dict.team_id
            )
            if len(team_config) == 0:
                pass
            else:
                team_id = team_config.pop("team_id", None)
                _is_valid_team_configs(
                    team_id=team_id, team_config=team_config, request_data=data
                )
                data["metadata"]["team_id"] = team_id
                data = {
                    **team_config,
                    **data,
                }  # add the team-specific configs to the completion call

        if debug_litellm:
            indah4("chat_completion #11", warna='cyan')

        ### END-USER SPECIFIC PARAMS ###
        if user_api_key_dict.allowed_model_region is not None:
            data["allowed_model_region"] = user_api_key_dict.allowed_model_region

        global user_temperature, user_request_timeout, user_max_tokens, user_api_base

        if debug_litellm:
            indah4("chat_completion #12", warna='cyan')

        # override with user settings, these are params passed via cli
        if user_temperature:
            data["temperature"] = user_temperature
        if user_request_timeout:
            data["request_timeout"] = user_request_timeout
        if user_max_tokens:
            data["max_tokens"] = user_max_tokens
        if user_api_base:
            data["api_base"] = user_api_base

        if debug_litellm:
            indah4("chat_completion #13", warna='cyan')

        ### MODEL ALIAS MAPPING ###
        # check if model name in model alias map
        # get the actual model name
        if data["model"] in litellm.model_alias_map:
            data["model"] = litellm.model_alias_map[data["model"]]

        if debug_litellm:
            indah4(f"""chat_completion #14, data={data}""", warna='cyan')

        ## LOGGING OBJECT ## - initialize logging object for logging success/failure events for call
        data["litellm_call_id"] = str(uuid.uuid4())

        logging_obj, data = litellm.utils.function_setup(
            original_function="acompletion",
            rules_obj=litellm.utils.Rules(),
            start_time=datetime.now(),
            **data,
        )
        data["litellm_logging_obj"] = logging_obj

        if debug_litellm:
            indah4(f"chat_completion #15, llm_router={llm_router}, user_api_key_dict={user_api_key_dict}, logging_obj={logging_obj}", warna='blue')

        ### CALL HOOKS ### - modify incoming data before calling the model
        data = await proxy_logging_obj.pre_call_hook(
            user_api_key_dict=user_api_key_dict,
            data=data,
            call_type="completion"
        )
        tasks = []
        tasks.append(
            proxy_logging_obj.during_call_hook(
                data=data,
                user_api_key_dict=user_api_key_dict,
                call_type="completion",
            )
        )
        
        if debug_litellm:
            indah4(f"chat_completion #16, tasks={tasks}", warna='cyan')

        ### ROUTE THE REQUEST ###
        # Do not change this - it should be a constant time fetch - ALWAYS
        router_model_names = llm_router.model_names if llm_router is not None else []

        if debug_litellm:
            indah4(f"chat_completion #16-000, router_model_names={router_model_names}", warna='cyan')

        # skip router if user passed their key
        if "api_key" in data:
            tasks.append(litellm.acompletion(**data))
            if debug_litellm:
                indah4(f"chat_completion #16a", warna='cyan')
        elif "user_config" in data:
            # initialize a new router instance. make request using this Router
            router_config = data.pop("user_config")
            user_router = litellm.Router(**router_config)
            tasks.append(user_router.acompletion(**data))
            if debug_litellm:
                indah4(f"chat_completion #16b", warna='cyan')
        elif (llm_router is not None
            and data["model"] in router_model_names):  # model in router model list
            tasks.append(llm_router.acompletion(**data))
            if debug_litellm:
                indah4(f"chat_completion #16c", warna='cyan')
        elif (llm_router is not None
            and llm_router.model_group_alias is not None
            and data["model"] in llm_router.model_group_alias
        ):  # model set in model_group_alias
            tasks.append(llm_router.acompletion(**data))
            if debug_litellm:
                indah4(f"chat_completion #16d", warna='cyan')
        elif (llm_router is not None
            and data["model"] in llm_router.deployment_names
        ):  # model in router deployments, calling a specific deployment on the router
            tasks.append(llm_router.acompletion(**data, specific_deployment=True))
            if debug_litellm:
                indah4(f"chat_completion #16e", warna='cyan')
        elif (llm_router is not None
            and data["model"] not in router_model_names
            and llm_router.default_deployment is not None
        ):  # model in router deployments, calling a specific deployment on the router
            tasks.append(llm_router.acompletion(**data))
            if debug_litellm:
                indah4(f"chat_completion #16f", warna='cyan')
        elif user_model is not None:  # `litellm --model <your-model-name>`
            # ini kenapa jadi openai acompletion???
            tasks.append(litellm.acompletion(**data))

            # # chat_completion #16g
            # # litellm=<module 'schnell.app.llmutils.langchainutils.proxy.litellm' from 'c:\\users\\usef\\work\\sidoarjo\\schnell\\app\\llmutils\\langchainutils\\proxy\\litellm\\__init__.py'>
            # # litellm.acompletion=<function acompletion at 0x0000023FB67F5F80>
            # # inspect.getcoroutinename(my_coroutine)=acompletion
            # # inspect.getsourcefile(my_coroutine)=c:\users\usef\work\sidoarjo\schnell\app\llmutils\langchainutils\proxy\litellm\utils.py
            # # inspect.getmodule(my_coroutine)=<module 'schnell.app.llmutils.langchainutils.proxy.litellm.main' from 'c:\\users\\usef\\work\\sidoarjo\\schnell\\app\\llmutils\\langchainutils\\proxy\\litellm\\main.py'>
            if debug_litellm:
                indah4(f"""chat_completion #16g
            litellm={litellm}
            litellm.acompletion={litellm.acompletion}
            inspect.getcoroutinename(my_coroutine)={litellm.acompletion.__qualname__}
            inspect.getsourcefile(my_coroutine)={inspect.getsourcefile(litellm.acompletion)}
            inspect.getmodule(my_coroutine)={inspect.getmodule(litellm.acompletion)}
            """, warna='cyan')

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "error": "chat_completion: Invalid model name passed in model="
                    + data.get("model", "")
                },
            )
        
        if debug_litellm:
            indah4(f"chat_completion #17, tasks={tasks}", warna='cyan')

        # wait for call to end
        responses = await asyncio.gather(*tasks)  # run the moderation check in parallel to the actual llm api call
        response = responses[1]

        if debug_litellm:
            indah4("chat_completion #18", warna='cyan')

        hidden_params = getattr(response, "_hidden_params", {}) or {}
        model_id = hidden_params.get("model_id", None) or ""
        cache_key = hidden_params.get("cache_key", None) or ""
        api_base = hidden_params.get("api_base", None) or ""

        if debug_litellm:
            indah4("chat_completion #19", warna='cyan')

        # Post Call Processing
        if llm_router is not None:
            data["deployment"] = llm_router.get_deployment(model_id=model_id)
        data["litellm_status"] = "success"  # used for alerting

        if (
            "stream" in data and data["stream"] == True
        ):  # use generate_responses to stream responses
            custom_headers = {
                "x-litellm-model-id": model_id,
                "x-litellm-cache-key": cache_key,
                "x-litellm-model-api-base": api_base,
                "x-litellm-version": version,
            }
            selected_data_generator = select_data_generator(
                response=response,
                user_api_key_dict=user_api_key_dict,
                request_data=data,
            )
            return StreamingResponse(
                selected_data_generator,
                media_type="text/event-stream",
                headers=custom_headers,
            )

        fastapi_response.headers["x-litellm-model-id"] = model_id
        fastapi_response.headers["x-litellm-cache-key"] = cache_key
        fastapi_response.headers["x-litellm-model-api-base"] = api_base
        fastapi_response.headers["x-litellm-version"] = version

        if debug_litellm:
            indah4("chat_completion #20", warna='cyan')

        ### CALL HOOKS ### - modify outgoing data
        response = await proxy_logging_obj.post_call_success_hook(user_api_key_dict=user_api_key_dict, response=response)

        if debug_litellm:
            indah4("chat_completion #99", warna='green')

        return response

    except Exception as e:
        error_msg = f"{str(e)}"

        indah4(f"[{__file__}:1374] chat_completion #100/exception: {error_msg}", warna='red')

        data["litellm_status"] = "fail"  # used for alerting
        traceback.print_exc()
        await proxy_logging_obj.post_call_failure_hook(user_api_key_dict=user_api_key_dict, original_exception=e, request_data=data)
        # verbose_proxy_logger.debug
        print(
            f"\033[1;31mAn error occurred: {e}\n\n  Debug this by setting `--debug`, e.g. `litellm --model gpt-3.5-turbo --debug`"
        )
        router_model_names = llm_router.model_names if llm_router is not None else []
        if user_debug:
            traceback.print_exc()

        if isinstance(e, HTTPException):
            raise ProxyException(
                message=getattr(e, "detail", str(e)),
                type=getattr(e, "type", "None"),
                param=getattr(e, "param", "None"),
                code=getattr(e, "status_code", status.HTTP_400_BAD_REQUEST),
            )

        raise ProxyException(
            message=getattr(e, "message", error_msg),
            type=getattr(e, "type", "None"),
            param=getattr(e, "param", "None"),
            code=getattr(e, "status_code", 500),
        )


@router.post("/v1/completions", dependencies=[Depends(user_api_key_auth)], tags=["completions"]
)
@router.post("/completions", dependencies=[Depends(user_api_key_auth)], tags=["completions"]
)
@router.post("/engines/{model:path}/completions",
    dependencies=[Depends(user_api_key_auth)],
    tags=["completions"],
)
@router.post("/openai/deployments/{model:path}/completions",
    dependencies=[Depends(user_api_key_auth)],
    tags=["completions"],
)
async def completion(
    request: Request,
    fastapi_response: Response,
    model: Optional[str] = None,
    user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),
):
    global user_temperature, user_request_timeout, user_max_tokens, user_api_base
    indah4(f"/v1/completions: {request}.", warna='yellow')
    try:
        body = await request.body()
        body_str = body.decode()
        try:
            data = ast.literal_eval(body_str)
        except:
            data = json.loads(body_str)

        data["user"] = data.get("user", user_api_key_dict.user_id)
        data["model"] = (
            general_settings.get("completion_model", None)  # server default
            or user_model  # model name passed via cli args
            or model  # for azure deployments
            or data["model"]  # default passed in http request
        )
        if user_model:
            data["model"] = user_model
        if "metadata" not in data:
            data["metadata"] = {}
        data["metadata"]["user_api_key"] = user_api_key_dict.api_key
        data["metadata"]["user_api_key_metadata"] = user_api_key_dict.metadata
        data["metadata"]["user_api_key_alias"] = getattr(
            user_api_key_dict, "key_alias", None
        )
        data["metadata"]["user_api_key_user_id"] = user_api_key_dict.user_id
        data["metadata"]["user_api_key_team_id"] = getattr(
            user_api_key_dict, "team_id", None
        )
        data["metadata"]["user_api_key_team_alias"] = getattr(
            user_api_key_dict, "team_alias", None
        )
        _headers = dict(request.headers)
        _headers.pop(
            "authorization", None
        )  # do not store the original `sk-..` api key in the db
        data["metadata"]["headers"] = _headers
        data["metadata"]["endpoint"] = str(request.url)

        # override with user settings, these are params passed via cli
        if user_temperature:
            data["temperature"] = user_temperature
        if user_request_timeout:
            data["request_timeout"] = user_request_timeout
        if user_max_tokens:
            data["max_tokens"] = user_max_tokens
        if user_api_base:
            data["api_base"] = user_api_base

        ### MODEL ALIAS MAPPING ###
        # check if model name in model alias map
        # get the actual model name
        if data["model"] in litellm.model_alias_map:
            data["model"] = litellm.model_alias_map[data["model"]]

        ### CALL HOOKS ### - modify incoming data before calling the model
        data = await proxy_logging_obj.pre_call_hook(
            user_api_key_dict=user_api_key_dict, data=data, call_type="completion"
        )

        ### ROUTE THE REQUESTs ###
        router_model_names = llm_router.model_names if llm_router is not None else []
        # skip router if user passed their key
        if "api_key" in data:
            response = await litellm.atext_completion(**data)
        elif (
            llm_router is not None and data["model"] in router_model_names
        ):  # model in router model list
            response = await llm_router.atext_completion(**data)
        elif (
            llm_router is not None
            and llm_router.model_group_alias is not None
            and data["model"] in llm_router.model_group_alias
        ):  # model set in model_group_alias
            response = await llm_router.atext_completion(**data)
        elif (
            llm_router is not None and data["model"] in llm_router.deployment_names
        ):  # model in router deployments, calling a specific deployment on the router
            response = await llm_router.atext_completion(
                **data, specific_deployment=True
            )
        elif (
            llm_router is not None
            and data["model"] not in router_model_names
            and llm_router.default_deployment is not None
        ):  # model in router deployments, calling a specific deployment on the router
            response = await llm_router.atext_completion(**data)
        elif user_model is not None:  # `litellm --model <your-model-name>`
            response = await litellm.atext_completion(**data)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "error": "completion: Invalid model name passed in model="
                    + data.get("model", "")
                },
            )

        hidden_params = getattr(response, "_hidden_params", {}) or {}
        model_id = hidden_params.get("model_id", None) or ""
        cache_key = hidden_params.get("cache_key", None) or ""
        api_base = hidden_params.get("api_base", None) or ""

        verbose_proxy_logger.debug("final response: %s", response)
        if (
            "stream" in data and data["stream"] == True
        ):  # use generate_responses to stream responses
            custom_headers = {
                "x-litellm-model-id": model_id,
                "x-litellm-cache-key": cache_key,
                "x-litellm-model-api-base": api_base,
                "x-litellm-version": version,
            }
            selected_data_generator = select_data_generator(
                response=response,
                user_api_key_dict=user_api_key_dict,
                request_data=data,
            )

            return StreamingResponse(
                selected_data_generator,
                media_type="text/event-stream",
                headers=custom_headers,
            )

        fastapi_response.headers["x-litellm-model-id"] = model_id
        fastapi_response.headers["x-litellm-cache-key"] = cache_key
        fastapi_response.headers["x-litellm-model-api-base"] = api_base
        fastapi_response.headers["x-litellm-version"] = version

        return response
    except Exception as e:
        data["litellm_status"] = "fail"  # used for alerting
        verbose_proxy_logger.debug("EXCEPTION RAISED IN PROXY MAIN.PY")
        verbose_proxy_logger.debug(
            "\033[1;31mAn error occurred: %s\n\n Debug this by setting `--debug`, e.g. `litellm --model gpt-3.5-turbo --debug`",
            e,
        )
        traceback.print_exc()
        error_traceback = traceback.format_exc()
        error_msg = f"{str(e)}"
        raise ProxyException(
            message=getattr(e, "message", error_msg),
            type=getattr(e, "type", "None"),
            param=getattr(e, "param", "None"),
            code=getattr(e, "status_code", 500),
        )

# save_worker_config(
#     model=model,
#     alias=alias,
#     api_base=api_base,
#     api_version=api_version,
#     debug=debug,
#     detailed_debug=detailed_debug,
#     temperature=temperature,
#     max_tokens=max_tokens,
#     request_timeout=request_timeout,
#     max_budget=max_budget,
#     telemetry=telemetry,
#     drop_params=drop_params,
#     add_function_to_prompt=add_function_to_prompt,
#     headers=headers,
#     save=save,
#     config=config,
#     use_queue=use_queue,
# )
# os.environ["WORKER_CONFIG"] = json.dumps(data)
# worker_config = json.loads(os.getenv("WORKER_CONFIG"))
# await initialize(**worker_config)


async def initialize(
    model=None,  # gemini/gemini-pro
    alias=None,  # @click.option("--alias", default=None, help='The alias for the model - use this to give a litellm model name (e.g. "huggingface/codellama/CodeLlama-7b-Instruct-hf") a more user-friendly name ("codellama")',
    api_base=None,  # @click.option("--api_base", default=None, help="API base URL.")
    api_version=None,  # @click.option("--api_version", default="2023-07-01-preview",
    debug=False,  # @click.option("--debug", default=False,
    detailed_debug=False,  # @click.option("--detailed_debug", default=False,
    temperature=None,  # @click.option("--temperature", default=None, type=float, help="Set temperature for the model"
    max_tokens=None,  # @click.option("--max_tokens", default=None, type=int, help="Set max tokens for the model"
    request_timeout=600,
    max_budget=None,  # @click.option("--max_budget", default=None,
    telemetry=False,
    drop_params=True,
    add_function_to_prompt=True,
    headers=None,
    save=False,
    use_queue=False,
    config=None,
):
    global user_model, user_api_base, user_debug, user_detailed_debug, user_user_max_tokens, user_request_timeout, user_temperature, user_telemetry, user_headers, experimental, llm_model_list, llm_router, general_settings, master_key, user_custom_auth, prisma_client

    # generate_feedback_box()
    user_model = model
    user_debug = debug

    if debug == True:  # this needs to be first, so users can see Router init debugg
        from schnell.app.llmutils.langchainutils.proxy.litellm._logging import (
            verbose_router_logger,
            verbose_proxy_logger,
            verbose_logger,
        )
        import logging

        # this must ALWAYS remain logging.INFO, DO NOT MODIFY THIS
        verbose_logger.setLevel(level=logging.INFO)  # sets package logs to info
        verbose_router_logger.setLevel(level=logging.INFO)  # set router logs to info
        verbose_proxy_logger.setLevel(level=logging.INFO)  # set proxy logs to info

    # if detailed_debug == True:
    #     from schnell.app.llmutils.langchainutils.proxy.litellm._logging import (
    #         verbose_router_logger,
    #         verbose_proxy_logger,
    #         verbose_logger,
    #     )
    #     import logging

    #     verbose_logger.setLevel(level=logging.DEBUG)  # set package log to debug
    #     verbose_router_logger.setLevel(level=logging.DEBUG)  # set router logs to debug
    #     verbose_proxy_logger.setLevel(level=logging.DEBUG)  # set proxy logs to debug

    elif debug == False and detailed_debug == False:
        # users can control proxy debugging using env variable = 'LITELLM_LOG'
        litellm_log_setting = os.environ.get("LITELLM_LOG", "")
        if litellm_log_setting != None:
            if litellm_log_setting.upper() == "INFO":
                from schnell.app.llmutils.langchainutils.proxy.litellm._logging import verbose_router_logger, verbose_proxy_logger
                import logging

                # this must ALWAYS remain logging.INFO, DO NOT MODIFY THIS

                verbose_router_logger.setLevel(
                    level=logging.INFO
                )  # set router logs to info
                verbose_proxy_logger.setLevel(
                    level=logging.INFO
                )  # set proxy logs to info
            elif litellm_log_setting.upper() == "DEBUG":
                from schnell.app.llmutils.langchainutils.proxy.litellm._logging import verbose_router_logger, verbose_proxy_logger
                import logging

                verbose_router_logger.setLevel(
                    level=logging.DEBUG
                )  # set router logs to info
                verbose_proxy_logger.setLevel(
                    level=logging.DEBUG
                )  # set proxy logs to debug

    dynamic_config = {"general": {}, user_model: {}}

    # if config:
    #     (
    #         llm_router,
    #         llm_model_list,
    #         general_settings,
    #     ) = await proxy_config.load_config(router=llm_router, config_file_path=config)
    # if headers:  # model-specific param
    #     user_headers = headers
    #     dynamic_config[user_model]["headers"] = headers
    # if api_base:  # model-specific param
    #     user_api_base = api_base
    #     dynamic_config[user_model]["api_base"] = api_base
    # if api_version:
    #     os.environ["AZURE_API_VERSION"] = (
    #         api_version  # set this for azure - litellm can read this from the env
    #     )
    if max_tokens:  # model-specific param
        user_max_tokens = max_tokens
        dynamic_config[user_model]["max_tokens"] = max_tokens
    if temperature:  # model-specific param
        user_temperature = temperature
        dynamic_config[user_model]["temperature"] = temperature
    if request_timeout:
        user_request_timeout = request_timeout
        dynamic_config[user_model]["request_timeout"] = request_timeout
    if alias:  # model-specific param
        dynamic_config[user_model]["alias"] = alias
    if drop_params == True:  # litellm-specific param
        litellm.drop_params = True
        dynamic_config["general"]["drop_params"] = True
    if add_function_to_prompt == True:  # litellm-specific param
        litellm.add_function_to_prompt = True
        dynamic_config["general"]["add_function_to_prompt"] = True
    # if max_budget:  # litellm-specific param
    #     litellm.max_budget = max_budget
    #     dynamic_config["general"]["max_budget"] = max_budget
    # if experimental:
    #     pass
    user_telemetry = telemetry

    indah4(f"""[{__file__}:3189] initialize
    user_model = {user_model}
    user_api_base = {user_api_base}
    user_debug = {user_debug}
    user_request_timeout = {user_request_timeout}
    user_temperature = {user_temperature}
    user_telemetry = {user_telemetry}
    user_headers = {user_headers}
    experimental = {experimental}
    llm_model_list = {llm_model_list}
    llm_router = {llm_router}
    general_settings = {general_settings}
    master_key = {master_key}
    user_custom_auth = {user_custom_auth}
    prisma_client = {prisma_client}
    """, warna="cyan")


# from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# from typing import List

# router = APIRouter()

# Define the response model structure
class ModelInfo(BaseModel):
    name: str
    label: str
    provider: str

# Mock data for the models; replace with actual data as needed
models_data = [
    {"name": "grok-beta", "label": "Grok", "provider": "OpenAILike"},
    # {"name": "model-2", "label": "model-2", "provider": "OpenAILike"},
    # Add more models as needed
]

@router.get("/v1/models", response_model=List[ModelInfo])
async def get_models():
    try:
        return models_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching models") from e


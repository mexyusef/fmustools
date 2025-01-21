# print('llm1')
from schnell.app.llmutils.langchainutils.llm_config import all_accounts
# print('llm2')
from schnell.app.llmutils.langchainutils.llm_config import change_active_model
# print('llm3')
from schnell.app.llmutils.langchainutils.llm_config import invoke_all
# print('llm4')
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm
# print('llm5')
from schnell.app.llmutils.langchainutils.llms.invoker import invoke_llm_all
# print('llm6')

# result = invoke_llm(skeleton_code_prompt, llm_name=llm_name)
# indah3(result, warna='green')
# result = invoke_llm(current_line, all_accounts['active'])
# indah3(result, warna='yellow')

# from schnell.db.llms import quick_invoke
def quick_invoke(user_query):
    result = invoke_llm(user_query, all_accounts['active'])
    return result

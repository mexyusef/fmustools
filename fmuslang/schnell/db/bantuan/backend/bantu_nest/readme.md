oprek model

  @Field()
  @Column ({nullable: true, length: 100})
  name: string;
__TEMPLATE_APP_ORMENTITY_WITHOUT_ID


  readonly name: string;
__TEMPLATE_APP_ORM_CREATEINPUT_WITHOUT_ID


ini adlh badan utk crud update rest
  readonly name: string;
__TEMPLATE_APP_ORM_UPDATEINPUT_WITHOUT_ID

  @Field()
  name: string;
__TEMPLATE_APP_GQLENTITY_WITHOUT_ID


  @Field()
  @IsNotEmpty()
  // @IsEmail()
  name: string;
__TEMPLATE_APP_GQL_CREATEINPUT_WITHOUT_ID


di sini badan tanpa id krn id sudah ditaro di atas dari kolom2 lainnya
beda dg rest dimana id sudah dihandle controller, dia hanya minta badan tanpa id
  @Field()
  // @IsOptional()
  @IsNotEmpty()
  name: string;
__TEMPLATE_APP_GQL_UPDATEINPUT_WITHOUT_ID


ini utk detail, bergantung badannya
kolom name -> find/detail by name
  @Field()
  @IsNotEmpty()
  name: string;

__TEMPLATE_APP_GQL_DETAIL_BY_COLUMN

**/home/usef/danger/ulib/schnell/db/bantuan/templates/,d
  nestjs_app_content_v1,f(t=)
  nestjs_app_rest_module_v1,f(t=)
  nestjs_app_rest_model_v1,f(t=)
  nestjs_app_rest_resolver_v1,f(t=)
  nestjs_app_rest_resolverspec_v1,f(t=)
  nestjs_app_rest_controller_v1,f(t=)
  nestjs_app_rest_controllerspec_v1,f(t=)
  nestjs_app_rest_service_v1,f(t=)
  nestjs_app_rest_servicespec_v1,f(t=)
  
tpl_appindex = joiner(TEMPLATESDIR, 'nestjs_app_rest_index_v1.tpl')
tpl_appcontroller = joiner(TEMPLATESDIR, 'nestjs_app_rest_controller_v1.tpl')
tpl_appmodel = joiner(TEMPLATESDIR, 'nestjs_app_rest_model_v1.tpl')
tpl_appservice = joiner(TEMPLATESDIR, 'nestjs_app_rest_service_v1.tpl')

tpl_appcontent = joiner(TEMPLATESDIR, 'nestjs_app_content_v1.tpl')

tpl_appmodule = joiner(TEMPLATESDIR, 'nestjs_app_rest_module_v1.tpl')
tpl_appmodel = joiner(TEMPLATESDIR, 'nestjs_app_rest_model_v1.tpl')
tpl_appresolver = joiner(TEMPLATESDIR, 'nestjs_app_rest_resolver_v1.tpl')
tpl_appresolver_spec = joiner(TEMPLATESDIR, 'nestjs_app_rest_resolverspec_v1.tpl')
tpl_appcontroller = joiner(TEMPLATESDIR, 'nestjs_app_rest_controller_v1.tpl')
tpl_appcontroller_spec = joiner(TEMPLATESDIR, 'nestjs_app_rest_controllerspec_v1.tpl')
tpl_appservice = joiner(TEMPLATESDIR, 'nestjs_app_rest_service_v1.tpl')
tpl_appservice_spec = joiner(TEMPLATESDIR, 'nestjs_app_rest_servicespec_v1.tpl')

attendee,d(/mk)
  attendee.module.ts,f(e=utama=/nestjs/src/attendee/attendee.module.ts)
  attendee.model.ts,f(e=utama=/nestjs/src/attendee/attendee.model.ts)
  attendee.resolver.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.ts)
  attendee.resolver.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.spec.ts)
  attendee.controller.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.ts)
  attendee.controller.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.spec.ts)
  attendee.service.ts,f(e=utama=/nestjs/src/attendee/attendee.service.ts)
  attendee.service.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.service.spec.ts)


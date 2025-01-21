nestjs_controller_template = """
export class __TABLENAME__Controller {

	constructor(private readonly __TABLENAME_LOWER__Service: __TABLENAME__Service) {}

	@Post()
	public async create(@Body() create__TABLENAME__DTO: Create__TABLENAME__DTO) {
		return await this.__TABLENAME_LOWER__Service.create(create__TABLENAME__DTO);
	}

	@Get()
	public async getList() {
		return await this.__TABLENAME_LOWER__Service.getList();
	}

	@Get('/:id')
  public async getDetail(@Param('id') __TABLENAME_LOWER__Id: number) {
		return await this.__TABLENAME_LOWER__Service.getDetail(__TABLENAME_LOWER__Id);
	}

	@Put('/:id')
  public async update(@Param('id') __TABLENAME_LOWER__Id: number, @Body() update__TABLENAME__DTO: Update__TABLENAME__DTO) {
		return await this.__TABLENAME_LOWER__Service.updateOne(__TABLENAME_LOWER__Id, update__TABLENAME__DTO);
	}

	@Delete('/:id')
	@HttpCode(HttpStatus.NO_CONTENT)
  public async delete(@Param('id') __TABLENAME_LOWER__Id: number) {
		await this.__TABLENAME_LOWER__Service.delete(__TABLENAME_LOWER__Id);
	}

}
"""

nestjs_service_template = """
export class __TABLENAME__Service {

	constructor(@InjectRepository(__TABLENAME__) private __TABLENAME_LOWER__Repository: Repository<__TABLENAME__>) {}

  private entityToDTO(__TABLENAME_LOWER__: __TABLENAME__): __TABLENAME__DTO {
    const __TABLENAME_LOWER__DTO = new __TABLENAME__DTO();
    __TABLENAME_LOWER__DTO.id = __TABLENAME_LOWER__.id;
    __TABLENAME_LOWER__DTO.title = __TABLENAME_LOWER__.title;
    __TABLENAME_LOWER__DTO.description = __TABLENAME_LOWER__.description;
    __TABLENAME_LOWER__DTO.status = __TABLENAME_LOWER__.status;
    return __TABLENAME_LOWER__DTO;
  }

  public async create(create__TABLENAME__DTO: Create__TABLENAME__DTO) {
    const __TABLENAME_LOWER__: __TABLENAME__ = new __TABLENAME__();
    __TABLENAME_LOWER__.title = create__TABLENAME__DTO.title;
    __TABLENAME_LOWER__.description = create__TABLENAME__DTO.description;
    __TABLENAME_LOWER__.status = __TABLENAME__Status.Created;
    await this.__TABLENAME_LOWER__Repository.save(__TABLENAME__);

    const __TABLENAME_LOWER__DTO = this.entityToDTO(__TABLENAME_LOWER__);
    return __TABLENAME_LOWER__DTO;
  }

  public async getList() {
    const __TABLENAME_LOWER__s: __TABLENAME__[] = await this.__TABLENAME_LOWER__Repository.find();
    const __TABLENAME_LOWER__DTOs: __TABLENAME__DTO[] = __TABLENAME_LOWER__s
      .map(x => this.entityToDTO(x));

    return __TABLENAME_LOWER__DTOs;	
  }
 
  public async getDetail(__TABLENAME_LOWER__Id: number) {
    const __TABLENAME_LOWER__: __TABLENAME__ = await this.__TABLENAME_LOWER__Repository.findOne(__TABLENAME_LOWER__Id);
    if (!__TABLENAME_LOWER__) throw new NotFoundException(`__TABLENAME_LOWER__ with id ${__TABLENAME_LOWER__Id} not found`);
    const __TABLENAME_LOWER__DTO: __TABLENAME__DTO = this.entityToDTO(__TABLENAME_LOWER__);
    return __TABLENAME_LOWER__DTO;
  }

  public async update(__TABLENAME_LOWER__Id: number, update__TABLENAME__DTO: Update__TABLENAME__DTO) {
    const __TABLENAME_LOWER__: __TABLENAME__ = await this.getDetail(__TABLENAME_LOWER__Id);
    if (update__TABLENAME__DTO.title) __TABLENAME_LOWER__.title = update__TABLENAME__DTO.title;
    if (update__TABLENAME__DTO.description) __TABLENAME_LOWER__.description = update__TABLENAME__DTO.description;
    if (update__TABLENAME__DTO.status) __TABLENAME_LOWER__.status = update__TABLENAME__DTO.status;
    await this.__TABLENAME_LOWER__Repository.save(__TABLENAME_LOWER__);

    const __TABLENAME_LOWER__DTO: __TABLENAME__DTO = this.entityToDTO(__TABLENAME_LOWER__);
    return __TABLENAME_LOWER__DTO;
  }

  public async delete(__TABLENAME_LOWER__Id: number) {
    const __TABLENAME_LOWER__: __TABLENAME__ = await this.getDetail(__TABLENAME_LOWER__Id);
    await this.__TABLENAME_LOWER__Repository.remove(__TABLENAME_LOWER__);
  }
	
}
"""

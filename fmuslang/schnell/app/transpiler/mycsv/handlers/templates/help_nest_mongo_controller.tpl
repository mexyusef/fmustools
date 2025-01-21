import { 
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Patch,
  Post, 
  Put
} from '@nestjs/common';

import { __TEMPLATE_MODELNAME_CASE__Service } from './__TEMPLATE_MODELNAME_LOWER__.service';

@Controller('__TEMPLATE_MODELNAME_LOWER__')
export class __TEMPLATE_MODELNAME_CASE__Controller {

  constructor(private readonly __TEMPLATE_MODELNAME_LOWER__Service: __TEMPLATE_MODELNAME_CASE__Service) {}

  @Get()
  async getAll__TEMPLATE_MODELNAME_CASE__s() {
    const __TEMPLATE_MODELNAME_LOWER__s = await this.__TEMPLATE_MODELNAME_LOWER__Service.list__TEMPLATE_MODELNAME_CASE__s();
    return __TEMPLATE_MODELNAME_LOWER__s;
  }

  @Get(':id')
  get__TEMPLATE_MODELNAME_CASE__(@Param('id') __TEMPLATE_MODELNAME_LOWER__Id: string) {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.detail__TEMPLATE_MODELNAME_CASE__(__TEMPLATE_MODELNAME_LOWER__Id);
  }

  @Post()
  async add__TEMPLATE_MODELNAME_CASE__(
__TAB2_TEMPLATE_BODIFIED__
  ) {
    const generatedId = await this.__TEMPLATE_MODELNAME_LOWER__Service.create__TEMPLATE_MODELNAME_CASE__(
      category, checked, content, description, images, inStock, price, sold, title
    );
    return { id: generatedId };
  }

  @Patch(':id')
  async update__TEMPLATE_MODELNAME_CASE__(
    @Param('id') __TEMPLATE_MODELNAME_LOWER__Id: string,

__TAB2_TEMPLATE_BODIFIED__

  ) {
    await this.__TEMPLATE_MODELNAME_LOWER__Service.update__TEMPLATE_MODELNAME_CASE__(
      __TEMPLATE_MODELNAME_LOWER__Id,
      category, checked, content, description, images, inStock, price, sold, title
    );
    return null;
  }

  @Delete(':id')
  async remove__TEMPLATE_MODELNAME_CASE__(@Param('id') __TEMPLATE_MODELNAME_LOWER__Id: string) {
    await this.__TEMPLATE_MODELNAME_LOWER__Service.delete__TEMPLATE_MODELNAME_CASE__(__TEMPLATE_MODELNAME_LOWER__Id);
    return null;
  }

}


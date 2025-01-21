import { 
  Body, 
  Controller, 
  Delete, 
  Get, 
  Param, 
  Post, 
  Put 
} from '@nestjs/common';
import { DeleteResult } from 'typeorm';
import { 
  __TEMPLATE_MODELNAME_CASE__Entity, 
  __TEMPLATE_MODELNAME_CASE__RO, 
  __TEMPLATE_MODELNAME_CASE__sRO, 
  Create__TEMPLATE_MODELNAME_CASE__Dto 
} from './__TEMPLATE_MODELNAME_LOWER__.rest';
import { __TEMPLATE_MODELNAME_CASE__Service } from './__TEMPLATE_MODELNAME_LOWER__.service';

@Controller('__TEMPLATE_MODELNAME_LOWER__')
export class __TEMPLATE_MODELNAME_CASE__Controller {

  constructor(private readonly __TEMPLATE_MODELNAME_LOWER__Service: __TEMPLATE_MODELNAME_CASE__Service) {}

  // *~localhost:3000/__TEMPLATE_MODELNAME_LOWER__
  @Get()
  public async getList(): Promise<__TEMPLATE_MODELNAME_CASE__sRO> {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.getList();
  }

  // *~localhost:3000/__TEMPLATE_MODELNAME_LOWER__/6
  @Get('/:id')
  public async getDetail(@Param('id') id: number): Promise<__TEMPLATE_MODELNAME_CASE__RO> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Detail controller: receiving ${id}.`);
    return this.__TEMPLATE_MODELNAME_LOWER__Service.getDetail({id});
  }

  // *~localhost:3000/__TEMPLATE_MODELNAME_LOWER__ p json {title=__TEMPLATE_MODELNAME_CASE__ no 5,description=semoga masuk ya, status=0}
  @Post()
  public async create(@Body() data: Create__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__Entity> {    
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Create controller: receiving ${JSON.stringify(data)}.`);
    return this.__TEMPLATE_MODELNAME_LOWER__Service.create(data);
  }

  // *~localhost:3000/__TEMPLATE_MODELNAME_LOWER__/6 u json {title=Empat jadi Tidak sempat}
  @Put('/:id')
  public async update(@Param('id') id: number, @Body() data: Create__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__RO> {    
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Update controller: receiving ${id} = ${JSON.stringify(data)}.`);
    return this.__TEMPLATE_MODELNAME_LOWER__Service.update({id}, data);
  }

  // *~localhost:3000/__TEMPLATE_MODELNAME_LOWER__/3 d
  @Delete('/:id')
  public async delete(@Param('id') id: number): Promise<DeleteResult> {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.delete({id});
  }

}


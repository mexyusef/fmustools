import { 
  Body, 
  Controller, 
  Delete, 
  Get, 
  Param, 
  Post, 
  Put 
} from '@nestjs/common';

import { 
  DeleteResult
} from 'typeorm';

import { 
  __TEMPLATE_MODELNAME_CASE__Entity, 
  __TEMPLATE_MODELNAME_CASE__RO, 
  __TEMPLATE_MODELNAME_CASE__sRO, 
  Create__TEMPLATE_MODELNAME_CASE__Dto, 
  Update__TEMPLATE_MODELNAME_CASE__Dto
} from './__TEMPLATE_MODELNAME_LOWER__.model';

import { __TEMPLATE_MODELNAME_CASE__Service } from './__TEMPLATE_MODELNAME_LOWER__.service';

@Controller('__TEMPLATE_MODELNAME_LOWER__')
export class __TEMPLATE_MODELNAME_CASE__Controller {

  constructor(private readonly bookService: __TEMPLATE_MODELNAME_CASE__Service) {}

  // *~localhost:9500/__TEMPLATE_MODELNAME_LOWER__
  @Get()
  public async getList(): Promise<__TEMPLATE_MODELNAME_CASE__sRO> {
    return this.bookService.getList();
  }

  // *~localhost:9500/__TEMPLATE_MODELNAME_LOWER__/6
  @Get('/:id')
  public async getDetail(@Param('id') id: number): Promise<__TEMPLATE_MODELNAME_CASE__RO> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Detail controller: receiving ${id}.`);
    return this.bookService.getDetail({id});
  }

  // *~localhost:9500/__TEMPLATE_MODELNAME_LOWER__ p json {title=__TEMPLATE_MODELNAME_CASE__ no 5,description=semoga masuk ya, status=0}
  @Post()
  public async create(@Body() data: Create__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__Entity> {    
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Create controller: receiving ${JSON.stringify(data)}.`);
    return this.bookService.create(data);
  }

  // *~localhost:9500/__TEMPLATE_MODELNAME_LOWER__/6 u json {title=Empat jadi Tidak sempat}
  @Put('/:id')
  public async update(@Param('id') id: number, @Body() data: Update__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__RO> {    
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Update controller: receiving ${id} = ${JSON.stringify(data)}.`);
    return this.bookService.update({id}, data);
  }

  // *~localhost:9500/__TEMPLATE_MODELNAME_LOWER__/3 d
  @Delete('/:id')
  public async delete(@Param('id') id: number): Promise<DeleteResult> {
    return this.bookService.delete({id});
  }

}

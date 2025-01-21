import { Injectable } from '@nestjs/common';
import {
  __TEMPLATE_MODELNAME_CASE__Entity,
  __TEMPLATE_MODELNAME_CASE__sRO,
  __TEMPLATE_MODELNAME_CASE__RO,
  Create__TEMPLATE_MODELNAME_CASE__Dto, 
  Update__TEMPLATE_MODELNAME_CASE__Dto,
} from './__TEMPLATE_MODELNAME_LOWER__.rest';
import { 
  DeleteResult,
  Repository,
  getRepository,
} from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';


@Injectable()
export class __TEMPLATE_MODELNAME_CASE__Service {

  constructor(
    @InjectRepository(__TEMPLATE_MODELNAME_CASE__Entity)
    private readonly __TEMPLATE_MODELNAME_LOWER__Repository: Repository<__TEMPLATE_MODELNAME_CASE__Entity>,
  ) {}

  public async create(data: Create__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__Entity> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Create service: receiving ${JSON.stringify(data)}.`);
    let __TEMPLATE_MODELNAME_LOWER__ = new __TEMPLATE_MODELNAME_CASE__Entity();
    __TEMPLATE_MODELNAME_LOWER__.title = data.title;
    __TEMPLATE_MODELNAME_LOWER__.description = data.description;
    __TEMPLATE_MODELNAME_LOWER__.status = data.status;
    const new__TEMPLATE_MODELNAME_CASE__ = await this.__TEMPLATE_MODELNAME_LOWER__Repository.save(__TEMPLATE_MODELNAME_LOWER__);
    return new__TEMPLATE_MODELNAME_CASE__;
  }

  public async getList(): Promise<__TEMPLATE_MODELNAME_CASE__sRO> {
    const __TEMPLATE_MODELNAME_LOWER__ = await this.__TEMPLATE_MODELNAME_LOWER__Repository.find();
    const qb = await getRepository(__TEMPLATE_MODELNAME_CASE__Entity)
      .createQueryBuilder('__TEMPLATE_MODELNAME_LOWER__')
    const __TEMPLATE_MODELNAME_LOWER__Count = await qb.getCount();
    return { __TEMPLATE_MODELNAME_LOWER__, __TEMPLATE_MODELNAME_LOWER__Count };
  }

  public async getDetail(where): Promise<__TEMPLATE_MODELNAME_CASE__RO> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Detail service: receiving ${JSON.stringify(where)}.`);
    const __TEMPLATE_MODELNAME_LOWER__ = await this.__TEMPLATE_MODELNAME_LOWER__Repository.findOne(where);
    return { __TEMPLATE_MODELNAME_LOWER__ };
  }

  public async update({ id }, data: Update__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__RO> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.__TEMPLATE_MODELNAME_LOWER__Repository.findOne({ id });
    let updated = Object.assign(toUpdate, data);
    const __TEMPLATE_MODELNAME_LOWER__ = await this.__TEMPLATE_MODELNAME_LOWER__Repository.save(updated);
    return { __TEMPLATE_MODELNAME_LOWER__ };
  }

  public async delete({ id }): Promise<DeleteResult> {
    return await this.__TEMPLATE_MODELNAME_LOWER__Repository.delete({ id });
  }

}

import { Injectable } from '@nestjs/common';
import {
  __TEMPLATE_TABLENAME_CASE__Entity,
  __TEMPLATE_TABLENAME_CASE__sRO,
  __TEMPLATE_TABLENAME_CASE__RO,
  Create__TEMPLATE_TABLENAME_CASE__Dto, 
  Update__TEMPLATE_TABLENAME_CASE__Dto,
  // Create__TEMPLATE_TABLENAME_CASE__Input, 
  Delete__TEMPLATE_TABLENAME_CASE__Input, 
  Update__TEMPLATE_TABLENAME_CASE__Input, 
  // Get__TEMPLATE_TABLENAME_CASE__Args, 
  // Get__TEMPLATE_TABLENAME_CASE__sArgs,
  // DeleteResultType,
} from './__TEMPLATE_TABLENAME_LOWER__.model';

import {
  DeleteResultType
} from '../common';

import { 
  DeleteResult,
  Repository,
  getRepository,
} from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';


@Injectable()
export class __TEMPLATE_TABLENAME_CASE__Service {

  constructor(
    @InjectRepository(__TEMPLATE_TABLENAME_CASE__Entity)
    private readonly __TEMPLATE_TABLENAME_LOWER__Repository: Repository<__TEMPLATE_TABLENAME_CASE__Entity>
  ) {}

  public async create(data: Create__TEMPLATE_TABLENAME_CASE__Dto): Promise<__TEMPLATE_TABLENAME_CASE__Entity> {
    // console.log(`__TEMPLATE_TABLENAME_CASE__ Create service: receiving ${JSON.stringify(data)}.`);
    let __TEMPLATE_TABLENAME_LOWER__ = new __TEMPLATE_TABLENAME_CASE__Entity();
    __TEMPLATE_TABLENAME_LOWER__.name = data.name;
    // __TEMPLATE_TABLENAME_LOWER__.description = data.description;
    // __TEMPLATE_TABLENAME_LOWER__.status = data.status;
    const new__TEMPLATE_TABLENAME_CASE__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.save(__TEMPLATE_TABLENAME_LOWER__);
    return new__TEMPLATE_TABLENAME_CASE__;
  }

  public async getList(): Promise<__TEMPLATE_TABLENAME_CASE__sRO> {
    const __TEMPLATE_TABLENAME_LOWER__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.find();
    const qb = await getRepository(__TEMPLATE_TABLENAME_CASE__Entity)
      .createQueryBuilder('__TEMPLATE_TABLENAME_LOWER__')
    const __TEMPLATE_TABLENAME_LOWER__Count = await qb.getCount();
    return { __TEMPLATE_TABLENAME_LOWER__, __TEMPLATE_TABLENAME_LOWER__Count };
  }

  public async getListGQL(): Promise<__TEMPLATE_TABLENAME_CASE__Entity[]> {
    const __TEMPLATE_TABLENAME_LOWER__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.find();
    // const qb = await getRepository(__TEMPLATE_TABLENAME_CASE__Entity).createQueryBuilder('__TEMPLATE_TABLENAME_LOWER__')
    // const __TEMPLATE_TABLENAME_LOWER__Count = await qb.getCount();
    return __TEMPLATE_TABLENAME_LOWER__;
  }

  public async getDetail(where): Promise<__TEMPLATE_TABLENAME_CASE__RO> {
    // console.log(`__TEMPLATE_TABLENAME_CASE__ Detail service: receiving ${JSON.stringify(where)}.`);
    const __TEMPLATE_TABLENAME_LOWER__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.findOne(where);
    return { __TEMPLATE_TABLENAME_LOWER__ };
  }

  public async getDetailGQL(where): Promise<__TEMPLATE_TABLENAME_CASE__Entity> {
    // console.log(`__TEMPLATE_TABLENAME_CASE__ Detail service: receiving ${JSON.stringify(where)}.`);
    const __TEMPLATE_TABLENAME_LOWER__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.findOne(where);
    return __TEMPLATE_TABLENAME_LOWER__;
  }

  public async update({ id }, data: Update__TEMPLATE_TABLENAME_CASE__Dto): Promise<__TEMPLATE_TABLENAME_CASE__RO> {
    // console.log(`__TEMPLATE_TABLENAME_CASE__ Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.__TEMPLATE_TABLENAME_LOWER__Repository.findOne({ id });
    let updated = Object.assign(toUpdate, data);
    const __TEMPLATE_TABLENAME_LOWER__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.save(updated);
    return { __TEMPLATE_TABLENAME_LOWER__ };
  }

  public async updateGQL(data: Update__TEMPLATE_TABLENAME_CASE__Input): Promise<__TEMPLATE_TABLENAME_CASE__Entity> {
    // console.log(`__TEMPLATE_TABLENAME_CASE__ Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.__TEMPLATE_TABLENAME_LOWER__Repository.findOne({ id: data.id });
    let updated = Object.assign(toUpdate, data);
    const __TEMPLATE_TABLENAME_LOWER__ = await this.__TEMPLATE_TABLENAME_LOWER__Repository.save(updated);
    return __TEMPLATE_TABLENAME_LOWER__;
  }

  public async delete({ id }): Promise<DeleteResult> {
    return await this.__TEMPLATE_TABLENAME_LOWER__Repository.delete({ id });
  }

  public async deleteGQL(data: Delete__TEMPLATE_TABLENAME_CASE__Input): Promise<DeleteResultType> {
    const delResult = this.__TEMPLATE_TABLENAME_LOWER__Repository.delete({ id: data.id });
    return {
      affected: (await delResult).affected
    }
  }

}

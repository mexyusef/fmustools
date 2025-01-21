import { Injectable } from '@nestjs/common';
import {
  __TEMPLATE_MODELNAME_CASE__Entity,
  __TEMPLATE_MODELNAME_CASE__sRO,
  __TEMPLATE_MODELNAME_CASE__RO,
  Create__TEMPLATE_MODELNAME_CASE__Dto, 
  Update__TEMPLATE_MODELNAME_CASE__Dto,
  // Create__TEMPLATE_MODELNAME_CASE__Input, 
  Delete__TEMPLATE_MODELNAME_CASE__Input, 
  Update__TEMPLATE_MODELNAME_CASE__Input, 
  // Get__TEMPLATE_MODELNAME_CASE__Args, 
  // Get__TEMPLATE_MODELNAME_CASE__sArgs,
  // DeleteResultType,
} from './__TEMPLATE_MODELNAME_LOWER__.model';


import {
  ArgsType,
  Field,
  InputType,
  Int, 
  ObjectType 
} from "@nestjs/graphql";
// import { DeleteResultType } from '../common';
@ObjectType()
export class DeleteResultType {

  @Field(type => Int)
  affected: number;

}

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
    private readonly bookRepository: Repository<__TEMPLATE_MODELNAME_CASE__Entity>
  ) {}

  public async create(data: Create__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__Entity> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Create service: receiving ${JSON.stringify(data)}.`);
    let __TEMPLATE_MODELNAME_LOWER__ = new __TEMPLATE_MODELNAME_CASE__Entity();
    __TEMPLATE_MODELNAME_LOWER__.name = data.name;
    // __TEMPLATE_MODELNAME_LOWER__.description = data.description;
    // __TEMPLATE_MODELNAME_LOWER__.status = data.status;
    const new__TEMPLATE_MODELNAME_CASE__ = await this.bookRepository.save(__TEMPLATE_MODELNAME_LOWER__);
    return new__TEMPLATE_MODELNAME_CASE__;
  }

  public async getList(): Promise<__TEMPLATE_MODELNAME_CASE__sRO> {
    const __TEMPLATE_MODELNAME_LOWER__ = await this.bookRepository.find();
    const qb = await getRepository(__TEMPLATE_MODELNAME_CASE__Entity)
      .createQueryBuilder('__TEMPLATE_MODELNAME_LOWER__')
    const bookCount = await qb.getCount();
    return { __TEMPLATE_MODELNAME_LOWER__, bookCount };
  }

  public async getListGQL(): Promise<__TEMPLATE_MODELNAME_CASE__Entity[]> {
    const __TEMPLATE_MODELNAME_LOWER__ = await this.bookRepository.find();
    // const qb = await getRepository(__TEMPLATE_MODELNAME_CASE__Entity).createQueryBuilder('__TEMPLATE_MODELNAME_LOWER__')
    // const bookCount = await qb.getCount();
    return __TEMPLATE_MODELNAME_LOWER__;
  }

  public async getDetail(where): Promise<__TEMPLATE_MODELNAME_CASE__RO> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Detail service: receiving ${JSON.stringify(where)}.`);
    const __TEMPLATE_MODELNAME_LOWER__ = await this.bookRepository.findOne(where);
    return { __TEMPLATE_MODELNAME_LOWER__ };
  }

  public async getDetailGQL(where): Promise<__TEMPLATE_MODELNAME_CASE__Entity> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Detail service: receiving ${JSON.stringify(where)}.`);
    const __TEMPLATE_MODELNAME_LOWER__ = await this.bookRepository.findOne(where);
    return __TEMPLATE_MODELNAME_LOWER__;
  }

  public async update({ id }, data: Update__TEMPLATE_MODELNAME_CASE__Dto): Promise<__TEMPLATE_MODELNAME_CASE__RO> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.bookRepository.findOne({ id });
    let updated = Object.assign(toUpdate, data);
    const __TEMPLATE_MODELNAME_LOWER__ = await this.bookRepository.save(updated);
    return { __TEMPLATE_MODELNAME_LOWER__ };
  }

  public async updateGQL(data: Update__TEMPLATE_MODELNAME_CASE__Input): Promise<__TEMPLATE_MODELNAME_CASE__Entity> {
    // console.log(`__TEMPLATE_MODELNAME_CASE__ Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.bookRepository.findOne({ id: data.id });
    let updated = Object.assign(toUpdate, data);
    const __TEMPLATE_MODELNAME_LOWER__ = await this.bookRepository.save(updated);
    return __TEMPLATE_MODELNAME_LOWER__;
  }

  public async delete({ id }): Promise<DeleteResult> {
    return await this.bookRepository.delete({ id });
  }

  public async deleteGQL(data: Delete__TEMPLATE_MODELNAME_CASE__Input): Promise<DeleteResultType> {
    const delResult = this.bookRepository.delete({ id: data.id });
    return {
      affected: (await delResult).affected
    }
  }

}


import { 
  Args, 
  Mutation,
  Query, 
  Resolver,
  ResolveField,
} from '@nestjs/graphql';

import { 
  DeleteResult 
} from 'typeorm';

import { __TEMPLATE_TABLENAME_CASE__Service } from './__TEMPLATE_TABLENAME_LOWER__.service';
import { 
  __TEMPLATE_TABLENAME_CASE__Entity, 
  // __TEMPLATE_TABLENAME_CASE__RO, 
  __TEMPLATE_TABLENAME_CASE__sRO, 
  // Create__TEMPLATE_TABLENAME_CASE__Dto,
  __TEMPLATE_TABLENAME_CASE__sROClass,
  Create__TEMPLATE_TABLENAME_CASE__Input, 
  Delete__TEMPLATE_TABLENAME_CASE__Input, 
  Update__TEMPLATE_TABLENAME_CASE__Input, 
  Get__TEMPLATE_TABLENAME_CASE__Args,
  // Get__TEMPLATE_TABLENAME_CASE__sArgs,
  // DeleteResultType 
} from './__TEMPLATE_TABLENAME_LOWER__.model';

import {
  DeleteResultType
} from '../common';

@Resolver(() => __TEMPLATE_TABLENAME_CASE__Entity)
export class __TEMPLATE_TABLENAME_CASE__Resolver {

  constructor(
    private readonly __TEMPLATE_TABLENAME_LOWER__Service: __TEMPLATE_TABLENAME_CASE__Service
  ) {}

  @Query(() => [__TEMPLATE_TABLENAME_CASE__Entity], { name: '__TEMPLATE_TABLENAME_LOWER__List', nullable: 'items' })
  public getAll(): Promise<__TEMPLATE_TABLENAME_CASE__Entity[]> {
    return this.__TEMPLATE_TABLENAME_LOWER__Service.getListGQL();
  }

  // @Query(() => __TEMPLATE_TABLENAME_CASE__sROClass, { name: '__TEMPLATE_TABLENAME_LOWER__All', nullable: 'items' })
  // @ResolveField('all', returns => __TEMPLATE_TABLENAME_CASE__sROClass)
  @Query(() => __TEMPLATE_TABLENAME_CASE__sROClass, { name: 'all' })
  public findAll(): Promise<__TEMPLATE_TABLENAME_CASE__sRO> {
    // const semua = new __TEMPLATE_TABLENAME_CASE__sROClass();
    return this.__TEMPLATE_TABLENAME_LOWER__Service.getList()
  }

  @Query(() => __TEMPLATE_TABLENAME_CASE__Entity, { name: '__TEMPLATE_TABLENAME_LOWER__Detail', nullable: true })
  public getDetail(@Args() get__TEMPLATE_TABLENAME_CASE__Args: Get__TEMPLATE_TABLENAME_CASE__Args): Promise<__TEMPLATE_TABLENAME_CASE__Entity> {
    return this.__TEMPLATE_TABLENAME_LOWER__Service.getDetailGQL(get__TEMPLATE_TABLENAME_CASE__Args);
  }

  @Mutation(() => __TEMPLATE_TABLENAME_CASE__Entity, { name: '__TEMPLATE_TABLENAME_LOWER__Create' })
  public async create(@Args('create__TEMPLATE_TABLENAME_CASE__Data') create__TEMPLATE_TABLENAME_CASE__Data: Create__TEMPLATE_TABLENAME_CASE__Input): Promise<__TEMPLATE_TABLENAME_CASE__Entity> {
    return this.__TEMPLATE_TABLENAME_LOWER__Service.create(create__TEMPLATE_TABLENAME_CASE__Data);
  }

  @Mutation(() => __TEMPLATE_TABLENAME_CASE__Entity, { name: '__TEMPLATE_TABLENAME_LOWER__Update' })
  public update(@Args('update__TEMPLATE_TABLENAME_CASE__Data') update__TEMPLATE_TABLENAME_CASE__Data: Update__TEMPLATE_TABLENAME_CASE__Input): Promise<__TEMPLATE_TABLENAME_CASE__Entity> {
    return this.__TEMPLATE_TABLENAME_LOWER__Service.updateGQL(update__TEMPLATE_TABLENAME_CASE__Data);
  }

  @Mutation(() => DeleteResultType, { name: '__TEMPLATE_TABLENAME_LOWER__Delete' })
  public delete(@Args('delete__TEMPLATE_TABLENAME_CASE__Data') delete__TEMPLATE_TABLENAME_CASE__Data: Delete__TEMPLATE_TABLENAME_CASE__Input): Promise<DeleteResultType> {
    return this.__TEMPLATE_TABLENAME_LOWER__Service.deleteGQL(delete__TEMPLATE_TABLENAME_CASE__Data);
  }

}
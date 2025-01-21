import { 
  Column,
  DeleteResult,
  Entity, 
  PrimaryGeneratedColumn, 
} from "typeorm";

import {
  ArgsType,
  Field,
  InputType,
  Int, 
  ObjectType 
} from "@nestjs/graphql";

import {
  IsArray,
  IsEmail, 
  IsNotEmpty, 
  IsOptional 
} from "class-validator";


export enum __TEMPLATE_TABLENAME_CASE__Status {
  Created = 0,
  InProgress = 1,
  Done = 2,
}

@ObjectType()
@Entity('__TEMPLATE_TABLENAME_LOWER__')
export class __TEMPLATE_TABLENAME_CASE__Entity {

  @Field(() => Int)
  @PrimaryGeneratedColumn ()
  id: number;

  @Field()
  @Column ({nullable: true, length: 100})
  name: string;
__TEMPLATE_APP_ORMENTITY_WITHOUT_ID
}

export class Create__TEMPLATE_TABLENAME_CASE__Dto {
  // readonly id: number;
  readonly name: string;
__TEMPLATE_APP_ORM_CREATEINPUT_WITHOUT_ID
}

export class Update__TEMPLATE_TABLENAME_CASE__Dto {
  // readonly id?: number;
  readonly name: string;
__TEMPLATE_APP_ORM_UPDATEINPUT_WITHOUT_ID
}

export interface __TEMPLATE_TABLENAME_CASE__RO {
  __TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__Entity;
}

export interface __TEMPLATE_TABLENAME_CASE__sRO {
  __TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__Entity[];
  __TEMPLATE_TABLENAME_LOWER__Count: number;
}

@ObjectType()
export class __TEMPLATE_TABLENAME_CASE__sROClass {
  @Field(() => [__TEMPLATE_TABLENAME_CASE__Entity])
  __TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__Entity[];

  @Field(() => Int)
  __TEMPLATE_TABLENAME_LOWER__Count: number;
}


@ObjectType()
export class __TEMPLATE_TABLENAME_CASE__ {

  @Field(() => Int)
  id: number;

  @Field()
  name: string;
__TEMPLATE_APP_GQLENTITY_WITHOUT_ID
}

@InputType()
export class Create__TEMPLATE_TABLENAME_CASE__Input {
  // __TEMPLATE_TABLENAME_LOWER__Id: string;

  @Field()
  @IsNotEmpty()
  // @IsEmail()
  name: string;
__TEMPLATE_APP_GQL_CREATEINPUT_WITHOUT_ID
}


@InputType()
export class Update__TEMPLATE_TABLENAME_CASE__Input {
  // __TEMPLATE_TABLENAME_LOWER__Id: string;

  @Field(() => Int)
  @IsNotEmpty()
  id: number;

  @Field()
  // @IsOptional()
  @IsNotEmpty()
  name: string;

__TEMPLATE_APP_GQL_UPDATEINPUT_WITHOUT_ID
}

@InputType()
export class Delete__TEMPLATE_TABLENAME_CASE__Input {
  @Field(() => Int)
  @IsNotEmpty()
  id: number;
}


@ArgsType()
export class Get__TEMPLATE_TABLENAME_CASE__Args {
  @Field()
  @IsNotEmpty()
  name: string;
// utk get detail by id, by name, by any column
__TEMPLATE_APP_GQL_DETAIL_BY_COLUMN
}

// @ArgsType()
// export class Get__TEMPLATE_TABLENAME_CASE__sArgs {
//   @Field(() => [String])
//   @IsArray()
//   name: string[];

// __TEMPLATE_APP_GQL_LIST_BY_COLUMNS
// }

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


export enum __TEMPLATE_MODELNAME_CASE__Status {
  Created = 0,
  InProgress = 1,
  Done = 2,
}

@ObjectType()
@Entity('__TEMPLATE_MODELNAME_LOWER__')
export class __TEMPLATE_MODELNAME_CASE__Entity {

  @Field(() => Int)
  @PrimaryGeneratedColumn ()
  id: number;

  @Field()
  @Column ({nullable: true, length: 100})
  name: string;

  // @Column ({nullable: true, length: 1024})
  // description: string;

  // @Column ()
  // status: __TEMPLATE_MODELNAME_CASE__Status;

}

export class Create__TEMPLATE_MODELNAME_CASE__Dto {
  // readonly id: number;
  readonly name: string;
  // readonly description: string;
  // readonly status: __TEMPLATE_MODELNAME_CASE__Status;
}

export class Update__TEMPLATE_MODELNAME_CASE__Dto {
  // readonly id?: number;
  readonly name: string;
  // readonly description?: string;
  // readonly status?: __TEMPLATE_MODELNAME_CASE__Status;
}

export interface __TEMPLATE_MODELNAME_CASE__RO {
  __TEMPLATE_MODELNAME_LOWER__: __TEMPLATE_MODELNAME_CASE__Entity;
}

export interface __TEMPLATE_MODELNAME_CASE__sRO {
  __TEMPLATE_MODELNAME_LOWER__: __TEMPLATE_MODELNAME_CASE__Entity[];
  bookCount: number;
}

@ObjectType()
export class __TEMPLATE_MODELNAME_CASE__sROClass {
  @Field(() => [__TEMPLATE_MODELNAME_CASE__Entity])
  __TEMPLATE_MODELNAME_LOWER__: __TEMPLATE_MODELNAME_CASE__Entity[];

  @Field(() => Int)
  bookCount: number;
}


@ObjectType()
export class __TEMPLATE_MODELNAME_CASE__ {

  @Field(() => Int)
  id: number;

  @Field()
  name: string;

  // @Field(() => Int)
  // age: number;

  // @Field({ nullable: true })
  // isSubscribed?: boolean;

}

@InputType()
export class Create__TEMPLATE_MODELNAME_CASE__Input {
  // bookId: string;

  @Field()
  @IsNotEmpty()
  // @IsEmail()
  name: string;

  // @Field()
  // @IsNotEmpty()
  // age: number;

  // isSubscribed?: boolean;
}


@InputType()
export class Update__TEMPLATE_MODELNAME_CASE__Input {
  // bookId: string;

  @Field(() => Int)
  @IsNotEmpty()
  id: number;

  @Field()
  // @IsOptional()
  @IsNotEmpty()
  name: string;

  // @Field({ nullable: true })
  // @IsOptional()
  // isSubscribed?: boolean;
}

@InputType()
export class Delete__TEMPLATE_MODELNAME_CASE__Input {
  @Field(() => Int)
  @IsNotEmpty()
  id: number;

  // @Field()
  // @IsNotEmpty()
  // @IsEmail()
  // email: string;

  // @Field()
  // @IsNotEmpty()
  // age: number;

  // isSubscribed?: boolean;
}


@ArgsType()
export class Get__TEMPLATE_MODELNAME_CASE__Args {
  @Field()
  @IsNotEmpty()
  name: string;

  // email: string;
  // age: number;
  // isSubscribed?: boolean;
}

@ArgsType()
export class Get__TEMPLATE_MODELNAME_CASE__sArgs {
  @Field(() => [String])
  @IsArray()
  name: string[];

  // email: string;
  // age: number;
  // isSubscribed?: boolean;
}

// @ObjectType()
// export class DeleteResultType {

//   @Field(type => Int)
//   affected: number;

// }


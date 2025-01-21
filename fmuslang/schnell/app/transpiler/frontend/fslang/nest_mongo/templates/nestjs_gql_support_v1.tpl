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

@ObjectType()
export class __TEMPLATE_MODELNAME_CASE__ {

  @Field()
  __TEMPLATE_MODELNAME_LOWER__Id: string;

  @Field()
  email: string;

  @Field(() => Int)
  age: number;

  @Field({ nullable: true })
  isSubscribed?: boolean;

}

@InputType()
export class Create__TEMPLATE_MODELNAME_CASE__Input {
  // __TEMPLATE_MODELNAME_LOWER__Id: string;

  @Field()
  @IsNotEmpty()
  @IsEmail()
  email: string;

  @Field()
  @IsNotEmpty()
  age: number;

  // isSubscribed?: boolean;
}


@InputType()
export class Update__TEMPLATE_MODELNAME_CASE__Input {
  // __TEMPLATE_MODELNAME_LOWER__Id: string;

  @Field()
  @IsNotEmpty()
  __TEMPLATE_MODELNAME_LOWER__Id: string;

  @Field()
  @IsOptional()
  @IsNotEmpty()
  age?: number;

  @Field({ nullable: true })
  @IsOptional()
  isSubscribed?: boolean;
}


@InputType()
export class Delete__TEMPLATE_MODELNAME_CASE__Input {
  @Field()
  @IsNotEmpty()
  __TEMPLATE_MODELNAME_LOWER__Id: string;

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

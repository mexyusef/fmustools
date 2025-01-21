import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { __TEMPLATE_TABLENAME_CASE__Service } from './__TEMPLATE_TABLENAME_LOWER__.service';
import { __TEMPLATE_TABLENAME_CASE__Entity } from './__TEMPLATE_TABLENAME_LOWER__.model';
import { __TEMPLATE_TABLENAME_CASE__Controller } from './__TEMPLATE_TABLENAME_LOWER__.controller';
import { __TEMPLATE_TABLENAME_CASE__Resolver } from './__TEMPLATE_TABLENAME_LOWER__.resolver';


@Module({
  imports: [
    TypeOrmModule.forFeature([
      __TEMPLATE_TABLENAME_CASE__Entity,
    ]), 
  ],
  providers: [
    __TEMPLATE_TABLENAME_CASE__Service, 
    __TEMPLATE_TABLENAME_CASE__Resolver
  ],
  controllers: [
    __TEMPLATE_TABLENAME_CASE__Controller
  ]
})

export class __TEMPLATE_TABLENAME_CASE__Module {}
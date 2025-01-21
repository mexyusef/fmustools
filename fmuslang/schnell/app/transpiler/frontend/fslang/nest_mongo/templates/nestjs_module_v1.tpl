import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { __TEMPLATE_MODELNAME_CASE__Service } from './__TEMPLATE_MODELNAME_LOWER__.service';
import { __TEMPLATE_MODELNAME_CASE__Entity } from './__TEMPLATE_MODELNAME_LOWER__.rest';
import { __TEMPLATE_MODELNAME_CASE__Controller } from './__TEMPLATE_MODELNAME_LOWER__.controller';
import { __TEMPLATE_MODELNAME_CASE__Resolver } from './__TEMPLATE_MODELNAME_LOWER__.resolver';


@Module({
  imports: [
    TypeOrmModule.forFeature([
      __TEMPLATE_MODELNAME_CASE__Entity
    ]), 
  ],
  providers: [
    __TEMPLATE_MODELNAME_CASE__Service, 
    __TEMPLATE_MODELNAME_CASE__Resolver
  ],
  controllers: [
    __TEMPLATE_MODELNAME_CASE__Controller
  ]
})

export class __TEMPLATE_MODELNAME_CASE__Module {}

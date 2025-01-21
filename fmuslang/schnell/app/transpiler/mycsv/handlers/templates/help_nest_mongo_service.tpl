import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';

import { __TEMPLATE_MODELNAME_CASE__ } from './__TEMPLATE_MODELNAME_LOWER__.model';

@Injectable()
export class __TEMPLATE_MODELNAME_CASE__Service {
  constructor(
    @InjectModel('__TEMPLATE_MODELNAME_CASE__') private readonly __TEMPLATE_MODELNAME_LOWER__Model: Model<__TEMPLATE_MODELNAME_CASE__>,
  ) {}

  async create__TEMPLATE_MODELNAME_CASE__(
__TAB2_TEMPLATE_PARAMS__
  ) {
    const new__TEMPLATE_MODELNAME_CASE__ = new this.__TEMPLATE_MODELNAME_LOWER__Model({
__TAB3_TEMPLATE_ARGS__
    });
    const result = await new__TEMPLATE_MODELNAME_CASE__.save();
    return result.id as string;
  }

  async list__TEMPLATE_MODELNAME_CASE__s() {
    const __TEMPLATE_MODELNAME_LOWER__s = await this.__TEMPLATE_MODELNAME_LOWER__Model.find().exec();
    return __TEMPLATE_MODELNAME_LOWER__s.map(__TEMPLATE_MODELNAME_LOWER__ => ({
      id: __TEMPLATE_MODELNAME_LOWER__.id,
__TAB3_TEMPLATE_DICT__
    }));
  }

  async detail__TEMPLATE_MODELNAME_CASE__(__TEMPLATE_MODELNAME_LOWER__Id: string) {
    const __TEMPLATE_MODELNAME_LOWER__ = await this.find__TEMPLATE_MODELNAME_CASE__(__TEMPLATE_MODELNAME_LOWER__Id);
    return {
      id: __TEMPLATE_MODELNAME_LOWER__.id,
__TAB3_TEMPLATE_DICT__
    };
  }

  async update__TEMPLATE_MODELNAME_CASE__(
    __TEMPLATE_MODELNAME_LOWER__Id: string,
__TAB2_TEMPLATE_PARAMS__
  ) {
    const updated__TEMPLATE_MODELNAME_CASE__ = await this.find__TEMPLATE_MODELNAME_CASE__(__TEMPLATE_MODELNAME_LOWER__Id);
__TAB2_TEMPLATE_UPDATED__
    updated__TEMPLATE_MODELNAME_CASE__.save();
  }

  async delete__TEMPLATE_MODELNAME_CASE__(__TEMPLATE_MODELNAME_LOWER__Id: string) {
    const result = await this.__TEMPLATE_MODELNAME_LOWER__Model.deleteOne({_id: __TEMPLATE_MODELNAME_LOWER__Id}).exec();
    if (result.n === 0) {
      throw new NotFoundException('Could not find __TEMPLATE_MODELNAME_LOWER__.');
    }
  }

  private async find__TEMPLATE_MODELNAME_CASE__(id: string): Promise<__TEMPLATE_MODELNAME_CASE__> {
    let __TEMPLATE_MODELNAME_LOWER__;
    try {
      __TEMPLATE_MODELNAME_LOWER__ = await this.__TEMPLATE_MODELNAME_LOWER__Model.findById(id).exec();
    } catch (error) {
      throw new NotFoundException('Could not find __TEMPLATE_MODELNAME_LOWER__.');
    }
    if (!__TEMPLATE_MODELNAME_LOWER__) {
      throw new NotFoundException('Could not find __TEMPLATE_MODELNAME_LOWER__.');
    }
    return __TEMPLATE_MODELNAME_LOWER__;
  }

}

import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

import { __TEMPLATE_MODELNAME_CASE__Module } from './__TEMPLATE_MODELNAME_LOWER__/__TEMPLATE_MODELNAME_LOWER__.module';

import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [

    __TEMPLATE_MODELNAME_CASE__Module, 
    
    MongooseModule.forRoot(
      'mongodb://usef:rahasia@localhost/tempdb?authSource=admin',
    ),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

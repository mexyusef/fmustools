import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { GraphQLModule } from '@nestjs/graphql';

import { AppController } from './app.controller';
import { AppService } from './app.service';

// import { TaskModule } from './task/task.module';
// import { TaskEntity } from './task/task.rest';
__TEMPLATE_IMPORT_MODULE_ALL_TABLES__
__TEMPLATE_IMPORT_ENTITY_ALL_TABLES__

@Module({
  imports: [
    TypeOrmModule.forRoot({
      "type": "postgres",
      "host": "gisel.ddns.net",
      "port": 9022,
      "username": "usef",
      "password": "rahasia",
      "database": "hapuslah",
      // ["src/**/**.entity{.ts,.js}"],
      "entities": [
        // TaskEntity
__TEMPLATE_ALL_ENTITIES__
      ], 
      "synchronize": true,
    }),

    GraphQLModule.forRoot({
      //autoSchemaFile: true,
			autoSchemaFile: 'schema.gql',
    }),

    // TaskModule
__TEMPLATE_ALL_MODULES__

  ],
  
  controllers: [AppController],
  providers: [AppService],
})

export class AppModule {}

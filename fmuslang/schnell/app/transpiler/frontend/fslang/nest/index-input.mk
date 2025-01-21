--% index/fmus
nest-backend,d(/mk)
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9500
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
  package.json,f(e=utama=/nestjs/package.json)
  .gitignore,f(e=utama=/nestjs/.gitignore)
  tsconfig.json,f(e=utama=/nestjs/tsconfig.json)
  .eslintrc.js,f(e=utama=/nestjs/.eslintrc.js)
  README.md,f(e=utama=/nestjs/README.md)
  # schema.gql,f(e=utama=/nestjs/schema.gql)
  tsconfig.build.json,f(e=utama=/nestjs/tsconfig.build.json)
  .prettierrc,f(e=utama=/nestjs/.prettierrc)
  nest-cli.json,f(e=utama=/nestjs/nest-cli.json)
  src,d(/mk)
    app.service.ts,f(e=utama=/nestjs/src/app.service.ts)
    app.controller.ts,f(e=utama=/nestjs/src/app.controller.ts)
    app.controller.spec.ts,f(e=utama=/nestjs/src/app.controller.spec.ts)
    app.module.ts,f(e=utama=/nestjs/src/app.module.ts)
    main.ts,f(e=utama=/nestjs/src/main.ts)
    common.ts,f(e=utama=/nestjs/src/common.ts)
    attendee,d(/mk)
      attendee.module.ts,f(e=utama=/nestjs/src/attendee/attendee.module.ts)
      attendee.resolver.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.spec.ts)
      attendee.controller.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.ts)
      attendee.service.ts,f(e=utama=/nestjs/src/attendee/attendee.service.ts)
      attendee.resolver.ts,f(e=utama=/nestjs/src/attendee/attendee.resolver.ts)
      attendee.model.ts,f(e=utama=/nestjs/src/attendee/attendee.model.ts)
      attendee.service.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.service.spec.ts)
      attendee.controller.spec.ts,f(e=utama=/nestjs/src/attendee/attendee.controller.spec.ts)
__TEMPLATE_SERVER_APP_CONTENT
  test,d(/mk)
    jest-e2e.json,f(e=utama=/nestjs/test/jest-e2e.json)
    app.e2e-spec.ts,f(e=utama=/nestjs/test/app.e2e-spec.ts)

  #$*qterminal 2>/dev/null &
--#

--% /nestjs/package.json
{
  "name": "mynest1",
  "version": "0.0.1",
  "description": "",
  "author": "",
  "private": true,
  "license": "UNLICENSED",
  "scripts": {
    "prebuild": "rimraf dist",
    "build": "nest build",
    "format": "prettier --write \"src/**/*.ts\" \"test/**/*.ts\"",
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:debug": "nest start --debug --watch",
    "start:prod": "node dist/main",
    "lint": "eslint \"{src,apps,libs,test}/**/*.ts\" --fix",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:cov": "jest --coverage",
    "test:debug": "node --inspect-brk -r tsconfig-paths/register -r ts-node/register node_modules/.bin/jest --runInBand",
    "test:e2e": "jest --config ./test/jest-e2e.json"
  },
  "dependencies": {
    "@nestjs/common": "^7.6.15",
    "@nestjs/core": "^7.6.15",
    "@nestjs/graphql": "^7.11.0",
    "@nestjs/mongoose": "^7.2.4",
    "@nestjs/platform-express": "^7.6.15",
    "@nestjs/typeorm": "^7.1.5",
    "apollo-server-express": "^2.25.2",
    "class-validator": "^0.13.1",
    "graphql": "^15.5.1",
    "graphql-tools": "^7.0.5",
    "mongoose": "^5.12.13",
    "pg": "^8.6.0",
    "reflect-metadata": "^0.1.13",
    "rimraf": "^3.0.2",
    "rxjs": "^6.6.6",
    "type-graphql": "^1.1.1",
    "typeorm": "^0.2.34"
  },
  "devDependencies": {
    "@nestjs/cli": "^7.6.0",
    "@nestjs/schematics": "^7.3.0",
    "@nestjs/testing": "^7.6.15",
    "@types/express": "^4.17.11",
    "@types/jest": "^26.0.22",
    "@types/node": "^14.14.36",
    "@types/supertest": "^2.0.10",
    "@typescript-eslint/eslint-plugin": "^4.19.0",
    "@typescript-eslint/parser": "^4.19.0",
    "eslint": "^7.22.0",
    "eslint-config-prettier": "^8.1.0",
    "eslint-plugin-prettier": "^3.3.1",
    "jest": "^26.6.3",
    "prettier": "^2.2.1",
    "supertest": "^6.1.3",
    "ts-jest": "^26.5.4",
    "ts-loader": "^8.0.18",
    "ts-node": "^9.1.1",
    "tsconfig-paths": "^3.9.0",
    "typescript": "^4.2.3"
  },
  "jest": {
    "moduleFileExtensions": [
      "js",
      "json",
      "ts"
    ],
    "rootDir": "src",
    "testRegex": ".*\\.spec\\.ts$",
    "transform": {
      "^.+\\.(t|j)s$": "ts-jest"
    },
    "collectCoverageFrom": [
      "**/*.(t|j)s"
    ],
    "coverageDirectory": "../coverage",
    "testEnvironment": "node"
  }
}

--#

--% /nestjs/.gitignore
# compiled output
/dist
/node_modules

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# OS
.DS_Store

# Tests
/coverage
/.nyc_output

# IDEs and editors
/.idea
.project
.classpath
.c9/
*.launch
.settings/
*.sublime-workspace

# IDE - VSCode
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
--#

--% /nestjs/tsconfig.json
{
  "compilerOptions": {
    "module": "commonjs",
    "declaration": true,
    "removeComments": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "allowSyntheticDefaultImports": true,
    "target": "es2017",
    "sourceMap": true,
    "outDir": "./dist",
    "baseUrl": "./",
    "incremental": true
  }
}

--#

--% /nestjs/.eslintrc.js
module.exports = {
  parser: '@typescript-eslint/parser',
  parserOptions: {
    project: 'tsconfig.json',
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint/eslint-plugin'],
  extends: [
    'plugin:@typescript-eslint/recommended',
    'plugin:prettier/recommended',
  ],
  root: true,
  env: {
    node: true,
    jest: true,
  },
  ignorePatterns: ['.eslintrc.js'],
  rules: {
    '@typescript-eslint/interface-name-prefix': 'off',
    '@typescript-eslint/explicit-function-return-type': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-explicit-any': 'off',
  },
};

--#

--% /nestjs/README.md
{
  all {
    attendee {
      id
      name
    }
    attendeeCount
  }
}

mutation {
  create (
    createAttendeeData: {
      name: "monyong kuda hapuslah"
    }
  ) {
    name
  }
}

mutation {
  delete(deleteAttendeeData: {id:6}){
    affected
  }
}

--#

--% /nestjs/schema.gql
# ------------------------------------------------------
# THIS FILE WAS AUTOMATICALLY GENERATED (DO NOT MODIFY)
# ------------------------------------------------------

type AttendeeEntity {
  id: Int!
  name: String!
}

type AttendeesROClass {
  attendee: [AttendeeEntity!]!
  attendeeCount: Int!
}

type DeleteResultType {
  affected: Int!
}

type Query {
  attendees: [AttendeeEntity]!
  all: AttendeesROClass!
  attendee(name: String!): AttendeeEntity
}

type Mutation {
  create(createAttendeeData: CreateAttendeeInput!): AttendeeEntity!
  update(updateAttendeeData: UpdateAttendeeInput!): AttendeeEntity!
  delete(deleteAttendeeData: DeleteAttendeeInput!): DeleteResultType!
}

input CreateAttendeeInput {
  name: String!
}

input UpdateAttendeeInput {
  id: Int!
  name: String!
}

input DeleteAttendeeInput {
  id: Int!
}

--#

--% /nestjs/tsconfig.build.json
{
  "extends": "./tsconfig.json",
  "exclude": ["node_modules", "test", "dist", "**/*spec.ts"]
}

--#

--% /nestjs/.prettierrc
{
  "singleQuote": true,
  "trailingComma": "all"
}
--#

--% /nestjs/nest-cli.json
{
  "collection": "@nestjs/schematics",
  "sourceRoot": "src"
}

--#

--% /nestjs/src/app.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return "OMG it's Alive!";
  }
}

--#

--% /nestjs/src/app.controller.ts
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}

--#

--% /nestjs/src/app.controller.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [AppService],
    }).compile();

    appController = app.get<AppController>(AppController);
  });

  describe('root', () => {
    it('should return "Hello World!"', () => {
      expect(appController.getHello()).toBe('Hello World!');
    });
  });
});

--#

--% /nestjs/src/app.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { GraphQLModule } from '@nestjs/graphql';

import { AppController } from './app.controller';
import { AppService } from './app.service';

// import { TaskModule } from './task/task.module';
// import { TaskEntity } from './task/task.entity';
import { AttendeeModule } from './attendee/attendee.module';
import { AttendeeEntity } from './attendee/attendee.model';
__TEMPLATE_ROOTAPP_IMPORTS__

@Module({
  imports: [
    TypeOrmModule.forRoot({
      "type": "postgres",
      "host": "__TEMPLATE_DBHOST",
      "port": __TEMPLATE_DBPORT,
      "username": "__TEMPLATE_DBUSER",
      "password": "__TEMPLATE_DBPASS",
      "database": "__TEMPLATE_DBNAME",
      // ["src/**/**.entity{.ts,.js}"],
      "entities": [
        // TaskEntity
        AttendeeEntity__TEMPLATE_ROOTAPP_ENTITYPARAMS__
      ], 
      "synchronize": true,
    }),

    GraphQLModule.forRoot({
      //autoSchemaFile: true,
      autoSchemaFile: 'schema.gql',
    }),

    AttendeeModule__TEMPLATE_ROOTAPP_MODULEPARAMS__
  ],
  
  controllers: [AppController],
  providers: [AppService],
})

export class AppModule {}

--#

--% /nestjs/src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(__TEMPLATE_SERVER_PORT__);
}
bootstrap();

--#

--% /nestjs/src/common.ts
import {
  ArgsType,
  Field,
  InputType,
  Int, 
  ObjectType 
} from "@nestjs/graphql";

@ObjectType()
export class DeleteResultType {

  @Field(type => Int)
  affected: number;

}
--#

--% /nestjs/src/attendee/attendee.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AttendeeService } from './attendee.service';
import { AttendeeEntity } from './attendee.model';
import { AttendeeController } from './attendee.controller';
import { AttendeeResolver } from './attendee.resolver';


@Module({
  imports: [
    TypeOrmModule.forFeature([
      AttendeeEntity,
    ]), 
  ],
  providers: [
    AttendeeService, 
    AttendeeResolver
  ],
  controllers: [
    AttendeeController
  ]
})

export class AttendeeModule {}

--#

--% /nestjs/src/attendee/attendee.resolver.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { AttendeeResolver } from './attendee.resolver';

describe('AttendeeResolver', () => {
  let resolver: AttendeeResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [AttendeeResolver],
    }).compile();

    resolver = module.get<AttendeeResolver>(AttendeeResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});

--#

--% /nestjs/src/attendee/attendee.controller.ts
import { 
  Body, 
  Controller, 
  Delete, 
  Get, 
  Param, 
  Post, 
  Put 
} from '@nestjs/common';

import { 
  DeleteResult
} from 'typeorm';

import { 
  AttendeeEntity, 
  AttendeeRO, 
  AttendeesRO, 
  CreateAttendeeDto, 
  UpdateAttendeeDto
} from './attendee.model';

import { AttendeeService } from './attendee.service';

@Controller('attendee')
export class AttendeeController {

  constructor(private readonly attendeeService: AttendeeService) {}

  // *~localhost:__TEMPLATE_SERVER_PORT__/attendee
  @Get()
  public async getList(): Promise<AttendeesRO> {
    return this.attendeeService.getList();
  }

  // *~localhost:__TEMPLATE_SERVER_PORT__/attendee/6
  @Get('/:id')
  public async getDetail(@Param('id') id: number): Promise<AttendeeRO> {
    // console.log(`Attendee Detail controller: receiving ${id}.`);
    return this.attendeeService.getDetail({id});
  }

  // *~localhost:__TEMPLATE_SERVER_PORT__/attendee p json {title=Attendee no 5,description=semoga masuk ya, status=0}
  @Post()
  public async create(@Body() data: CreateAttendeeDto): Promise<AttendeeEntity> {    
    // console.log(`Attendee Create controller: receiving ${JSON.stringify(data)}.`);
    return this.attendeeService.create(data);
  }

  // *~localhost:__TEMPLATE_SERVER_PORT__/attendee/6 u json {title=Empat jadi Tidak sempat}
  @Put('/:id')
  public async update(@Param('id') id: number, @Body() data: UpdateAttendeeDto): Promise<AttendeeRO> {    
    // console.log(`Attendee Update controller: receiving ${id} = ${JSON.stringify(data)}.`);
    return this.attendeeService.update({id}, data);
  }

  // *~localhost:__TEMPLATE_SERVER_PORT__/attendee/3 d
  @Delete('/:id')
  public async delete(@Param('id') id: number): Promise<DeleteResult> {
    return this.attendeeService.delete({id});
  }

}

--#

--% /nestjs/src/attendee/attendee.service.ts
import { Injectable } from '@nestjs/common';
import {
  AttendeeEntity,
  AttendeesRO,
  AttendeeRO,
  CreateAttendeeDto, 
  UpdateAttendeeDto,
  // CreateAttendeeInput, 
  DeleteAttendeeInput, 
  UpdateAttendeeInput, 
  // GetAttendeeArgs, 
  // GetAttendeesArgs,
  // DeleteResultType,
} from './attendee.model';

import {
  DeleteResultType
} from '../common';

import { 
  DeleteResult,
  Repository,
  getRepository,
} from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';


@Injectable()
export class AttendeeService {

  constructor(
    @InjectRepository(AttendeeEntity)
    private readonly attendeeRepository: Repository<AttendeeEntity>
  ) {}

  public async create(data: CreateAttendeeDto): Promise<AttendeeEntity> {
    // console.log(`Attendee Create service: receiving ${JSON.stringify(data)}.`);
    let attendee = new AttendeeEntity();
    attendee.name = data.name;
    // attendee.description = data.description;
    // attendee.status = data.status;
    const newAttendee = await this.attendeeRepository.save(attendee);
    return newAttendee;
  }

  public async getList(): Promise<AttendeesRO> {
    const attendee = await this.attendeeRepository.find();
    const qb = await getRepository(AttendeeEntity)
      .createQueryBuilder('attendee')
    const attendeeCount = await qb.getCount();
    return { attendee, attendeeCount };
  }

  public async getListGQL(): Promise<AttendeeEntity[]> {
    const attendee = await this.attendeeRepository.find();
    // const qb = await getRepository(AttendeeEntity).createQueryBuilder('attendee')
    // const attendeeCount = await qb.getCount();
    return attendee;
  }

  public async getDetail(where): Promise<AttendeeRO> {
    // console.log(`Attendee Detail service: receiving ${JSON.stringify(where)}.`);
    const attendee = await this.attendeeRepository.findOne(where);
    return { attendee };
  }

  public async getDetailGQL(where): Promise<AttendeeEntity> {
    // console.log(`Attendee Detail service: receiving ${JSON.stringify(where)}.`);
    const attendee = await this.attendeeRepository.findOne(where);
    return attendee;
  }

  public async update({ id }, data: UpdateAttendeeDto): Promise<AttendeeRO> {
    // console.log(`Attendee Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.attendeeRepository.findOne({ id });
    let updated = Object.assign(toUpdate, data);
    const attendee = await this.attendeeRepository.save(updated);
    return { attendee };
  }

  public async updateGQL(data: UpdateAttendeeInput): Promise<AttendeeEntity> {
    // console.log(`Attendee Update service: receiving id: ${id} dan data: ${JSON.stringify(data)}.`);
    let toUpdate = await this.attendeeRepository.findOne({ id: data.id });
    let updated = Object.assign(toUpdate, data);
    const attendee = await this.attendeeRepository.save(updated);
    return attendee;
  }

  public async delete({ id }): Promise<DeleteResult> {
    return await this.attendeeRepository.delete({ id });
  }

  public async deleteGQL(data: DeleteAttendeeInput): Promise<DeleteResultType> {
    const delResult = this.attendeeRepository.delete({ id: data.id });
    return {
      affected: (await delResult).affected
    }
  }

}

--#

--% /nestjs/src/attendee/attendee.resolver.ts
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

import { AttendeeService } from './attendee.service';
import { 
  AttendeeEntity, 
  // AttendeeRO, 
  AttendeesRO, 
  // CreateAttendeeDto,
  AttendeesROClass,
  CreateAttendeeInput, 
  DeleteAttendeeInput, 
  UpdateAttendeeInput, 
  GetAttendeeArgs,
  // GetAttendeesArgs,
  // DeleteResultType 
} from './attendee.model';

import {
  DeleteResultType
} from '../common';

@Resolver(() => AttendeeEntity)
export class AttendeeResolver {

  constructor(
    private readonly attendeeService: AttendeeService
  ) {}

  @Query(() => [AttendeeEntity], { name: 'attendees', nullable: 'items' })
  public getAll(): Promise<AttendeeEntity[]> {
    return this.attendeeService.getListGQL();
  }

  // @Query(() => AttendeesROClass, { name: 'all', nullable: 'items' })
  // @ResolveField('all', returns => AttendeesROClass)
  @Query(() => AttendeesROClass, { name: 'all' })
  public findAll(): Promise<AttendeesRO> {
    // const semua = new AttendeesROClass();
    return this.attendeeService.getList()
  }

  @Query(() => AttendeeEntity, { name: 'attendee', nullable: true })
  public getDetail(@Args() getAttendeeArgs: GetAttendeeArgs): Promise<AttendeeEntity> {
    return this.attendeeService.getDetailGQL(getAttendeeArgs);
  }

  @Mutation(() => AttendeeEntity)
  public async create(@Args('createAttendeeData') createAttendeeData: CreateAttendeeInput): Promise<AttendeeEntity> {
    return this.attendeeService.create(createAttendeeData);
  }

  @Mutation(() => AttendeeEntity)
  public update(@Args('updateAttendeeData') updateAttendeeData: UpdateAttendeeInput): Promise<AttendeeEntity> {
    return this.attendeeService.updateGQL(updateAttendeeData);
  }

  @Mutation(() => DeleteResultType)
  public delete(@Args('deleteAttendeeData') deleteAttendeeData: DeleteAttendeeInput): Promise<DeleteResultType> {
    return this.attendeeService.deleteGQL(deleteAttendeeData);
  }

}

--#

--% /nestjs/src/attendee/attendee.model.ts
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


export enum AttendeeStatus {
  Created = 0,
  InProgress = 1,
  Done = 2,
}

@ObjectType()
@Entity('attendee')
export class AttendeeEntity {

  @Field(() => Int)
  @PrimaryGeneratedColumn ()
  id: number;

  @Field()
  @Column ({nullable: true, length: 100})
  name: string;

  // @Column ({nullable: true, length: 1024})
  // description: string;

  // @Column ()
  // status: AttendeeStatus;

}

export class CreateAttendeeDto {
  // readonly id: number;
  readonly name: string;
  // readonly description: string;
  // readonly status: AttendeeStatus;
}

export class UpdateAttendeeDto {
  // readonly id?: number;
  readonly name: string;
  // readonly description?: string;
  // readonly status?: AttendeeStatus;
}

export interface AttendeeRO {
  attendee: AttendeeEntity;
}

export interface AttendeesRO {
  attendee: AttendeeEntity[];
  attendeeCount: number;
}

@ObjectType()
export class AttendeesROClass {
  @Field(() => [AttendeeEntity])
  attendee: AttendeeEntity[];

  @Field(() => Int)
  attendeeCount: number;
}


@ObjectType()
export class Attendee {

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
export class CreateAttendeeInput {
  // attendeeId: string;

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
export class UpdateAttendeeInput {
  // attendeeId: string;

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
export class DeleteAttendeeInput {
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
export class GetAttendeeArgs {
  @Field()
  @IsNotEmpty()
  name: string;

  // email: string;
  // age: number;
  // isSubscribed?: boolean;
}

@ArgsType()
export class GetAttendeesArgs {
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

--#

--% /nestjs/src/attendee/attendee.service.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { AttendeeService } from './attendee.service';

describe('AttendeeService', () => {
  let service: AttendeeService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [AttendeeService],
    }).compile();

    service = module.get<AttendeeService>(AttendeeService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});

--#

--% /nestjs/src/attendee/attendee.controller.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { AttendeeController } from './attendee.controller';

describe('AttendeeController', () => {
  let controller: AttendeeController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [AttendeeController],
    }).compile();

    controller = module.get<AttendeeController>(AttendeeController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});

--#

--% /nestjs/test/jest-e2e.json
{
  "moduleFileExtensions": ["js", "json", "ts"],
  "rootDir": ".",
  "testEnvironment": "node",
  "testRegex": ".e2e-spec.ts$",
  "transform": {
    "^.+\\.(t|j)s$": "ts-jest"
  }
}

--#

--% /nestjs/test/app.e2e-spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { INestApplication } from '@nestjs/common';
import * as request from 'supertest';
import { AppModule } from './../src/app.module';

describe('AppController (e2e)', () => {
  let app: INestApplication;

  beforeEach(async () => {
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleFixture.createNestApplication();
    await app.init();
  });

  it('/ (GET)', () => {
    return request(app.getHttpServer())
      .get('/')
      .expect(200)
      .expect('Hello World!');
  });
});

--#


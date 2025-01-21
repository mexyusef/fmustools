--% index/fmus
nest-mongo,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/.gitignore)
	.prettierrc,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/.prettierrc)
	docker-compose.yml,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/docker-compose.yml)
	nest-cli.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/nest-cli.json)
	nodemon-debug.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/nodemon-debug.json)
	nodemon.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/nodemon.json)
	package.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/package.json)
	README.md,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/README.md)
	run.sh,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/run.sh)
	tsconfig.build.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/tsconfig.build.json)
	tsconfig.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/tsconfig.json)
	tslint.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/tslint.json)
	.vscode,d(/mk)
		settings.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/.vscode/settings.json)
	src,d(/mk)
		app.controller.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/app.controller.ts)
		app.module.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/app.module.ts)
		app.service.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/app.service.ts)
		main.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/main.ts)
		products,d(/mk)
			product.model.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/product.model.ts)
			products.controller.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/products.controller.ts)
			products.module.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/products.module.ts)
			products.service.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/products.service.ts)
		users,d(/mk)
			users.controller.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.controller.ts)
			users.module.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.module.ts)
			users.repository.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.repository.ts)
			users.service.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.service.ts)
			dto,d(/mk)
				create-user.dto.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/dto/create-user.dto.ts)
				update-user.dto.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/dto/update-user.dto.ts)
			schemas,d(/mk)
				user.schema.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/schemas/user.schema.ts)
	test,d(/mk)
		app.e2e-spec.ts,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/test/app.e2e-spec.ts)
		jest-e2e.json,f(e=utama=C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/test/jest-e2e.json)
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/.gitignore
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

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/.prettierrc
{
  "singleQuote": true,
  "trailingComma": "all"
}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/docker-compose.yml
version: '3'
services:
  database:
    image: 'mongo'
    # container_name: 'mymongocontainer'
    environment:
      - MONGO_INITDB_DATABASE=tempdb
      - MONGO_INITDB_ROOT_USERNAME=usef
      - MONGO_INITDB_ROOT_PASSWORD=rahasia
    ports:
      - '27017-27019:27017-27019'

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/nest-cli.json
{
  "language": "ts",
  "collection": "@nestjs/schematics",
  "sourceRoot": "src"
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/nodemon-debug.json
{
  "watch": ["src"],
  "ext": "ts",
  "ignore": ["src/**/*.spec.ts"],
  "exec": "node --inspect-brk -r ts-node/register -r tsconfig-paths/register src/main.ts"
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/nodemon.json
{
  "watch": ["dist"],
  "ext": "js",
  "exec": "node dist/main"
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/package.json
{
  "name": "nestjs-intro",
  "version": "0.0.1",
  "description": "",
  "author": "",
  "license": "MIT",
  "scripts": {
    "build": "tsc -p tsconfig.build.json",
    "format": "prettier --write \"src/**/*.ts\"",
    "start": "ts-node -r tsconfig-paths/register src/main.ts",
    "start:dev": "concurrently --handle-input \"wait-on dist/main.js && nodemon\" \"tsc -w -p tsconfig.build.json\" ",
    "start:debug": "nodemon --config nodemon-debug.json",
    "prestart:prod": "rimraf dist && npm run build",
    "start:prod": "node dist/main.js",
    "lint": "tslint -p tsconfig.json -c tslint.json",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:cov": "jest --coverage",
    "test:debug": "node --inspect-brk -r tsconfig-paths/register -r ts-node/register node_modules/.bin/jest --runInBand",
    "test:e2e": "jest --config ./test/jest-e2e.json"
  },
  "dependencies": {
    "@nestjs/common": "^7.0.0",
    "@nestjs/core": "^7.0.0",
    "@nestjs/mongoose": "^7.2.3",
    "@nestjs/platform-express": "^7.0.0",
    "@types/mongoose": "^5.11.97",
    "mongoose": "^5.11.17",
    "reflect-metadata": "^0.1.13",
    "rimraf": "^3.0.2",
    "rxjs": "^6.5.4"
  },
  "devDependencies": {
    "@nestjs/testing": "^7.0.0",
    "@types/express": "^4.17.3",
    "@types/jest": "25.2.3",
    "@types/node": "^13.9.1",
    "@types/supertest": "^2.0.8",
    "concurrently": "^4.1.0",
    "jest": "26.0.1",
    "nodemon": "^1.18.9",
    "prettier": "^1.19.1",
    "supertest": "^4.0.2",
    "ts-jest": "26.1.0",
    "ts-node": "^8.6.2",
    "tsconfig-paths": "^3.9.0",
    "tslint": "5.16.0",
    "typescript": "^3.7.4",
    "wait-on": "^3.2.0"
  },
  "jest": {
    "moduleFileExtensions": [
      "js",
      "json",
      "ts"
    ],
    "rootDir": "src",
    "testRegex": ".spec.ts$",
    "transform": {
      "^.+\\.(t|j)s$": "ts-jest"
    },
    "coverageDirectory": "../coverage",
    "testEnvironment": "node"
  }
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/README.md
<p align="center">
  <a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo_text.svg" width="320" alt="Nest Logo" /></a>
</p>

[travis-image]: https://api.travis-ci.org/nestjs/nest.svg?branch=master
[travis-url]: https://travis-ci.org/nestjs/nest
[linux-image]: https://img.shields.io/travis/nestjs/nest/master.svg?label=linux
[linux-url]: https://travis-ci.org/nestjs/nest
  
  <p align="center">A progressive <a href="http://nodejs.org" target="blank">Node.js</a> framework for building efficient and scalable server-side applications, heavily inspired by <a href="https://angular.io" target="blank">Angular</a>.</p>
    <p align="center">
<a href="https://www.npmjs.com/~nestjscore"><img src="https://img.shields.io/npm/v/@nestjs/core.svg" alt="NPM Version" /></a>
<a href="https://www.npmjs.com/~nestjscore"><img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" /></a>
<a href="https://www.npmjs.com/~nestjscore"><img src="https://img.shields.io/npm/dm/@nestjs/core.svg" alt="NPM Downloads" /></a>
<a href="https://travis-ci.org/nestjs/nest"><img src="https://api.travis-ci.org/nestjs/nest.svg?branch=master" alt="Travis" /></a>
<a href="https://travis-ci.org/nestjs/nest"><img src="https://img.shields.io/travis/nestjs/nest/master.svg?label=linux" alt="Linux" /></a>
<a href="https://coveralls.io/github/nestjs/nest?branch=master"><img src="https://coveralls.io/repos/github/nestjs/nest/badge.svg?branch=master#5" alt="Coverage" /></a>
<a href="https://gitter.im/nestjs/nestjs?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=body_badge"><img src="https://badges.gitter.im/nestjs/nestjs.svg" alt="Gitter" /></a>
<a href="https://opencollective.com/nest#backer"><img src="https://opencollective.com/nest/backers/badge.svg" alt="Backers on Open Collective" /></a>
<a href="https://opencollective.com/nest#sponsor"><img src="https://opencollective.com/nest/sponsors/badge.svg" alt="Sponsors on Open Collective" /></a>
  <a href="https://paypal.me/kamilmysliwiec"><img src="https://img.shields.io/badge/Donate-PayPal-dc3d53.svg"/></a>
  <a href="https://twitter.com/nestframework"><img src="https://img.shields.io/twitter/follow/nestframework.svg?style=social&label=Follow"></a>
</p>
  <!--[![Backers on Open Collective](https://opencollective.com/nest/backers/badge.svg)](https://opencollective.com/nest#backer)
  [![Sponsors on Open Collective](https://opencollective.com/nest/sponsors/badge.svg)](https://opencollective.com/nest#sponsor)-->

## Description

[Nest](https://github.com/nestjs/nest) framework TypeScript starter repository.

## Installation

```bash
$ npm install
```

## Running the app

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

## Test

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```

## Support

Nest is an MIT-licensed open source project. It can grow thanks to the sponsors and support by the amazing backers. If you'd like to join them, please [read more here](https://docs.nestjs.com/support).

## Stay in touch

- Author - [Kamil Myśliwiec](https://kamilmysliwiec.com)
- Website - [https://nestjs.com](https://nestjs.com/)
- Twitter - [@nestframework](https://twitter.com/nestframework)

http://localhost:3000/users
http://localhost:3000/products

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/run.sh
yarn start

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/tsconfig.build.json
{
  "extends": "./tsconfig.json",
  "exclude": ["node_modules", "test", "dist", "**/*spec.ts"]
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/tsconfig.json
{
  "compilerOptions": {
    "module": "commonjs",
    "declaration": true,
    "removeComments": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "target": "es6",
    "sourceMap": true,
    "outDir": "./dist",
    "baseUrl": "./",
    "incremental": true
  },
  "exclude": ["node_modules"]
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/tslint.json
{
  "defaultSeverity": "error",
  "extends": ["tslint:recommended"],
  "jsRules": {
    "no-unused-expression": true
  },
  "rules": {
    "quotemark": [true, "single"],
    "member-access": [false],
    "ordered-imports": [false],
    "max-line-length": [true, 150],
    "member-ordering": [false],
    "interface-name": [false],
    "arrow-parens": false,
    "object-literal-sort-keys": false
  },
  "rulesDirectory": []
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/.vscode/settings.json
{
    "window.zoomLevel": 6
}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/app.controller.ts
import { Controller, Get, Header } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  @Header('Content-Type', 'text/html')
  getHello(): {name: string} {
    return {name: 'Max'};
  }
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/app.module.ts
import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';

import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ProductsModule } from './products/products.module';
import { UsersModule } from './users/users.module';

@Module({
  imports: [
    ProductsModule,
    UsersModule,
    MongooseModule.forRoot(
      // 'mongodb+srv://maximilian:B3dqPzooRLzFiVYm@cluster0-ntrwp.mongodb.net/nestjs-demo?retryWrites=true&w=majority',
      'mongodb://usef:rahasia@localhost/?authSource=admin',
    ),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/app.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/product.model.ts
import * as mongoose from 'mongoose';

export const ProductSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  price: { type: Number, required: true },
});

export interface Product extends mongoose.Document {
  id: string;
  title: string;
  description: string;
  price: number;
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/products.controller.ts
import {
  Controller,
  Post,
  Body,
  Get,
  Param,
  Patch,
  Delete,
} from '@nestjs/common';

import { ProductsService } from './products.service';

@Controller('products')
export class ProductsController {
  constructor(private readonly productsService: ProductsService) {}

  @Post()
  async addProduct(
    @Body('title') prodTitle: string,
    @Body('description') prodDesc: string,
    @Body('price') prodPrice: number,
  ) {
    const generatedId = await this.productsService.insertProduct(
      prodTitle,
      prodDesc,
      prodPrice,
    );
    return { id: generatedId };
  }

  @Get()
  async getAllProducts() {
    const products = await this.productsService.getProducts();
    return products;
  }

  @Get(':id')
  getProduct(@Param('id') prodId: string) {
    return this.productsService.getSingleProduct(prodId);
  }

  @Patch(':id')
  async updateProduct(
    @Param('id') prodId: string,

    @Body('title') prodTitle: string,
    @Body('description') prodDesc: string,
    @Body('price') prodPrice: number,
  ) {
    await this.productsService.updateProduct(
      prodId, prodTitle, prodDesc, prodPrice
    );
    return null;
  }

  @Delete(':id')
  async removeProduct(@Param('id') prodId: string) {
      await this.productsService.deleteProduct(prodId);
      return null;
  }
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/products.module.ts
import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';

import { ProductsController } from './products.controller';
import { ProductsService } from './products.service';
import { ProductSchema } from './product.model';

@Module({
  imports: [
    MongooseModule.forFeature([{ name: 'Product', schema: ProductSchema }]),
  ],
  controllers: [ProductsController],
  providers: [ProductsService],
})
export class ProductsModule {}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/products/products.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';

import { Product } from './product.model';

@Injectable()
export class ProductsService {
  constructor(
    @InjectModel('Product') private readonly productModel: Model<Product>,
  ) {}

  async insertProduct(title: string, desc: string, price: number) {
    const newProduct = new this.productModel({
      title,
      description: desc,
      price,
    });
    const result = await newProduct.save();
    return result.id as string;
  }

  async getProducts() {
    const products = await this.productModel.find().exec();
    return products.map(prod => ({
      id: prod.id,
      title: prod.title,
      description: prod.description,
      price: prod.price,
    }));
  }

  async getSingleProduct(productId: string) {
    const product = await this.findProduct(productId);
    return {
      id: product.id,
      title: product.title,
      description: product.description,
      price: product.price,
    };
  }

  async updateProduct(
    productId: string,
    title: string,
    desc: string,
    price: number,
  ) {
    const updatedProduct = await this.findProduct(productId);
    if (title) {
      updatedProduct.title = title;
    }
    if (desc) {
      updatedProduct.description = desc;
    }
    if (price) {
      updatedProduct.price = price;
    }
    updatedProduct.save();
  }

  async deleteProduct(prodId: string) {
    const result = await this.productModel.deleteOne({_id: prodId}).exec();
    if (result.n === 0) {
      throw new NotFoundException('Could not find product.');
    }
  }

  private async findProduct(id: string): Promise<Product> {
    let product;
    try {
      product = await this.productModel.findById(id).exec();
    } catch (error) {
      throw new NotFoundException('Could not find product.');
    }
    if (!product) {
      throw new NotFoundException('Could not find product.');
    }
    return product;
  }
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.controller.ts
import { Body, Controller, Get, Param, Patch, Post } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';

import { User } from './schemas/user.schema';
import { UsersService } from './users.service';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get(':userId')
  async getUser(@Param('userId') userId: string): Promise<User> {
    return this.usersService.getUserById(userId);
  }

  @Get()
  async getUsers(): Promise<User[]> {
      return this.usersService.getUsers();
  }

  @Post()
  async createUser(@Body() createUserDto: CreateUserDto): Promise<User> {
      return this.usersService.createUser(createUserDto.email, createUserDto.age)
  }

  @Patch(':userId')
  async updateUser(@Param('userId') userId: string, @Body() updateUserDto: UpdateUserDto): Promise<User> {
      return this.usersService.updateUser(userId, updateUserDto);
  }
}

--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.module.ts
import { Module } from "@nestjs/common";
import { MongooseModule } from "@nestjs/mongoose";
import { User, UserSchema } from "./schemas/user.schema";
import { UsersController } from "./users.controller";
import { UsersRepository } from "./users.repository";
import { UsersService } from "./users.service";

@Module({
    imports: [MongooseModule.forFeature([{ name: User.name, schema: UserSchema }])],
    controllers: [UsersController],
    providers: [UsersService, UsersRepository]
})
export class UsersModule {}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.repository.ts
import { Injectable } from "@nestjs/common";
import { InjectModel } from "@nestjs/mongoose";
import { FilterQuery, Model } from "mongoose";

import { User, UserDocument } from "./schemas/user.schema";

@Injectable()
export class UsersRepository {
    constructor(@InjectModel(User.name) private userModel: Model<UserDocument>) {}

    async findOne(userFilterQuery: FilterQuery<UserDocument>): Promise<User> {
        return this.userModel.findOne(userFilterQuery);
    }

    async find(usersFilterQuery: FilterQuery<UserDocument>): Promise<User[]> {
        return this.userModel.find(usersFilterQuery)
    }

    async create(user: User): Promise<User> {
        const newUser = new this.userModel(user);
        return newUser.save()
    }

    async findOneAndUpdate(userFilterQuery: FilterQuery<UserDocument>, user: Partial<User>): Promise<User> {
        return this.userModel.findOneAndUpdate(userFilterQuery, user, { new: true });
    }
}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/users.service.ts
import { Injectable } from "@nestjs/common";
import { v4 as uuidv4 } from 'uuid';
import { UpdateUserDto } from "./dto/update-user.dto";

import { User } from "./schemas/user.schema";
import { UsersRepository } from "./users.repository";

@Injectable()
export class UsersService {
    constructor(private readonly usersRepository: UsersRepository) {}

    async getUserById(userId: string): Promise<User> {
        return this.usersRepository.findOne({ userId })
    }

    async getUsers(): Promise<User[]> {
        return this.usersRepository.find({});
    }

    async createUser(email: string, age: number): Promise<User> {
        return this.usersRepository.create({
            userId: uuidv4(),
            email,
            age,
            favoriteFoods: []
        })
    }

    async updateUser(userId: string, userUpdates: UpdateUserDto): Promise<User> {
        return this.usersRepository.findOneAndUpdate({ userId }, userUpdates);
    }
}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/dto/create-user.dto.ts
export class CreateUserDto {
    email: string;
    age: number;
}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/dto/update-user.dto.ts
export class UpdateUserDto {
    favoriteFoods: string[]
    age: number;
}
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/src/users/schemas/user.schema.ts
import { Prop, Schema, SchemaFactory } from "@nestjs/mongoose";
import { Document } from 'mongoose';

export type UserDocument = User & Document;

@Schema()
export class User {
    @Prop()
    userId: string;

    @Prop()
    email: string;

    @Prop()
    age: number;

    @Prop([String])
    favoriteFoods: string[]
}

export const UserSchema = SchemaFactory.createForClass(User);
--#

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/test/app.e2e-spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import * as request from 'supertest';
import { AppModule } from './../src/app.module';

describe('AppController (e2e)', () => {
  let app;

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

--% C:/tmp/hapus/fl1/references-nest/nestjs-intro-mongo/test/jest-e2e.json
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


import { NestFactory } from '@nestjs/core';
import { NestExpressApplication } from '@nestjs/platform-express';

import { AppModule } from './app.module';
import { join } from 'path';

async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);


  app.useStaticAssets(
    join(__dirname, '..', 'public')
  );

  await app.listen(__TEMPLATE_SERVER_PORT);
}
bootstrap();

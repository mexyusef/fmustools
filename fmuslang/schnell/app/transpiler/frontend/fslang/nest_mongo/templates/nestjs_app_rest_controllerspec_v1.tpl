import { Test, TestingModule } from '@nestjs/testing';
import { __TEMPLATE_TABLENAME_CASE__Controller } from './__TEMPLATE_TABLENAME_LOWER__.controller';

describe('__TEMPLATE_TABLENAME_CASE__Controller', () => {
  let controller: __TEMPLATE_TABLENAME_CASE__Controller;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [__TEMPLATE_TABLENAME_CASE__Controller],
    }).compile();

    controller = module.get<__TEMPLATE_TABLENAME_CASE__Controller>(__TEMPLATE_TABLENAME_CASE__Controller);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
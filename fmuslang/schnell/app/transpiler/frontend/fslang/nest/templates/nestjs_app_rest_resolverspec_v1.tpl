import { Test, TestingModule } from '@nestjs/testing';
import { __TEMPLATE_TABLENAME_CASE__Resolver } from './__TEMPLATE_TABLENAME_LOWER__.resolver';

describe('__TEMPLATE_TABLENAME_CASE__Resolver', () => {
  let resolver: __TEMPLATE_TABLENAME_CASE__Resolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [__TEMPLATE_TABLENAME_CASE__Resolver],
    }).compile();

    resolver = module.get<__TEMPLATE_TABLENAME_CASE__Resolver>(__TEMPLATE_TABLENAME_CASE__Resolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});
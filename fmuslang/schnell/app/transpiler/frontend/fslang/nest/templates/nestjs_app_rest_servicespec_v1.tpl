import { Test, TestingModule } from '@nestjs/testing';
import { __TEMPLATE_TABLENAME_CASE__Service } from './__TEMPLATE_TABLENAME_LOWER__.service';

describe('__TEMPLATE_TABLENAME_CASE__Service', () => {
  let service: __TEMPLATE_TABLENAME_CASE__Service;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [__TEMPLATE_TABLENAME_CASE__Service],
    }).compile();

    service = module.get<__TEMPLATE_TABLENAME_CASE__Service>(__TEMPLATE_TABLENAME_CASE__Service);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
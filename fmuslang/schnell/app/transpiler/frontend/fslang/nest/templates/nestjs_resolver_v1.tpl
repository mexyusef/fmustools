import { 
  Args, 
  Mutation,
  Query, 
  Resolver,   
} from '@nestjs/graphql';
import { 
  __TEMPLATE_MODELNAME_CASE__, 
  Create__TEMPLATE_MODELNAME_CASE__Input, 
  Delete__TEMPLATE_MODELNAME_CASE__Input, 
  Update__TEMPLATE_MODELNAME_CASE__Input, 
  Get__TEMPLATE_MODELNAME_CASE__Args, 
  Get__TEMPLATE_MODELNAME_CASE__sArgs 
} from './__TEMPLATE_MODELNAME_LOWER__.gql';
import { __TEMPLATE_MODELNAME_CASE__Service } from './__TEMPLATE_MODELNAME_LOWER__.service';

@Resolver(() => __TEMPLATE_MODELNAME_CASE__)
export class __TEMPLATE_MODELNAME_CASE__Resolver {

  constructor(
    private readonly __TEMPLATE_MODELNAME_LOWER__Service: __TEMPLATE_MODELNAME_CASE__Service
  ) {}

  /**
    query {
      pengguna {
        email
        age
      }
    }
    {
      "data": {
        "pengguna": [
          {
            "email": "sample-email@gmail.com",
            "age": 24
          }
        ]
      }
    }
   */

  @Query(() => [__TEMPLATE_MODELNAME_CASE__], { name: '__TEMPLATE_MODELNAME_LOWER__s', nullable: 'items' })
  public getAll(): __TEMPLATE_MODELNAME_CASE__[] {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.getAll();
  }

  /**
    query {
      __TEMPLATE_MODELNAME_LOWER__s(__TEMPLATE_MODELNAME_LOWER__Ids: ["eefebb04-f22c-4d0e-ad72-619f8bb7eddf"]) {
        __TEMPLATE_MODELNAME_LOWER__Id
        email
        age
        isSubscribed
      }
    } 

    {
      "data": {
        "__TEMPLATE_MODELNAME_LOWER__s": [
          {
            "__TEMPLATE_MODELNAME_LOWER__Id": "eefebb04-f22c-4d0e-ad72-619f8bb7eddf",
            "email": "sample-email@gmail.com",
            "age": 22,
            "isSubscribed": null
          }
        ]
      }
    }
   */
  @Query(() => [__TEMPLATE_MODELNAME_CASE__], { name: '__TEMPLATE_MODELNAME_LOWER__s', nullable: 'items' })
  public getList(@Args() get__TEMPLATE_MODELNAME_CASE__sArgs: Get__TEMPLATE_MODELNAME_CASE__sArgs): __TEMPLATE_MODELNAME_CASE__[] {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.getList(get__TEMPLATE_MODELNAME_CASE__sArgs);
  }

  /**
    query {
      __TEMPLATE_MODELNAME_LOWER__(__TEMPLATE_MODELNAME_LOWER__Id: "eefebb04-f22c-4d0e-ad72-619f8bb7eddf") {
        __TEMPLATE_MODELNAME_LOWER__Id
        email
        age
        isSubscribed
      }
    }

    {
      "data": {
        "__TEMPLATE_MODELNAME_LOWER__": {
          "__TEMPLATE_MODELNAME_LOWER__Id": "eefebb04-f22c-4d0e-ad72-619f8bb7eddf",
          "email": "sample-email@gmail.com",
          "age": 22,
          "isSubscribed": null
        }
      }
    }
   */
  @Query(() => __TEMPLATE_MODELNAME_CASE__, { name: '__TEMPLATE_MODELNAME_LOWER__', nullable: true })
  public getDetail(@Args() get__TEMPLATE_MODELNAME_CASE__Args: Get__TEMPLATE_MODELNAME_CASE__Args): __TEMPLATE_MODELNAME_CASE__ {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.getDetail(get__TEMPLATE_MODELNAME_CASE__Args);
  }

  /**
    mutation {
      create(create__TEMPLATE_MODELNAME_CASE__Data: {email: "sample-email@gmail.com", age: 22}) {
        __TEMPLATE_MODELNAME_LOWER__Id
        email
        age
        isSubscribed
      }
    }

    {
      "data": {
        "create": {
          "__TEMPLATE_MODELNAME_LOWER__Id": "eefebb04-f22c-4d0e-ad72-619f8bb7eddf",
          "email": "sample-email@gmail.com",
          "age": 22,
          "isSubscribed": null
        }
      }
    }

    mutation {
      create(create__TEMPLATE_MODELNAME_CASE__Data: {email: "sample-email@gmail.com", age: 27}) {
        __TEMPLATE_MODELNAME_LOWER__Id
        email
        age
      }
    }
    
    {
      "data": {
        "create": {
          "__TEMPLATE_MODELNAME_LOWER__Id": "31220e5c-22ae-4369-8686-7172dd26aebc",
          "email": "sample-email@gmail.com",
          "age": 27
        }
      }
    }
   */
  @Mutation(() => __TEMPLATE_MODELNAME_CASE__)
  public create(@Args('create__TEMPLATE_MODELNAME_CASE__Data') create__TEMPLATE_MODELNAME_CASE__Data: Create__TEMPLATE_MODELNAME_CASE__Input): __TEMPLATE_MODELNAME_CASE__ {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.create(create__TEMPLATE_MODELNAME_CASE__Data);
  }

  @Mutation(() => __TEMPLATE_MODELNAME_CASE__)
  public update(@Args('update__TEMPLATE_MODELNAME_CASE__Data') update__TEMPLATE_MODELNAME_CASE__Data: Update__TEMPLATE_MODELNAME_CASE__Input): __TEMPLATE_MODELNAME_CASE__ {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.update(update__TEMPLATE_MODELNAME_CASE__Data);
  }

  @Mutation(() => __TEMPLATE_MODELNAME_CASE__)
  public delete(@Args('delete__TEMPLATE_MODELNAME_CASE__Data') delete__TEMPLATE_MODELNAME_CASE__Data: Delete__TEMPLATE_MODELNAME_CASE__Input): __TEMPLATE_MODELNAME_CASE__ {
    return this.__TEMPLATE_MODELNAME_LOWER__Service.delete(delete__TEMPLATE_MODELNAME_CASE__Data);
  }

}

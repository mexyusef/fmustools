import { 
  Column, 
  Entity, 
  PrimaryGeneratedColumn, 
} from "typeorm";


export enum __TEMPLATE_MODELNAME_CASE__Status {
  Created = 0,
  InProgress = 1,
  Done = 2,
}

@Entity('__TEMPLATE_MODELNAME_LOWER__')
export class __TEMPLATE_MODELNAME_CASE__Entity {

  @PrimaryGeneratedColumn ()
  id: number;

  @Column ({nullable: true, length: 64})
  title: string;

  @Column ({nullable: true, length: 1024})
  description: string;

  @Column ()
  status: __TEMPLATE_MODELNAME_CASE__Status;

}

export class Create__TEMPLATE_MODELNAME_CASE__Dto {
  // readonly id: number;
  readonly title: string;
  readonly description: string;
  readonly status: __TEMPLATE_MODELNAME_CASE__Status;
}

export class Update__TEMPLATE_MODELNAME_CASE__Dto {
  // readonly id?: number;
  readonly title?: string;
  readonly description?: string;
  readonly status?: __TEMPLATE_MODELNAME_CASE__Status;
}

export interface __TEMPLATE_MODELNAME_CASE__RO {
  __TEMPLATE_MODELNAME_LOWER__: __TEMPLATE_MODELNAME_CASE__Entity;
}

export interface __TEMPLATE_MODELNAME_CASE__sRO {
  __TEMPLATE_MODELNAME_LOWER__: __TEMPLATE_MODELNAME_CASE__Entity[];
	__TEMPLATE_MODELNAME_LOWER__Count: number;
}

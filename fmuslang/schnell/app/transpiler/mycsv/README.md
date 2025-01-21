# workflow

main.py
  => 
    handler (handlers/__init__.py)
# mana yg sudah dan mana yg belum?

# LOG
==================== $[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s

csv_operation
  csv_keyword
  csv_code      [usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s

di sini item punya anak...csv_code yg kita butuhkan...

==================== $mg,pg/[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s

csv_operation
  csv_keyword
  csv_config
    csv_items
      mongoose
      sql_postgres
  csv_code      [usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s

mg/[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s

mg,sqlz/[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s

mg, sqlz, pris/[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk;title,s;publisher,s


mg/[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk,df=Tulisanku;title,s;publisher,s
n = not null, N = null
mg/[usef:rahasia@localhost:5432/hapuslah]{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s

mg/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s
{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s

pris/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s
pris/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s,u
https://youtu.be/mU8-nKwfw4Y?t=2163
pris/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;user,fk/User.id/d=cascade
pris/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;posts,[s]

sqlz/{@Book=#5}isbn,s,pk,n,df=Tulisanku;title,s;publisher,s

import { ARRAY, BIGINT, BOOLEAN, DATE, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, STRING, TEXT, UUID, UUIDV1, UUIDV4, } from 'sequelize';

gimana hasilkan:

const fieldsMap = {
  title: STRING,
  description: TEXT,
  status: {
    type: STRING,
    values: [
      "created",
      "inprogress",
      "done"
    ],
    default: "created"
  },
  date: DATE
};

sqlz/{@Todo=#5}title,s;description,t;status,s,(created,inprogress,done>created);tanggal,dt

pengennya gimana:
dari lalang:

username,s; password,s
dst.
ini kita sebut csv_code

??csv_code
??mg/csv_code
??sqlz/csv_code
??sboot,sqlz/csv_code

contoh generate:
mongoose
sequelize
graphql this and that...
go struct
rust struct

ada juga csv_code == help (read help) dan help* (edit)
utk lihat pemetaannya gimana

nsp/{@Product=#5}title,s;description,s;price,n
nsm/{@Product=#5}title,s;description,s;price,n
nsm/{@Product=#5}title,s,N;description,s,N;price,n,N;inStock,n,N,df=0
nsm/{@Product=#5}title,s,N;description,s,N;price,n,N;inStock,n,N,df=0;images,[s]

nsm/{@Product=#5}category,s,N;checked,b,N,df=false;content,s,N;description,s,N;images,[s],N,df=__EMPTY;inStock,n,N,df=0;price,n,N;sold,n,N,df=0;title,s,N

nsm/{@Product=#5}
category,s,n;
checked,b,n,df=false;
content,s,N;
description,s,N;
images,[],N,df=[];
inStock,n,N,df=0;
price,n,N;
sold,n,N,df=0;
title,s,N

title,s,N;description,s,N;price,n,N;inStock,n,N,df=0;images,[s]

nsp/{@Product=#5}title,s,N;description,s,N;price,n,N;inStock,n,N,df=0;images,[s]

dj/{@Product=#5}category,s,N;checked,b,N,df=false;content,s,N;description,s,N;images,[s],N,df=__EMPTY;inStock,n,N,df=0;price,n,N;sold,n,N,df=0;title,s,N

json1/{@Product=#5}category,s,N;checked,b,N,df=false;content,s,N;description,s,N;images,[s],N,df=__EMPTY;inStock,n,N,df=0;price,n,N;sold,n,N,df=0;title,s,N
json2/{@Product=#5}category,s,N;checked,b,N,df=false;content,s,N;description,s,N;images,[s],N,df=__EMPTY;inStock,n,N,df=0;price,n,N;sold,n,N,df=0;title,s,N
csv/{@Product=#5}category,s,N;checked,b,N,df=false;content,s,N;description,s,N;images,[s],N,df=__EMPTY;inStock,n,N,df=0;price,n,N;sold,n,N,df=0;title,s,N

csv/{@PostReport,ts,-id,->User/id/user_id/user}category,s,N

{@PostReport,ts,-id,->User/id/user_id/user}category,s,N

database
  table
    configuration
      config_spec
        config_name_spec
          schema_table
            tablename           PostReport
      config_timestamp_spec
      config_remove_attribute_id
      config_spec
        has_one_syntax
          assoc_table           User
          foreign_column        id
          domestic_column       user_id
          as_column             user
    statement
      column_name               category
      column_type_spec
        string
      column_constraint_spec
        not_null

AnyNode(label='root', output='', outputs=[], type='root')
└── AnyNode(model='PostReport', name='table', timestamp=True, type='table')
    └── AnyNode(allowNull=False, hasConstraint=True, label='category', type='string')
...

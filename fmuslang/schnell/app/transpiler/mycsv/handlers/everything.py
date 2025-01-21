from schnell.app.dirutils import joiner, joinhere
from schnell.app.fileutils import file_content


def headerbody(header, body):
    delimiter = f'\n{"*"*10}\n'
    kembali = header + delimiter + body
    return kembali


def provide_vue(tables, RootNode):
    header = "provide vue header here"
    body = "provide vue body here"
    return headerbody(header, body)


def provide_springboot(tables, RootNode):
    # header = 'provide springboot header here'
    # body = 'provide springboot body here'
    # return headerbody(header, body)
    from .be_springboot import be_springboot

    head1 = f'\n{"="*20}[be_springboot]\n'
    satu = be_springboot(tables)
    return head1 + satu


def provide_quarkus(tables, RootNode):
    header = "provide quarkus header here"
    body = "provide quarkus body here"
    return headerbody(header, body)


def provide_react(tables, RootNode):
    header = "provide react header here"
    body = "provide react body here"
    return headerbody(header, body)


def provide_play(tables, RootNode):
    header = "provide play header here"
    body = "provide play body here"
    return headerbody(header, body)


def provide_gonic(tables, RootNode):
    header = "provide gonic header here"
    body = "provide gonic body here"
    return headerbody(header, body)


def provide_angular(tables, RootNode):
    header = "provide angular header here"
    body = "provide angular body here"
    return headerbody(header, body)


def provide_django(tables, RootNode):
    # header = 'provide django header here'
    # body = 'provide django body here'
    # return headerbody(header, body)
    from .django_orm import django_orm

    head1 = f'\n{"="*20}[django]\n'
    satu = django_orm(tables)
    return head1 + satu


def provide_fastapi(tables, RootNode):
    # header = 'provide fastapi header here'
    # body = 'provide fastapi body here'
    # return headerbody(header, body)
    from .be_fastapi import be_fastapi

    head1 = f'\n{"="*20}[fastapi]\n'
    satu = be_fastapi(tables)
    return head1 + satu


def provide_flask(tables, RootNode):
    # header = 'provide flask header here'
    # body = 'provide flask body here'
    # return headerbody(header, body)
    from .be_flask import be_flask

    head1 = f'\n{"="*20}[flask]\n'
    satu = be_flask(tables)
    return head1 + satu


def provide_nest(tables, RootNode):
    # header = 'provide nest header here'
    # body = 'provide nest body here'
    # return headerbody(header, body)
    from .nest_mongoose import nest_mongoose
    from .nest_typeorm import nest_typeorm

    head1 = f'\n{"="*20}[nest mongo]\n'
    satu = nest_mongoose(tables)
    dua = nest_typeorm(tables)
    head2 = f'\n{"="*20}[nest pg]\n'
    hasil = head1 + satu + head2 + dua
    return hasil


def provide_next(tables, RootNode):
    header = "provide next header here"
    body = "provide next body here"
    return headerbody(header, body)


def provide_node(tables, RootNode):
    # header = 'provide node header here'
    # body = 'provide node body here'
    # return headerbody(header, body)
    from .sequelize import sequelize

    head1 = f'\n{"="*20}[node sequelize]\n'
    satu = sequelize(tables)
    return head1 + satu


def language_go(tables, RootNode):
    from .struct_go import struct_go

    head1 = f'\n{"="*20}[Go]\n'
    satu = struct_go(tables)
    return head1 + satu


def language_java(tables, RootNode):
    from .struct_java import struct_java

    head1 = f'\n{"="*20}[Java]\n'
    satu = struct_java(tables)
    return head1 + satu


def language_kotlin(tables, RootNode):
    from .struct_kt import struct_kt

    head1 = f'\n{"="*20}[Kotlin]\n'
    satu = struct_kt(tables)
    return head1 + satu


def language_rust(tables, RootNode):
    from .struct_rs import struct_rs

    head1 = f'\n{"="*20}[Rust]\n'
    satu = struct_rs(tables)
    return head1 + satu


def language_typescript(tables, RootNode):
    from .struct_ts import struct_ts

    head1 = f'\n{"="*20}[Typescript]\n'
    satu = struct_ts(tables)
    return head1 + satu


def orm_hibernate(tables, RootNode):
    from .hibernate import hibernate

    head1 = f'\n{"="*20}[Hibernate]\n'
    satu = hibernate(tables)
    return head1 + satu


def orm_mybatis(tables, RootNode):
    from .mybatis import mybatis

    head1 = f'\n{"="*20}[MyBatis]\n'
    satu = mybatis(tables)
    return head1 + satu


def orm_prisma(tables, RootNode):
    from .prisma import prisma

    head1 = f'\n{"="*20}[Prisma]\n'
    satu = prisma(tables)
    return head1 + satu


def sql_mssql(tables, RootNode):
    from .sql_mssql import sql_mssql

    head1 = f'\n{"="*20}[MS SQL]\n'
    satu = sql_mssql(tables)
    return head1 + satu


def sql_mysql(tables, RootNode):
    from .sql_mysql import sql_mysql

    head1 = f'\n{"="*20}[MySQL]\n'
    satu = sql_mysql(tables)
    return head1 + satu


def sql_postgres(tables, RootNode):
    from .sql_postgres import sql_postgres

    head1 = f'\n{"="*20}[Postgres]\n'
    satu = sql_postgres(tables)
    return head1 + satu


def sql_sqlite(tables, RootNode):
    from .sql_sqlite import sql_sqlite

    head1 = f'\n{"="*20}[SQLite]\n'
    satu = sql_sqlite(tables)
    return head1 + satu


def call_swagger_json(tables, RootNode):
    from .swagger_json import swagger_json

    head1 = f'\n{"="*20}[swagger_json]\n'
    satu = swagger_json(tables)
    return head1 + satu


def call_swagger_yaml(tables, RootNode):
    from .swagger_yaml import swagger_yaml

    head1 = f'\n{"="*20}[swagger_yaml]\n'
    satu = swagger_yaml(tables)
    return head1 + satu


def call_swagger_postman(tables, RootNode):
    from .swagger_postman import swagger_postman

    head1 = f'\n{"="*20}[swagger_postman]\n'
    satu = swagger_postman(tables)
    return head1 + satu


def mobile_rn(tables, RootNode):
    from .mobile_rn import mobile_rn

    head1 = f'\n{"="*20}[React Native]\n'
    satu = mobile_rn(tables)
    return head1 + satu


providers = [
    # provide_django,
    # provide_fastapi,
    # provide_flask,
    # provide_gonic,
    # provide_nest,
    # provide_next,
    # provide_node,
    # provide_play,
    # provide_quarkus,
    # provide_react,
    provide_springboot,
    # provide_angular,
    # provide_vue,
    # language_go,
    # language_java,
    # language_kotlin,
    # language_rust,
    # language_typescript,
    # sql_mssql,
    # sql_mysql,
    # sql_postgres,
    # sql_sqlite,
    # orm_hibernate,
    # orm_mybatis,
    # orm_prisma,
    # call_swagger_json,
    # call_swagger_yaml,
    # call_swagger_postman,
]


banner = file_content(joinhere(__file__, "templates/everything/banner.txt"))


def everything(tables, RootNode):
    """
    /c. all/{@Todo}title,s
    """
    kembali = banner

    for provider in providers:
        kembali += "\n\n"
        kembali += provider(tables, RootNode)
    return kembali

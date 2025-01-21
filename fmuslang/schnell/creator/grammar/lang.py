from .languages import (
  embedded_bahasa_languages_header,
  embedded_bahasa_languages_body,
  bun_header,
  bun_body,
  fintech_header, fintech_body,
  flask_header, flask_body,
  vscode_header, vscode_body,
)
from .languages.lang_kernel import lang_kernel_body, lang_kernel_header
from .languages.lang_llm  import llm_body, llm_header
from .languages.lang_langchain import langchain_body, langchain_header
from .lang_fastapi import fastapi_header, fastapi_body
from .lang_mmm import (
  mmm_header,
  mmm_body,
)
from .languages.lang_builder_io import (
  header as builder_io_header,
  body as builder_io_body,
)
from .languages.lang_cloud import (
  header as cloud_header,
  body as cloud_body,
)
from .languages.lang_google import (
  header as google_header,
  body as google_body,
)
from .languages.lang_play import (
  header as play_header,
  body as play_body,
)
from .languages.lang_zio import (
  header as zio_header,
  body as zio_body,
)
from .lang_akka import (
  embedded_akka_languages_header,
  embedded_akka_languages_body,
)
from .lang_algods import (algods_languages_header,algods_languages_body)
from .lang_android import (
  embedded_android_languages_header,
  embedded_android_languages_body,
)
from .lang_angular import (
  angular_head,
  angular_body,
)
from .lang_aspnetcore import (aspnetcore_header, aspnetcore_body)
from .lang_buku import (buku_header,buku_body)
from .lang_compete import (
  compete_header,
  compete_body,
)
from .lang_crack import (
  embedded_crack_languages_header,
  embedded_crack_languages_body,
)
from .lang_cppweb import (
  embedded_cppweb_languages_header,
  embedded_cppweb_languages_body,
)
from .lang_data import (embedded_data_languages_header,embedded_data_languages_body)
from .lang_database import (embedded_database_languages_header,embedded_database_languages_body)
from .lang_deno import (deno_header,deno_body)
from .lang_devops import (embedded_devops_languages_header,embedded_devops_languages_body)
from .lang_django import (embedded_django_languages_header,embedded_django_languages_body)
from .lang_flutter import(embedded_flutter_languages_header,embedded_flutter_languages_body)
from .lang_gawe import (
  gawe_header,
  gawe_body,
)
from .lang_goweb import (embedded_goweb_languages_header,embedded_goweb_languages_body)
from .lang_guilang import (
  gui_header,gui_body,
)
from .lang_html_css_js import (embedded_html_css_js_languages_header, embedded_html_css_js_languages_body)
from .lang_karya import (karya_header, karya_body)
from .lang_laravel import (embedded_laravel_languages_header,embedded_laravel_languages_body)
from .lang_medium import (
  medium_languages_header,
  medium_languages_body
)
from .lang_ml import (ml_languages_header, ml_languages_body)
from .lang_node import (embedded_node_languages_header,embedded_node_languages_body)
from .lang_nest import (nest_header, nest_body)
from .lang_next import (next_header, next_body)
from .lang_pattern import (embedded_pattern_languages_header,embedded_pattern_languages_body)
from .lang_phoenix import (embedded_phoenix_languages_header,embedded_phoenix_languages_body)
from .lang_proto import (
  embedded_proto_languages_header,
  embedded_proto_languages_body,
)
from .lang_rails import (embedded_rails_languages_header,embedded_rails_languages_body)
from .lang_react import (
  embedded_react_languages_header,
  embedded_react_languages_body,
)
from .lang_reactnative import (embedded_reactnative_languages_header,embedded_reactnative_languages_body)
from .lang_rustweb import (
  embedded_rustweb_languages_header,
  embedded_rustweb_languages_body
)
from .lang_springboot import (
  embedded_springboot_languages_header,
  embedded_springboot_languages_body,
)
from .lang_spring import (
  header as spring_header,
  body as spring_body,
)
from .lang_vue import (
  vue_languages_header,
  vue_languages_body,
)
from .lang_workup import (
  workup_header,
  workup_body,
)
# dataviz js: https://youtu.be/2LhoCfjm8R4?t=12041

from .lang_parser import parser_header, parser_body
from .lang_scraper import scraper_header, scraper_body
from .lang_head import lang_head
from .lang_body import lang_body

main_languages = f"""

programs: program (program)*

program: statement*

//  | class
//  | class_ask
//  | modules
//  | modules_ask
//modules: "@m" class*
//class: "@c" statement*
//modules_ask: "@m~"
//class_ask: "@c~"

{lang_head}
{embedded_akka_languages_header}
{algods_languages_header}
{angular_head}
{embedded_bahasa_languages_header}
{buku_header}
{bun_header}
{embedded_android_languages_header}
{aspnetcore_header}
{builder_io_header}
{cloud_header}
{compete_header}
{embedded_cppweb_languages_header}
{embedded_crack_languages_header}
{embedded_data_languages_header}
{embedded_database_languages_header}
{deno_header}
{embedded_devops_languages_header}
{embedded_django_languages_header}
{fastapi_header}
{fintech_header}
{flask_header}
{embedded_flutter_languages_header}
{gawe_header}
{google_header}
{embedded_goweb_languages_header}
{gui_header}
{embedded_html_css_js_languages_header}
{karya_header}
{lang_kernel_header}
{langchain_header}
{llm_header}
{embedded_laravel_languages_header}
{medium_languages_header}
{ml_languages_header}
{nest_header}
{next_header}
{embedded_node_languages_header}
{embedded_pattern_languages_header}
{embedded_phoenix_languages_header}
{play_header}
{embedded_proto_languages_header}
{embedded_rails_languages_header}
{embedded_react_languages_header}
{embedded_reactnative_languages_header}
{embedded_rustweb_languages_header}
{spring_header}
{embedded_springboot_languages_header}
{vue_languages_header}
{mmm_header}
{parser_header}
{scraper_header}
{vscode_header}
{workup_header}
{zio_header}

  | modifier statement
  | statement edit_or_execute_fmus?
  | statement baris_cari                    -> statement_berbaris_cari
  | statement wieke wieke wieke wieke wieke -> statement_berwiekes
  | statement wieke wieke wieke wieke       -> statement_berwiekes
  | statement wieke wieke wieke             -> statement_berwiekes
  | statement wieke wieke                   -> statement_berwiekes
  | statement wieke                         -> statement_berwiekes
  | statement only_toc                      -> statement_show_only_toc
  | statement show_content                  -> statement_show_content

//  | statement wieke (wieke)* -> statement_berwiekes
//  | statement wiekes      -> statement_berwiekes

// modifier # kita taro di bawah krn embedded* banyak pake #
// used:
// @c @l @m 
// A B I L M P T V
// c d f l

// agar prioritas
{embedded_akka_languages_body}
{algods_languages_body}
{angular_body}
{embedded_bahasa_languages_body}
{builder_io_body}
{buku_body}
{bun_body}
{cloud_body}
{embedded_android_languages_body}
{aspnetcore_body}
{compete_body}
{embedded_cppweb_languages_body}
{embedded_crack_languages_body}
{embedded_data_languages_body}
{embedded_database_languages_body}
{deno_body}
{embedded_devops_languages_body}
{embedded_django_languages_body}
{fastapi_body}
{fintech_body}
{flask_body}
{embedded_flutter_languages_body}
{gawe_body}
{google_body}
{embedded_goweb_languages_body}
{gui_body}
{embedded_html_css_js_languages_body}
{karya_body}
{lang_kernel_body}
{langchain_body}
{llm_body}
{embedded_laravel_languages_body}
{medium_languages_body}
{ml_languages_body}
{nest_body}
{next_body}
{embedded_node_languages_body}
{embedded_pattern_languages_body}
{embedded_phoenix_languages_body}
{play_body}
{embedded_proto_languages_body}
{embedded_rails_languages_body}
{embedded_react_languages_body}
{embedded_reactnative_languages_body}
{embedded_rustweb_languages_body}
{spring_body}
{embedded_springboot_languages_body}
{vue_languages_body}
{mmm_body}
{parser_body}
{scraper_body}
{vscode_body}
{workup_body}
{zio_body}

{lang_body}

// ini mengganggu
modifier: "(+"    -> public
  | "(-"          -> private
  | "(#"          -> protected
  | "(f"          -> final
  | "(o"          -> override
  | "(r"          -> return
  | "(s"          -> static
  | "(v"          -> volatile
  | "(w"          -> await
  | "(y"          -> async

baris_cari        : "`" HURUF_FOLDER_LAMA_BERBINTANG_NOSPACE
wiekes            : wieke (wieke)*
wieke             : "\\\\" HURUF_FOLDER_LAMA_BERBINTANG_NOSPACE
edit_or_execute_fmus: "?e"  -> edit_fmus // ff?e
| "?x"                      -> exec_fmus // ff?x
only_toc          : "#"
show_content      : "*"
library_usage     : "@@" "[" HURUF_FOLDER "]"
"""

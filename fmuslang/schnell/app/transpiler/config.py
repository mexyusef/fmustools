
# from schnell.app.transpiler.zgenerate.gen_js import generate as generate_js
from schnell.app.transpiler.zgenerate.gen_py import generate as generate_py
from schnell.app.transpiler.zgenerate.gen_rb import generate as generate_rb
from schnell.app.transpiler.zgenerate.gen_ts import generate as generate_ts
from schnell.app.transpiler.zgenerate.gen_kt import generate as generate_kt
from schnell.app.transpiler.zgenerate.gen_java import generate as generate_java
from schnell.app.transpiler.zgenerate.gen_dart import generate as generate_dart
from schnell.app.transpiler.zgenerate.gen_go import generate as generate_go
from schnell.app.transpiler.zgenerate.gen_rs import generate as generate_rs
from schnell.app.transpiler.zgenerate.gen_v import generate as generate_v

languages = [
  'clj',
  'cpp',
  'cs',
  'dart',
  'elixir',
  'erlang',
  'go',
  'hs',
  'java',
  'js',
  'kt',
  'php',
  'pl',
  'py',
  'rb',
  'scala',
  'swift',
  'ts',
  'v',
]

daftar_languages = {
  'py'              : generate_py,
  'dart'            : generate_dart,
  'go'              : generate_go,
  'java'            : generate_java,
  'kt'              : generate_kt,
  'rb'              : generate_rb,
  'rs'              : generate_rs,
  'ts'              : generate_ts,
  'v'               : generate_v,

  # unused
  'clj'             : generate_py,
  'cpp'             : generate_py,
  'cs'              : generate_py,
  'elixir'          : generate_py,
  'erlang'          : generate_py,
  'hs'              : generate_py,
  'js'              : generate_py,
  'php'             : generate_py,
  'scala'           : generate_py,
}

program_context = {
  'language_context': [],
  'library_context': [],
  'framework_context': [],
  'tools_context': [],
}

scope_context = {}

statement_context = {}

library_context = {}

framework_context = {}

tools_context = {}

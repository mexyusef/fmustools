from app.libpohon.columnify import (
  columnify_and_transform,
  transform_columns,
  columnify,
)
from app.printutils import indah, indah4
from app.stringutils import tabify_content, tabify_contentlist
from app.treeutils import tables_from_rootnode
from app.usutils import tab
from app.fileutils import (
  file_content,
  append_entry_tostring,
  # append_entry_tofile,
  file_write,
)
from app.dirutils import (
  get_cwd, joiner, here, absolutify,
)
from app.fileutils import get_definition_by_key_permissive_start
from app.fmus import Fmus


disini = here(__file__)


class Coordinator:


  def __init__(self, RootNode, project_dir='input'):
    self.root = RootNode
    self.tables = tables_from_rootnode(self.root)
    self.project_dir = project_dir
    self.mkfile_input = joiner(disini, 'index-input.mk')
    self.mkfile_output = joiner(get_cwd(), 'index.mk')
    self.mkfile_input_content = file_content(self.mkfile_input)


  def mkfile(self):
    print('hasil mkfile:', self.mkfile_output)


  def model(self):
    print('hasil model:', self.mkfile_output)


  def save_file(self):
    print('hasil save file:', self.mkfile_output)


  def run_fmus(self, filepath, baris_entry):
    program = get_definition_by_key_permissive_start(filepath, baris_entry)
    fmus = Fmus(False)
    fmus.set_file_dir_template(filepath)
    fmus.process(program)


  def generate(self):
    # self.mkfile()
    # self.model()
    # self.save_file()

    indah4('Masukkan direktori parent folder untuk fullstack:', newline=False)
    root_folder = input(' ')
    # create if not exist
    # create backend+frontend+mobile+desktop
    # pertama nda dulu...
    root_folder = absolutify(root_folder)
    baris_entry = 'index/fmus'
    indah(f'Press key jika siap generate fullstack apps di {root_folder}', warna='yellow', newline=False)
    input(' ')

    from .assistance import Coordinator as assistance_generator
    generator = assistance_generator (self.root, joiner(root_folder, 'assistance'))
    generator.generate()
    filepath = generator.output()
    self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate node_antd_pg... ')
    # from ..node_antd import Coordinator as node_antd_generator
    # generator = node_antd_generator (self.root, joiner(root_folder, 'node_antd_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate node_antd_mg... ')
    # from ..node_antd_mongo import Coordinator as node_antd_mongo_generator
    # generator = node_antd_mongo_generator (self.root, joiner(root_folder, 'node_antd_mg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate node_apollo_pg... ')
    # from ..node_apollo import Coordinator as node_apollo_generator
    # generator = node_apollo_generator (self.root, joiner(root_folder, 'node_apollo_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .node_next import Coordinator as node_next_generator
    # generator = node_next_generator (self.root, joiner(root_folder, 'node_next'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .node_ts1_mg import Coordinator as node_ts1_mg_generator
    # generator = node_ts1_mg_generator (self.root, joiner(root_folder, 'node_ts1_mg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate nest_pg... ')
    # from ..nest import Coordinator as nest_generator
    # generator = nest_generator (self.root, joiner(root_folder, 'nest_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate nest_mg... ')
    # from ..nest_mongo import Coordinator as nest_mongo_generator
    # generator = nest_mongo_generator (self.root, joiner(root_folder, 'nest_mg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate django_pg... ')
    # from ..django import Coordinator as django_generator
    # generator = django_generator (self.root, joiner(root_folder, 'django_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate django_mg... ')
    # from ..django_mongo import Coordinator as django_mongo_generator
    # generator = django_mongo_generator (self.root, joiner(root_folder, 'django_mg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate fastapi_pg... ')
    # from ..fastapi import Coordinator as fastapi_generator
    # generator = fastapi_generator (self.root, joiner(root_folder, 'fastapi_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate flask_pg... ')
    # from ..flask import Coordinator as flask_generator
    # generator = flask_generator (self.root, joiner(root_folder, 'flask_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate moleculer_pg... ')
    # from ..moleculer import Coordinator as moleculer_generator
    # generator = moleculer_generator (self.root, joiner(root_folder, 'moleculer_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate springboot_pg... ')
    # from ..springboot import Coordinator as springboot_generator
    # generator = springboot_generator (self.root, joiner(root_folder, 'springboot_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate quarkus_pg... ')
    # from ..quarkus import Coordinator as quarkus_generator
    # generator = quarkus_generator (self.root, joiner(root_folder, 'quarkus_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # # input('Press key untuk generate dropwizard_pg... ')
    # from ..dropwizard import Coordinator as dropwizard_generator
    # generator = dropwizard_generator (self.root, joiner(root_folder, 'dropwizard_pg'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from ..jakartaee import Coordinator as jakartaee_generator
    # generator = jakartaee_generator (self.root, joiner(root_folder, 'jakartaee'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .gin_gonic import Coordinator as gin_gonic_generator
    # generator = gin_gonic_generator (self.root, joiner(root_folder, 'gin_gonic'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .gin_gonic_simple import Coordinator as gin_gonic_simple_generator
    # generator = gin_gonic_simple_generator (self.root, joiner(root_folder, 'gin_gonic_simple'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .go_echo import Coordinator as go_echo_generator
    # generator = go_echo_generator (self.root, joiner(root_folder, 'go_echo'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .go_mux import Coordinator as go_mux_generator
    # generator = go_mux_generator (self.root, joiner(root_folder, 'go_mux'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from ..mobile.flutter import Coordinator as mobile_flutter_generator
    # generator = mobile_flutter_generator (self.root, joiner(root_folder, 'mobile_flutter'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from ..mobile.kotlin import Coordinator as mobile_kotlin_generator
    # generator = mobile_kotlin_generator (self.root, joiner(root_folder, 'mobile_kotlin'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from ..mobile.reactnative import Coordinator as mobile_reactnative_generator
    # generator = mobile_reactnative_generator (self.root, joiner(root_folder, 'mobile_reactnative'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_argon import Coordinator as next_argon_generator
    # generator = next_argon_generator (self.root, joiner(root_folder, 'next_argon'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_mkit import Coordinator as next_mkit_generator
    # generator = next_mkit_generator (self.root, joiner(root_folder, 'next_mkit'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_mui import Coordinator as next_mui_generator
    # generator = next_mui_generator (self.root, joiner(root_folder, 'next_mui'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_notus import Coordinator as next_notus_generator
    # generator = next_notus_generator (self.root, joiner(root_folder, 'next_notus'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_tailwind import Coordinator as next_tailwind_generator
    # generator = next_tailwind_generator (self.root, joiner(root_folder, 'next_tailwind'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_ts1 import Coordinator as next_ts1_generator
    # generator = next_ts1_generator (self.root, joiner(root_folder, 'next_ts1'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .next_ts2 import Coordinator as next_ts2_generator
    # generator = next_ts2_generator (self.root, joiner(root_folder, 'next_ts2'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_airframe import Coordinator as react_airframe_generator
    # generator = react_airframe_generator (self.root, joiner(root_folder, 'react_airframe'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_argon import Coordinator as react_argon_generator
    # generator = react_argon_generator (self.root, joiner(root_folder, 'react_argon'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_iot import Coordinator as react_iot_generator
    # generator = react_iot_generator (self.root, joiner(root_folder, 'react_iot'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_light import Coordinator as react_light_generator
    # generator = react_light_generator (self.root, joiner(root_folder, 'react_light'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_mkit import Coordinator as react_mkit_generator
    # generator = react_mkit_generator (self.root, joiner(root_folder, 'react_mkit'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_mui import Coordinator as react_mui_generator
    # generator = react_mui_generator (self.root, joiner(root_folder, 'react_mui'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_notus import Coordinator as react_notus_generator
    # generator = react_notus_generator (self.root, joiner(root_folder, 'react_notus'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_now import Coordinator as react_now_generator
    # generator = react_now_generator (self.root, joiner(root_folder, 'react_now'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_paper import Coordinator as react_paper_generator
    # generator = react_paper_generator (self.root, joiner(root_folder, 'react_paper'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_ts1 import Coordinator as react_ts1_generator
    # generator = react_ts1_generator (self.root, joiner(root_folder, 'react_ts1'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_volt import Coordinator as react_volt_generator
    # generator = react_volt_generator (self.root, joiner(root_folder, 'react_volt'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .react_xtreme import Coordinator as react_xtreme_generator
    # generator = react_xtreme_generator (self.root, joiner(root_folder, 'react_xtreme'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .tokyo_white import Coordinator as tokyo_white_generator
    # generator = tokyo_white_generator (self.root, joiner(root_folder, 'tokyo_white'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

    # from .vue_materio import Coordinator as vue_materio_generator
    # generator = vue_materio_generator (self.root, joiner(root_folder, 'vue_materio'))
    # generator.generate()
    # filepath = generator.output()
    # self.run_fmus(filepath, baris_entry)

  def output(self):
    return self.mkfile_output

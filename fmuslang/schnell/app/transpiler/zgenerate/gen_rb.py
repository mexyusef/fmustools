from schnell.app.appconfig import programming_data
from schnell.app.dirutils import (
  here, 
  joiner,
  tempdir,
  new_filename_timestamp,
)
from schnell.app.fmus import Fmus
from schnell.app.printutils import print_enumerate
from schnell.app.utils import (
	tidur,
  env_int,
)
try:
  from schnell.app.transpiler.editor import editor
except ImportError as err:
  pass
from schnell.app.treeutils import (
  data, 
  token, 
  child1, 
  child2, 
  child3, 
  child4,
  child,
  chdata,
  chtoken,
  anak,
  beranak, 
  sebanyak,
  jumlahanak,
  istoken,
)


ULIBPY_FMUS_CAPTURE_STDOUT_STDERR = programming_data['j']['schnell']['app']['configuration']['ULIBPY_FMUS_CAPTURE_STDOUT_STDERR']
ULIBPY_STDOUT_CAPTURE_SLEEP_MS = programming_data['j']['schnell']['app']['configuration']['ULIBPY_STDOUT_CAPTURE_SLEEP_MS']
peta_tipe_data = {
  'char': 'string',
  'integer': 'number',
  'float': 'number',

  'string': 'string',  
  'boolean': 'boolean',
  'any': 'nil',
  'void': 'void', 
}

class Generator:
  def __init__(self, RootNode, program_context):
    self.root = RootNode
    self.program_context = program_context
    self.indentno = 0
    self.output = ''
    # self.tabspace = '\t'
    self.tabspace = '  '
    self.empty_content = f'{self.tab()}# pass'


  def set_empty_content(self, content=None):
    if not content:
      self.empty_content = f'{self.tab()}# pass'
    else:
      self.empty_content = content


  def print(self, text):
    self.output += text


  def dedent(self):
    self.indentno -= 1 if self.indentno>0 else 0
    return self.tabspace * self.indentno


  def indent(self):
    self.indentno += 1
    return self.tabspace * self.indentno


  def tab(self, tabno=0):
    return self.tabspace * (tabno if tabno else self.indentno)


  def dec(self):
    self.indentno -= 1 if self.indentno>0 else 0


  def inc(self):
    self.indentno += 1


  def tabify_content(self, content):
    tabify = [self.tab() + item for item in content.splitlines()]
    return '\n'.join(tabify)


  def literal_bool(self, nilailiteral):
    # nilai = True if nilailiteral.data == 'boolean_true' else False
    nilai = 'true' if nilailiteral.data == 'boolean_true' else 'false'
    return nilai


  def literal_number(self, nilailiteral):
    """
    konversi ke int jadi sering bikin
    can only concatenate str (not "int") to str
    """
    # nilailiteralstr = int(nilailiteral.children[0])
    nilailiteralstr = str(nilailiteral.children[0])
    return nilailiteralstr


  def literal_char(self, nilailiteral):
    nilailiteralstr = "'"+str(nilailiteral.children[0])+"'"
    # self.output += f'\t\t\tketemu literal_char: {nilailiteralstr}\n'
    return nilailiteralstr


  def literal_string(self, nilailiteral):
    nilailiteralstr = '"'+str(nilailiteral.children[0])+'"'
    # self.output += f'\t\t\tketemu literal_string: {nilailiteralstr}\n'
    return nilailiteralstr


  def literal_list(self, nilailiteral):
    '''
    literal_list <- nilailiteral
      kadang sampai di atas sudah saja...
      *
      list_items
        *
        list_item
          expression_item
            literal
              literal_number    value
        list_item
          expression_item
            literal
              literal_number  2
        list_item
          expression_item
            literal
              literal_number  3
    '''
    # print('literal_list:', nilailiteral.data)
    kembalian_list = []
    if nilailiteral.children:
      '''
      punya: list_items
      '''
      # list_items
      list_items = nilailiteral.children[0]
      # list_item = li
      for li in list_items.children:        
        ei = li.children[0]
        if ei.data == 'expression_item':
          couldbe_literal = ei.children[0]
          if couldbe_literal.data == 'literal':
            hasil_literal = self.literal(couldbe_literal)
            kembalian_list.append(hasil_literal)
    else:
      '''
      empty list
      '''
      # self.output += '[]'
      kembalian_list = []

    return kembalian_list


  def literal_dict(self, tree):
    """
      literal_dict
        dict_items
          dict_item
            dict_item_name      a
            expression_item
              literal
                literal_number  1
          dict_item
            dict_item_name      b
            expression_item
              literal
                literal_number  2
    """
    items = child1(tree)
    entries = []
    for item in anak(items):
      key = token(child1(item))
      value = self.expression_item(child2(item), returning=True)
      entries.append(f'{key}: {value}')

    return '{' + ', '.join(entries) + '}'


  def literal(self, couldbe_literal):
    '''
    literal
      literal_list
        literal_string    value
        literal_number    value
        literal_char      value
        list_items
          *
          list_item
            expression_item
              literal
                literal_number    value

    '''
    nilailiteral = couldbe_literal.children[0]
    kembalian_literal = None
    # print('nilailiteral:', nilailiteral)
    if nilailiteral.children:
      if nilailiteral.data == 'literal_string':
        kembalian_literal = self.literal_string(nilailiteral)        
      elif nilailiteral.data == 'literal_char':
        kembalian_literal = self.literal_char(nilailiteral)
      elif nilailiteral.data == 'literal_number':
        kembalian_literal = self.literal_number(nilailiteral)
      elif nilailiteral.data == 'literal_list':
        kembalian_literal = self.literal_list(nilailiteral)
      elif nilailiteral.data == 'literal_dict':
        kembalian_literal = self.literal_dict(nilailiteral)
      # nilailiteralstr = str(nilailiteral.children[0])
      # self.output += f'\t\t\tketemu nilailiteralstr: {nilailiteralstr}\n'
    elif nilailiteral.data .startswith('boolean'):
      '''
      literal
        boolean_true
        boolean_false
      '''
      kembalian_literal = self.literal_bool(nilailiteral)
    elif nilailiteral.data == 'literal_list':
      kembalian_literal = self.literal_list(nilailiteral)

    return kembalian_literal


  def enum_member(self, tree):
    """
    enum_member
      nama_identifier     satu
    enum_member
      nama_identifier     dua
      expression_item
        literal
          literal_number  2
    """
    nama, nilai = '', ''
    for item in anak(tree):
      if data(item) == 'nama_identifier':
        nama = token(item).upper() # https://stackoverflow.com/questions/75759/how-to-implement-enums-in-ruby
      elif data(item) == 'expression_item':
        nilai = self.expression_item(item, returning=True)
    if nilai:
      return f'{nama} = {nilai}'
    return nama


  def enum_body(self, tree):
    """
    enum_body
      enum_member_list
        enum_member
          nama_identifier     satu
        enum_member
          nama_identifier     dua
          expression_item
            literal
              literal_number  2
        enum_member
          nama_identifier     tiga
    """
    memberlist = child1(tree)
    results = []
    for index, item in enumerate(anak(memberlist),1):
      if data(item) == 'enum_member':
        hasil = self.enum_member(item)
        if not '=' in hasil:
          # ini salah utk tiga jk: satu, dua=50, tiga -> tiga = 3 harusnya 51
          hasil = f'{hasil} = {index}'
        results.append(hasil)
    
    results = [self.tab()+item for item in results]    
    return '\n'.join(results)


  def enum_declaration(self, tree):
    """
    enum_declaration
      nama_identifier   myenum
      enum_body
    """
    nama_enum, isi_enum = '', ''
    for item in anak(tree):
      if data(item) == 'nama_identifier':
        nama_enum = token(item).capitalize()
      elif data(item) == 'enum_body':
        self.inc()
        isi_enum = self.enum_body(item)
        self.dec()

    from .common import ruby_enum_info
    hasil = ruby_enum_info
    hasil = ['// ' + item for item in hasil.splitlines()]
    hasil = '\n'.join(hasil) + '\n'
    hasil += f'module {nama_enum}\n{isi_enum}\nend'
    return hasil


  def relational_expression(self, tree):
    """
    relational_expression
      expression_item
        nama_identifier i
      operator_less
      expression_item
        literal
          literal_number        2
    """
    kembalian = '__KIRI __OPER __KANAN'
    kiri = child1(tree)
    gantikiri = self.expression_item(kiri, returning=True)
    # print(f'{kiri} gantikiri', gantikiri)
    # expression item bisa hasilkan literal number
    kembalian = kembalian.replace('__KIRI', str(gantikiri))

    oper = child2(tree)
    if data(oper) == 'operator_less':
      kembalian = kembalian.replace('__OPER', '<')
    elif data(oper) == 'operator_less_equal':
      kembalian = kembalian.replace('__OPER', '<=')
    elif data(oper) == 'operator_greater':
      kembalian = kembalian.replace('__OPER', '>')
    elif data(oper) == 'operator_greater_equal':
      kembalian = kembalian.replace('__OPER', '>=')
    elif data(oper) == 'operator_equal':
      kembalian = kembalian.replace('__OPER', '==')
    elif data(oper) == 'operator_not_equal':
      kembalian = kembalian.replace('__OPER', '!=')

    kanan = child3(tree)
    gantikanan = self.expression_item(kanan, returning=True)
    # print('gantikanan', gantikanan)
    kembalian = kembalian.replace('__KANAN', str(gantikanan))
    print('relational_expression => kembalian:', kembalian)
    return kembalian


  def arithmetic_operator_to_string(self, tree):
    if data(tree) == 'operator_plus':
      return '+'
    elif data(tree) == 'operator_minus':
      return '-'
    elif data(tree) == 'operator_mult':
      return '*'
    elif data(tree) == 'operator_div':
      return '/'
    return ''


  def arithmetic_expression(self, tree):
    """
    arithmetic_expression
      expression_item
        nama_identifier x
      operator_plus
      expression_item
        nama_identifier y
    """
    kiri = self.expression_item(child1(tree), returning=True)
    oper = self.arithmetic_operator_to_string(child2(tree))
    kanan = self.expression_item(child3(tree), returning=True)
    return f"{kiri} {oper} {kanan}"


  def casting_expression(self, tree):
    """
    casting_expression
      expression_item
        nama_identifier       str
      keyword_casting
      expression_item
        nama_identifier       any
    casting_expression
      expression_item
        nama_identifier       int
      keyword_casting
      expression_item
        casting_expression
          expression_item
            nama_identifier   float
          keyword_casting
          expression_item
            nama_identifier   bool
    """
    left_ei = child1(tree)
    left = self.expression_item(left_ei, returning=True)
    kw = child2(tree)
    right_first_ei = child3(tree)
    is_nameid = data(child1(right_first_ei)) == 'nama_identifier'

    # jk hanya ada 2: tipe1>>tipe2
    # utk 3: tipe1>>tipe2>>tipe3, data adlh casting_expression
    # if is_nameid:
    #   right = self.expression_item(right_first_ei, returning=True)
    #   return f'({right}){left}'

    right = self.expression_item(right_first_ei, returning=True)
    return f'({right}){left}'


  def range_expression(self, tree):
    kembali = ''
    start,stop,step='','',''
    for item in anak(tree):
      jenis = data(item)
      if jenis == 'range_keyword':
        pass
      elif jenis == 'range_expr_config':
        pass
      elif jenis == 'range_start':
        start = token(item)
      elif jenis == 'range_stop':
        stop = token(item)
      elif jenis == 'range_step':
        step = token(item)
    kembali += f'{start}..{stop}'
    return kembali


  def expression_item(self, expritem, returning=True):
    """
    literal dalam expression_item bisa berbeda tipe hasilnya
    ada yg '' juga "" dan [] dst.
    """
    # literal
    literal = child1(expritem)
    hasil = ''
    if data(literal) == 'literal':
      hasil = self.literal(literal)
    elif data(literal) == 'nama_identifier':
      hasil = token(literal)
    elif data(literal) == 'relational_expression':
      hasil = self.relational_expression(literal)
    elif data(literal) == 'function_call':
      hasil = self.function_call(literal)
    elif data(literal) == 'arithmetic_expression':
      hasil = self.arithmetic_expression(literal)
    elif data(literal) == 'casting_expression':
      hasil = self.casting_expression(literal)
    elif data(literal) == 'casting_expression':
      hasil = self.casting_expression(literal)

    if returning:
      return hasil
    else:
      self.output += f"{hasil}"


  def declaration_value(self, tree):
    ei = child1(tree)
    nilai_variable = self.expression_item(ei, returning=True)
    return nilai_variable


  def tipe_identifier(self, tree):
    kembali = ''
    for item in anak(tree):
      if data(item) == 'tipe_data_buatan':
        kembali = chtoken(item)
      else:
        jenis = data(item)
        kembali = peta_tipe_data.get(jenis, jenis)
    return kembali


  def const_declaration(self, tree, returning=True):
    """
    $str="not a number"
    const_declaration
      declaration_name        v
      declaration_value
        expression_item
          literal
            literal_dict
              dict_items
                dict_item
                  dict_item_name      a
                  expression_item
                    nama_identifier   d
                dict_item
                  dict_item_name      b
                  expression_item
                    nama_identifier   whatever

    var_declaration: "$" declaration_config? declaration_name tipe_identifier? declaration_value?
    const_declaration: "%" declaration_config? declaration_name tipe_identifier? declaration_value?
    """
    kembali = ''
    for dahan in anak(tree):
      if data(dahan) == 'declaration_config':
        pass
      elif data(dahan) == 'declaration_name':
        declaration_name = token(dahan).capitalize() # first letter hrs besar
        if returning:
          kembali += declaration_name
        else: 
          self.print(declaration_name)
      elif data(dahan) == 'tipe_identifier':
        # jenis = data(child1(dahan))
        # tipe_native = peta_tipe_data.get(jenis, jenis)
        tipe_native = self.tipe_identifier(dahan)
        if returning:
          kembali += f': {tipe_native}'
        else: 
          self.print(f': {tipe_native}')
      elif data(dahan) == 'declaration_value':
        # ei = child1(dahan)
        # nilai_variable = self.expression_item(ei, returning=True)
        nilai_variable = self.declaration_value(dahan)
        if returning:
          kembali += f' = {nilai_variable}'
        else: 
          self.print(f' = {nilai_variable}')
    return kembali


  def var_declaration(self, tree, returning=True):
    """
    $str="not a number"
    var_declaration
      declaration_name        str
      declaration_value
        expression_item
          literal
            literal_string    not a number
    $str:s="not a number"
    var_declaration
      declaration_name        str
      tipe_identifier
        string
      declaration_value
        expression_item
          literal
            literal_string    not a number
    var_declaration: "$" declaration_config? declaration_name tipe_identifier? declaration_value?
    """
    kembali = ''
    for dahan in anak(tree):
      if data(dahan) == 'declaration_config':
        pass
      elif data(dahan) == 'declaration_name':
        declaration_name = token(dahan)
        if returning:
          kembali += declaration_name
        else: 
          self.print(declaration_name)
      elif data(dahan) == 'tipe_identifier':
        pass
        # jenis = data(child1(dahan))
        # tipe_native = peta_tipe_data.get(jenis, jenis)
        # if returning:
        #   kembali += f': {tipe_native}'
        # else: 
        #   self.print(f': {tipe_native}')
      elif data(dahan) == 'declaration_value':
        ei = child1(dahan)
        if data(ei) == 'expression_item':
          nilai_variable = self.expression_item(ei, returning=True)
          if returning:
            kembali += f' = {nilai_variable}'
          else: 
            self.print(f' = {nilai_variable}')
        elif data(ei) == 'instantiation_expression':
          '''
          $c=*MyClass()
          '''
          # print('instantiation_expression #1')
          hasil = self.instantiation_expression(ei, returning=True)
          # print('instantiation_expression #2')
          hasil = ' = ' + hasil # nama = hasil
          if returning:
            kembali += hasil
          else: 
            self.print(hasil)


  def return_statement(self, item, returning=True):
    if returning:
      kembali = f'return '
    else:
      self.print(f'return ') # plus space

    # expression_item
    expritem = child1(item)
    if data(expritem) == 'expression_item':
      jika_mintaresult = self.expression_item(expritem, returning=returning)
      if returning:
        kembali += jika_mintaresult

    if returning:
      return kembali


  def assignment_statement(self, tree, returning=True):
    kembali = ''
    lhs, rhs = '',''
    for item in anak(tree):
      if data(item) == 'nama_identifier':
        lhs = token(item)
      elif data(item) == 'instantiation_expression':
        rhs = self.instantiation_expression(item, returning=True)
      elif data(item) == 'expression_item':
        rhs = self.expression_item(item)
    kembali += f'{lhs} = {rhs}'
    return kembali


  def stdout_operation(self, tree):
    """
    ?+
    stdout_operation
      penanda
      console_log
        expression_item
          literal
            literal_string    hello
    """
    for item in anak(tree):
      # kita iterate utk antisipasi masa depan mau tambah child = config etc
      # misa utk print logger, DebugOutputString dst.
      if data(item) == 'console_log':
        ei = child1(item)
        nilai = self.expression_item(ei, returning=True)
        return f'print({nilai})'


  def object_content(self, tree):
    """
    object_content
      nama_identifier satu
      tipe_identifier
        string
    object_content
      nama_identifier dua
      tipe_identifier
        integer
    """
    nama, jenis = '', ''
    for item in anak(tree):
      if data(item) == 'nama_identifier':
        nama = token(item)
      elif data(item) == 'tipe_identifier':
        jenis = self.tipe_identifier(item)
    return f'{nama}: {jenis}' + ';' # perlu ; atau , ?


  def object_type(self, tree):
    """
    object_type
      object_contents
        object_content
          nama_identifier satu
          tipe_identifier
            string
        statement_separator
        object_content
          nama_identifier dua
          tipe_identifier
            integer
    /ts/&&mytype={}
    /ts/&&mytype={satu:s;dua:i}
    /ts/@@mytype{satu:s|dua:i}
    """
    if not beranak(tree):
      return '{}'
    object_contents = child1(tree)
    contents = []
    for item in anak(object_contents):
      # ingat ada juga content = statement_separator
      if data(item) == 'object_content':
        buah = self.object_content(item)
        contents.append(buah)

    kembali = '\n'.join(contents)
    self.inc()
    kembali = self.tabify_content(kembali)
    self.dec()
    kembali = '{\n' + kembali + '\n}'
    return kembali


  def tipe_data_semua(self, tree):
    """
    tipe_data_semua: tipe_data_builtin
      | tipe_data_collection
      | tipe_data_fungsi
      | tipe_data_buatan
    tipe_data_semua
      array
        item_type
          string    
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'array':
        kembali = self.tipe_identifier_array(item)
      elif data(item) == 'object_type':
        kembali = self.object_type(item)
      else:
        jenis = data(item)
        kembali = peta_tipe_data.get(jenis, jenis)
    return kembali


  def typealias_declaration(self, tree):
    """
      typealias_declaration
        typealias_keyword
        nama_identifier mytypename
        tipe_data_semua
    /ts/&&mynewtype = As
    """
    kembali = ''
    kw, nama, nilai = '', '', ''
    for item in anak(tree):
      if data(item) == 'typealias_keyword':
        kw = 'type'
      elif data(item) == 'nama_identifier':
        nama = token(item)
      elif data(item) == 'tipe_data_semua':
        nilai = self.tipe_data_semua(item)
    kembali = f'{kw} {nama} = {nilai}'
    return kembali


  def file_operation(self, tree):
    """
    file_operation
      penanda
      json_out
        expression_item
          nama_identifier       out
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'json_out':
        ei = child1(item)
        hasil = self.expression_item(ei, returning=True)
        kembali = f'JSON.stringify({hasil})'
      elif data(item) == 'json_in':
        ei = child1(item)
        hasil = self.expression_item(ei, returning=True)
        kembali = f'JSON.parse({hasil})'
    # print('kembali file/json operation:', kembali)
    return kembali


  def array_map(self, tree):
    """
    map
      anonymous_function
        function_param
        anon_statements
          statement_item
            single_statement
              stdout_operation
                penanda
                console_log
                  expression_item
                    literal
                      literal_string  hello
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'anonymous_function':
        kembali = self.anonymous_function(item)
    return kembali


  def array_operation(self, tree):
    """
    data_operation
      array_operation
        penanda
        map
    /py/iden?AM#(){?+'hello'}
    """
    kembali = ''
    for item in anak(tree):
      '''
      array_filter, array_reduce
      '''
      if data(item) == 'penanda':
        pass
      elif data(item) == 'array_map':
        kembali = self.array_map(item)
        kembali['operation'] = 'map'
      elif data(item) == 'array_filter':
        kembali = self.array_map(item) # sementara belum array_filter
        kembali['operation'] = 'filter'
      elif data(item) == 'array_reduce':
        kembali = self.array_map(item) # sementara belum array_reduce
        kembali['operation'] = 'reduce'
    return kembali


  def data_operation(self, tree):
    """
    data_operation
      file_operation
        penanda
        json_out
          expression_item
            nama_identifier       out
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'file_operation':
        kembali = self.file_operation(item)
        kembali = {
          'type': 'file_operation',
          'result': kembali
        }
      elif data(item) == 'array_operation':
        kembali = self.array_operation(item)
        kembali['type'] = 'array_operation'
    return kembali


  def dataops_statement(self, tree):
    """
    dataops_statement
      data_operation
        file_operation
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'data_operation':
        kembali = self.data_operation(item)
    return kembali


  def dataops_statement_with_identifier(self, tree):
    """
    /ts/mydata?Fj>out
    dataops_statement_with_identifier
      nama_identifier mydata
      dataops_statement
        data_operation
          file_operation
            penanda
            json_out
              expression_item
                nama_identifier       out
    """
    identifier, rhs = '', ''
    for item in anak(tree):
      if data(item) == 'nama_identifier':
        identifier = token(item)
      elif data(item) == 'dataops_statement':
        rhs = self.dataops_statement(item)


    if isinstance(rhs, dict):
      '''
      kembalian anon func: dict berisi internal dan external
      '''
      if rhs['type'] == 'array_operation':
        operasi = rhs['operation']
        if rhs['external']:
          kembali = f"{rhs['external']}\n{operasi}({rhs['internal']}, {identifier})"
        else:
          kembali = f"{operasi}({rhs['internal']}, {identifier})"
      elif rhs['type'] == 'file_operation':
        kembali = f'const {identifier} = {rhs["result"]}'

    return kembali
    # return f'const {identifier} = {rhs};'


  def faker_args(self, tree):
    """
    faker_args
      fake_arg      0
      fake_arg      100
    """
    args = []
    for item in anak(tree):
      if data(item) == 'fake_arg':
        hasil = token(item)
        if hasil.isdigit():
          hasil = int(hasil)
        args.append(hasil)
    # return ', '.join(args)
    return args # biar *args


  def faker_ops(self, tree):
    """
    faker_ops
      penanda
      faker_num       10
      faker_cmd       random_int
      faker_args
        fake_arg      0
        fake_arg      100
      as_list
    faker_ops
      penanda
      faker_num       10
      faker_cmd       random_int
      faker_args
        fake_arg      0
        fake_arg      100
    /py/?K10/random_int(0,100)/A
    """
    kembali = ''
    as_list, as_string = True, False
    funcname, funcargs, callnum = '','',1

    # print('#1')
    for item in anak(tree):
      if data(item) == 'penanda':
        pass
      elif data(item) == 'faker_num':
        callnum = int(token(item))
      elif data(item) == 'faker_cmd':
        funcname = token(item)
      elif data(item) == 'faker_args':
        funcargs = self.faker_args(item)
      elif data(item) == 'as_list':
        as_list = True
      elif data(item) == 'as_string':
        as_string = True
    # print('#2, args:', funcargs)
    from schnell.langs.data.fakesey import palsu
    faker = palsu.faker
    hasil = []
    # print('#3, func', funcname)
    for i in range(callnum):
      # print('\ti:', i)
      if funcargs:
        ok = getattr(faker, funcname)(*funcargs)
        # print('\t\tok:', ok)
      else:
        ok = getattr(faker, funcname)()
      
      if isinstance(ok, int):
        ok = str(ok)
      elif isinstance(ok, list):
        ok = str(ok)
      elif isinstance(ok, str):
        ok = '"' + ok + '"'
      # print('adding ok:', ok)
      hasil.append(ok)
    if as_string:
      return ', '.join(hasil)
    return '[' + ', '.join(hasil) + ']'


  def fmus_run(self, program):
    fmus = Fmus(env_int('ULIBPY_FMUS_DEBUG'))
    # fmus.set_file_dir_template(filepath)
    # fmus.set_file_template(filepath)
    # fmus.set_dir_template_from_file(filepath)
    fmus.process(program, capture_outerr=True)
    if '$*' in program:
      tidur(ms=ULIBPY_STDOUT_CAPTURE_SLEEP_MS)
      if fmus.stdout or fmus.stderr:
        self.output = fmus.stdout if fmus.stdout else fmus.stderr


  def fmus_cmd(self, tree):
    """
    fmus_cmd
      fmus_execute  $*code /tmp
    fmus_cmd
      fmus_new
        fmus_new_basedir    /tmp/whatever
    fmus_cmd
      fmus_new
        fmus_new_filename   myfile.txt
    fmus_cmd
      fmus_new
        fmus_new_filepath   /tmp/hapus/myfile.txt
    """
    code = ''
    filepath = joiner(tempdir(), new_filename_timestamp())
    
    for item in anak(tree):
      if data(item) == 'fmus_execute':
        code = token(item)
        program = code + '\n'
        # print('executing program:', program)
        self.fmus_run(program)
        # print('selesai')
      elif data(item) == 'fmus_new':
        for basefile in anak(item):
          if data(item) == 'fmus_new_basedir':
            basedir = token(item)
            filepath = joiner(basedir, new_filename_timestamp())
          elif data(item) == 'fmus_new_filename':
            filename = token(item)
            filepath = joiner(tempdir(), filename)
          elif data(item) == 'fmus_new_filepath':
            filepath = token(item)
        # pastikan filepath ada dan basedir terbuat
        program = editor(filepath)
        program = program + '\n'
        print('************')
        print(program)
        print('************')
        self.fmus_run(program)
    return filepath # sementara...harusnya showtext/file utk coding


  def fmus_ops(self, tree):
    """
    fmus_ops
      fmus_keyword
      fmus_cmd
        fmus_execute  $*code /tmp
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'fmus_keyword':
        pass
      elif data(item) == 'fmus_cmd':
        kembali += self.fmus_cmd(item)
    return kembali


  def redis_args(self, tree):
    """
    redis_args
      redis_arg
        redis_key   monyong
    """
    redis_arg = child1(tree)
    # kembali = ''
    args = []
    for item in anak(redis_arg):
      if data(item) == 'redis_key':
        hasil = token(item)
        args.append(hasil)
      elif data(item) == 'redis_value':
        # sementara value masih string
        # nanti bisa: dict, list, set
        hasil = token(item)
        args.append(hasil)

    kembali = args
    return kembali


  def redis_operation(self, tree):
    """    
    """
    from schnell.app.transpiler.zgenerate.helper.redis_helper import redis_process
    kembali = ''
    cmd, thing = '', ''
    args = []
    for item in anak(tree):
      if data(item) == 'penanda':
        pass
      elif data(item) == 'redis_string_get':
        cmd = 'get'
      elif data(item) == 'redis_string_add':
        cmd = 'set'
      elif data(item) == 'redis_keys':
        cmd = 'list'
      elif data(item) == 'redis_key':
        thing = token(item)
        args.append(thing)
      elif data(item) == 'redis_value':
        thing = token(item)
        args.append(thing)
      elif data(item) == 'redis_args':
        args = self.redis_args(item)
    
    hasil = redis_process(cmd, args)
    print(f'redis_process({cmd}, {args})', hasil)
    if isinstance(hasil, list):
      hasil = [item.decode('utf8') for item in hasil]
      print_enumerate(hasil)
      kembali = '\n'.join(hasil)
    elif isinstance(hasil, str):
      kembali = hasil
    elif isinstance(hasil, bytes):
      kembali = hasil.decode('utf8')
    else:
      print('result:', type(hasil))      
    return kembali


  def single_statement(self, jenisstmt, returning=True):
    """
    """
    item = child1(jenisstmt)
    if item.data == 'return_statement':
      jika_mintaresult = self.return_statement(item, returning=returning)
      if returning:
        return jika_mintaresult
    elif item.data == 'var_declaration':
      jika_mintaresult = self.var_declaration(item, returning=returning)
      if returning:
        return jika_mintaresult
    elif item.data == 'const_declaration':
      jika_mintaresult = self.const_declaration(item, returning=returning)
      if returning:
        return jika_mintaresult
    elif item.data == 'assignment_statement':
      jika_mintaresult = self.assignment_statement(item, returning=returning)
      if returning:
        return jika_mintaresult
    elif item.data == 'stdout_operation':
      hasil = self.stdout_operation(item)
      if returning:
        return hasil
      self.print(hasil)
    elif item.data == 'typealias_declaration':
      hasil = self.typealias_declaration(item)
      if returning:
        return hasil
    elif item.data == 'faker_ops':
      hasil = self.faker_ops(item)
      if returning:
        return hasil
      self.print(hasil)
    elif item.data == 'fmus_ops':
      hasil = self.fmus_ops(item)
      if returning:
        return hasil
      self.print(hasil)
    elif item.data == 'redis_operation':
      hasil = self.redis_operation(item)
      if returning:
        return hasil
      self.print(hasil)
    elif item.data == 'dataops_statement_with_identifier':
      hasil = self.dataops_statement_with_identifier(item)
      if returning:
        return hasil
      self.print(hasil)


  def instantiation_expression(self, tree, returning=True):
    """
    instantiation_expression
      new_operator
      nama_identifier     MyClass
      function_call_param
    """
    kembali = ''
    for item in anak(tree):
      if data(item) == 'new_operator':
        pass
      elif data(item) == 'nama_identifier':
        kembali += token(item)
      elif data(item) == 'function_call_param':
        hasil = self.function_call_param(item, returning=returning)
        kembali += hasil
    if returning:
      return kembali
    self.print(kembali)


  def named_value(self, tree):
    """
    named_value
      nama_identifier   username
      tipe_identifier
        string
      nilai_identifier
        expression_item
          literal
            literal_string      wieke
    """
    nama, jenis, nilai = '', '', ''
    for item in anak(tree):          
      if data(item) == 'nama_identifier':
        nama = token(item)
      elif data(item) == 'tipe_identifier':
        jenis = chdata(item) # python gak pake type sementara
      elif data(item) == 'nilai_identifier':
        ei = child1(item)
        nilai = self.expression_item(ei, returning=True)
    return nama, jenis, nilai


  def named_values(self, tree):
    """
    named_values
      named_value
        nama_identifier   username
        tipe_identifier
          string
        nilai_identifier
          expression_item
            literal
              literal_string      wieke

    # print('param named_values')
    for kv in namaid.children:
      # named_value = kv
      namaidentifier = str(kv.children[0].children[0])
      nilaiidentifier = kv.children[1]
      ei = nilaiidentifier.children[0]
      lit = ei.children[0]
      nilaiidentifierstr = self.literal(lit)
    actualargs.append(f'{namaidentifier}={nilaiidentifierstr}')
    """
    # username=some,password=some
    args = []
    for nv in anak(tree):
      if data(nv) == 'named_value':
        nama, _, nilai = self.named_value(nv)
        args.append(f'{nama}={nilai}')
    return ', '.join(args)


  def function_call_param(self, funcparam, add_self=False, returning=True):
    """
    function_param utk deklarasi/definisi fungsi
    function_call_param utk pemanggilan fungsi/method/constructor

    function_call_param
      callparamlist
        callparam
          literal
            literal_string        hello
    instantiation_expression
      new_operator
      nama_identifier     MyClass
      function_call_param

    """
    if not beranak(funcparam):
      return '()'
    
    # function_call_param hanya punya 1 anak
    # callparamlist
    funcparamlist = child1(funcparam)
    if anak(funcparamlist):
      actualargs = []
      # print('iterate funcparamlist.children:', funcparamlist.children)
      for param in funcparamlist.children:
        # callparam
        # print('func call param:', param)
        # nama_identifier or named_values
        if not param.children:
          continue
        namaid = param.children[0]
        if namaid.data == 'nama_identifier':
          # print('param nama_identifier')
          argid = str(namaid.children[0])
          actualargs.append(argid)
        elif namaid.data == 'named_values':
          # print('param named_values')
          for kv in namaid.children:
            # named_value = kv
            # namaidentifier = str(kv.children[0].children[0])
            # nilaiidentifier = kv.children[1]
            # ei = nilaiidentifier.children[0]
            # lit = ei.children[0]
            # nilaiidentifierstr = self.literal(lit)
            namaidentifier, _, nilaiidentifierstr = self.named_value(kv)
            actualargs.append(f'{namaidentifier}={nilaiidentifierstr}')
        elif namaid.data == 'literal':
          hasil = self.literal(namaid)
          actualargs.append(hasil)

      the_params = ", ".join(actualargs)
      if add_self:
        if the_params:
          the_params = 'self, ' + the_params
        else:
          the_params = 'self'
      result = f'({the_params})'
      if returning:
        return result
      self.output += result
    else:
      result = f'({"self" if add_self else ""})'
      if returning:
        return result
      self.output += result


  def for_start(self, tree):
    """
    for_start
      key_name  i
      expression_item
        literal
          literal_number        0
    """
    keyname = token(child1(tree))
    range_start_value = self.expression_item(child2(tree), returning=True)
    return keyname, range_start_value


  def for_end(self, forend):
    """
    for_end
      expression_item
        relational_expression
          expression_item
            nama_identifier     i
          operator_less
          expression_item
            literal
              literal_number    5
    """
    # for (...; i<5; ...)
    # manual handle relational_expression
    ei = child1(forend)
    relation = child1(ei)
    kiri = child1(relation)
    kiri = self.expression_item(kiri, returning=True)
    # kiri gak penting
    oper = child2(relation)
    kanan = child3(relation)
    kanan = self.expression_item(kanan, returning=True)
    # sementara gak handle > dan >= utk for x in range(...; forend)
    # print(f'forend, range oper {oper}, end {kanan}')
    if data(oper) == 'operator_less':
      return kanan
    elif data(oper) == 'operator_less_equal':
      return kanan-1
    return 0


  def for_traditional(self, tree):
    """
    for_traditional
      for_start
      for_end
      for_step
        expression_item
          post_inc_expression
            expression_item
              nama_identifier     i
    for i in range(start, <end, step)
    """
    forstart = child1(tree)
    keyname, range_start = self.for_start(forstart)
    # for keyname in range(range_start, end, step):
    forend = child2(tree)
    range_end = self.for_end(forend)

    # sementara kita skip dulu step: range(start, end, step)
    forstep = None
    if jumlahanak(tree)>2:
      '''
      for_step
        expression_item
          post_inc_expression
            expression_item
              nama_identifier     i
      '''
      forstep1 = child3(tree)
      ei = child1(forstep1)
      anakei = child1(ei)      
      if data(anakei) == 'pre_inc_expression':
        # ++i
        forstep = None
      elif data(anakei) == 'post_inc_expression':
        # i++
        forstep = None
      elif data(anakei) == 'literal':
        forstep = self.expression_item(ei, returning=True)
    # forstep = 'ini stepper di awal atau diakhir bergantung ++i atau i++'

    if not forstep:
      return f"{keyname} in range({range_start}, {range_end}):\n"
    else:
      return f"{keyname} in range({range_start}, {range_end}, {forstep}):\n"


  def for_each(self, tree):
    """
    "@" for_each "@"  // for@item/items/index@
    for_each: item_name "/" array_name ("/" key_name)?
    for_each
      item_name   item
      array_name  items
    """
    item = token(child1(tree))
    items = token(child2(tree))
    if anak(tree)==3:
      index = token(child3(tree))
      return f"{index}, {item} in enumerate({items})"
    return f"index, {item} in enumerate({items})"


  def for_in(self, tree):
    """
    "#" for_in "#"    // for#key/items#
    for_in: key_name "/" array_name
    """
    index = token(child1(tree))
    items = token(child2(tree))
    return f"{index}, _ in enumerate({items})"


  def for_of(self, tree):
    thing, things = '',''
    for item in anak(tree):
      if data(item) == 'item_name':
        nama_jenis_identifier_optional = child1(item)
        thing = self.nama_jenis_identifier_optional(nama_jenis_identifier_optional)
      elif data(item) == 'array_name':
        for cucu in anak(item):
          if data(cucu) == 'nama_identifier':
            things = chtoken(item)
          elif data(cucu) == 'expression_item':
            things = self.expression_item(cucu)
    return f"(const {thing} of {things})"


  def for_variation(self, tree):
    """
    returning value instead of self.output += ...

    for_variation
      for_traditional
      for_each = for k,v
      for_in = for_key
      for_of = for_value

    for index,item in enumerate(items): ...
    -> index,item in enumerate(items): ...
    """
    varian = child1(tree)
    if data(varian) == 'for_traditional':
      # hasil = self.for_traditional(varian)
      # self.output += hasil
      return self.for_traditional(varian)
    elif data(varian) == 'for_each':
      return self.for_each(varian)
    elif data(varian) == 'for_in':
      return self.for_in(varian)
    elif data(varian) == 'for_of':
      return self.for_of(varian)

    return ''


  def condition_for(self, tree):
    """
    returning value instead of self.output += ...

    condition_for
      expression_item
        literal
          literal_number      42
    condition_for
      for_variation
    """
    ei = child1(tree)
    if data(ei) == 'expression_item':
      return self.expression_item(ei, returning=True)
    elif data(ei) == 'for_variation':
      return self.for_variation(ei)

    return ''


  def condition_body(self, tree, returning=True):
    """
    condition_body
      statement_list
    """
    if beranak(tree):
      sl = child1(tree)
      jika_mintaresult = self.statement_list(sl, returning=returning)
      if returning:
        return jika_mintaresult
    else:
      '''
      for@item/items@{}

      utk empty for
      asumsikan ini berlaku utk selain for: switch dll
      '''
      # if data(bapak(tree)) == 'for_statement':
      #   '''
      #   sudah ada "for" tambah ":\n"
      #   '''
      if returning:
        return ':\n' + f'{self.tab()}pass'
      else:
        self.print(':\n' + f'{self.tab()}pass')


  def for_statement(self, tree, returning=True):
    """
    for_statement
      for_keyword
      condition_for
      condition_body

    for(){}
    for@@{}
    for##{}
    for$${}
    """
    forkeyword = child1(tree)
    if returning:
      kembali = 'for'
    else:
      self.print('for')
    condition_for = child2(tree)
    header = self.condition_for(condition_for)
    if returning:
      kembali += ' ' + header
      kembali += ':\n'
    else:
      self.print(' ' + header)
      self.print(':\n')

    self.inc()
    condition_body = child3(tree)
    jika_mintaresult = self.condition_body(condition_body, returning=returning)
    if returning:
      return kembali + jika_mintaresult
    self.dec()


  def if_statement(self, tree, returning=True):
    """
    if_statement
      if_keyword
      condition_then_if
        condition_if
          expression_item
            literal
              literal_number    42
        condition_body
          statement_list
            statement_item
              expression_item
                literal
                  literal_string        ini if
    if (if)/elif/ /elif/(else)
    """
    ifkeyword = child1(tree)
    kembali = '' # digunakan hanya jk returning
    self.inc()
    condition_then_if = child2(tree)
    condition_if = child1(condition_then_if)
    condition_body = child2(condition_then_if)
    if data(condition_if) == 'condition_if':
      ei = child1(condition_if)
      kembalikan_ekspresi = self.expression_item(ei, returning=True)
      if returning:
        kembali += f'if {kembalikan_ekspresi}:\n'
      else:
        self.output += f'if {kembalikan_ekspresi}:\n'

    jika_mintaresult = self.condition_body(condition_body, returning=returning)    
    self.dec() # kurangi indent dulu
    if returning:
      return kembali + jika_mintaresult


  def condition_while(self, condition_while):
    """
    condition_while
      expression_item
        relational_expression
          expression_item
            nama_identifier   i
          operator_less
          expression_item
            literal
              literal_number  2
    """
    ei = child1(condition_while)
    hasil = self.expression_item(ei, returning=True)
    return hasil


  def while_statement(self, tree, returning=True):
    """
    while_statement
      while_keyword
      condition_while
      condition_body
        statement_list
          statement_item
            expression_item
              function_call
                function_name   print
                argument_list
                  argument
                    expression_item
                      literal
                        literal_string  Hello
          statement_separator
          statement_item
            expression_item
              function_call
                function_name   print
    """
    whilekw = child1(tree)
    condition_while = child2(tree)
    hasil = self.condition_while(condition_while)
    if returning:
      kembali = f'while {hasil}:\n'
    else:
      self.output += f'while {hasil}:\n'
    self.inc()
    condition_body = child3(tree)
    jika_mintaresult = self.condition_body(condition_body, returning=returning)
    self.dec()
    if returning:
      return kembali + jika_mintaresult


  def condition_switch(self, tree):
    """
    condition_switch
      expression_item
        nama_identifier       myvalue
    """
    ei = child1(tree)
    hasil = self.expression_item(ei, returning=True)
    return hasil


  def case_body(self, tree, terbanding, first_case=False, returning=True):
    """
    first_case => if, otherwise: elif
    case_body
      
      condition_case
        expression_item
          literal
            literal_number    42
      -- or
      condition_defaultcase

      condition_body
        statement_list
          statement_item
            expression_item
              function_call
                function_name print
                argument_list
                  argument
                    expression_item
                      literal
                        literal_string        asyik
    s(myvalue)(42){print("asyik")}(43){print("dapat 43")}(){print("default")}
    """
    condition_case = child1(tree)
    
    if data(condition_case) == 'condition_defaultcase':
      # elif_keyword = 'default'
      header = f"else:\n"
    elif data(condition_case) == 'condition_case':
      # elif_keyword = 'elif'
      if_or_elif = "if" if first_case else "elif"
      ei = child1(condition_case)
      membanding = self.expression_item(ei, returning=True)    
      header = f"{if_or_elif} {terbanding} == {membanding}:\n"

    if returning:
      kembali = header
    else:
      self.output += header
    condition_body = child2(tree)
    statement_list = child1(condition_body)
    self.inc()
    jika_mintaresult = self.statement_list(statement_list, returning=returning)
    self.dec()
    
    if returning:
      return kembali + jika_mintaresult + '\n'
    
    self.output += '\n' # agar elif dan else mulai dari newline


  def switch_statement(self, tree, returning=True):
    """
    s(myvalue)(42){print("asyik")}(43){print("dapat 43")}
    """
    swkw = child1(tree)
    terbanding = None
    # condition_switch = child2(tree)
    # if terbanding == nilai ... elif terbanding == nilai ... else ...
    # terbanding = self.condition_switch(condition_switch)
    # case_body = child3(tree)
    # self.case_body(case_body, terbanding)
    
    kembali = '' # dipake utk returning

    first_case = True
    for cond_or_case in anak(tree):
      if data(cond_or_case) == 'condition_switch':
        terbanding = self.condition_switch(cond_or_case)
        # print('terbanding adlh', terbanding)
      elif data(cond_or_case) == 'case_body':        
        kembali += self.case_body(cond_or_case, terbanding, first_case, returning=returning)
        if first_case:
          first_case = False

    if returning:
      return kembali


  def statement_item(self, contentitem, returning=True):
    jenisstmt = child1(contentitem)
    if jenisstmt.data == 'single_statement':
      jika_mintaresult = self.single_statement(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'instantiation_expression':
      jika_mintaresult = self.instantiation_expression(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'for_statement':
      jika_mintaresult = self.for_statement(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'if_statement':
      jika_mintaresult = self.if_statement(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'expression_item':
      jika_mintaresult = self.expression_item(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'while_statement':
      jika_mintaresult = self.while_statement(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'switch_statement':
      jika_mintaresult = self.switch_statement(jenisstmt, returning=returning)
      if returning:
        return jika_mintaresult
    elif jenisstmt.data == 'enum_declaration':
      jika_mintaresult = self.enum_declaration(jenisstmt)
      if returning:
        return jika_mintaresult
      self.print(jika_mintaresult)


  def statement_list(self, tree, returning=True):
    """
    statement_list
      statement_item
        expression_item
          literal
            literal_string  hello
      statement_separator
      statement_item
        if_statement
          if_keyword
          condition_then_if
            condition_if
              expression_item
                literal
                  literal_number    42
            condition_body
              statement_list
                statement_item
                  expression_item
                    literal
                      literal_string        ini if
    """
    for stmt in anak(tree):
      if data(stmt) == 'statement_item':
        jika_mintaresult = self.statement_item(stmt, returning=returning)
        if returning:
          return jika_mintaresult
      elif data(stmt) == 'statement_separator':
        if returning:
          return '\n'
        self.output += '\n'


  def functioncontent(self, tree):
    """
    functioncontent
      statement_item
        expression_item
          arithmetic_expression
            expression_item
              arithmetic_expression
                expression_item
                  nama_identifier a
                operator_plus
                expression_item
                  nama_identifier b
            operator_mult
            expression_item
              literal
                literal_number    10
    """
    # print('func content:', tree)
    direct_child = child1(tree)
    if data(direct_child) == 'statement_item':
      hasil = self.statement_item(direct_child, returning=True)
      # print('hasil statement item:', statement_item)
      return hasil


  def functioncontentlist(self, tree):
    """
    functioncontentlist
      functioncontent
        statement_item
          expression_item
            arithmetic_expression
              expression_item
                arithmetic_expression
                  expression_item
                    nama_identifier a
                  operator_plus
                  expression_item
                    nama_identifier b
              operator_mult
              expression_item
                literal
                  literal_number    10
    """
    allcontent = []
    for item in anak(tree):
      hasil = self.functioncontent(item)
      if hasil:
        allcontent.append(hasil)
    # print('allcontent sblm ditabify', allcontent)
    tabify = [self.tab() + item for item in allcontent]
    pemisah_content = '\n'
    return pemisah_content.join(tabify)


  def function_content(self, funccontent, returning=True):
    """
    foo(){}
    function_item
      function_name     foo
      function_param
      function_content
    """
    
    kembali = '' # digunakan oleh returning
    if beranak(funccontent):
      # functioncontentlist
      functioncontentlist = child1(funccontent)
      hasil = self.functioncontentlist(functioncontentlist)
      if hasil:
        return hasil
      else:
        # f(){} empty funcbody
        if returning:
          return kembali + self.empty_content
        else:
          self.output += self.empty_content
    else:
      if returning:
        return kembali + self.empty_content
      else:
        self.output += self.empty_content


  def function_param(self, funcparam, add_self=False, returning=True):
    """
    utk method/ctor: add_self=True
    utk function call, class instantiation (memanggil ctor): function_call=True

    standalone spt ini gak punya anak
    function_param
    """
    # end_with_colon = "" if function_call else ":"

    if beranak(funcparam):
      # paramlist
      funcparamlist = child1(funcparam)
      actualargs = self.paramlist(funcparamlist)
      the_params = ", ".join(actualargs)
      if returning:
        return f'({the_params})'
      else:
        self.output += f'({the_params})'

    else:
      if returning:
        return f'({"self" if add_self else ""})'
      else:
        self.output += f'({"self" if add_self else ""})'


  def anon_expression(self, tree):
    """
    anon_expression
      expression_item
        arithmetic_expression
          expression_item
            nama_identifier   x
          operator_mult
          expression_item
            literal
              literal_number  2
    """
    return self.expression_item(child1(tree), returning=True)


  def anon_statements(self, tree):
    """
    returning by default True krn kita pengen apit ini dg {}

    anon_statements
      statement_item
        single_statement
          return_statement
            expression_item
              arithmetic_expression
                expression_item
                  nama_identifier     x
                operator_mult
                expression_item
                  literal
                    literal_number    2
    di sini sengaja kembalikan list
    agar pemanggil tau apa hrs gunakan {} atau tidak
    jk hanya ada 1 statement maka tidak perlu {}
    jk 0 atau lebih dari 1 maka gunakan {} utk mengapit
    """
    statement_list = []
    # statement_item = child1(tree)
    # hasil = self.statement_item(statement_item, returning=True)
    for statement in anak(tree):
      # print('statement x:', statement.pretty())
      if data(statement) == 'statement_item':
        # skip statement_separator
        hasil = self.statement_item(statement, returning=True)
        hasil = str(hasil) # si -> ei -> suka hasilkan number
        statement_list.append(hasil)

    # print('peroleh statement_list:', statement_list)
    return statement_list


  def anonymous_function(self, tree):
    """
    argument
      anonymous_function
        non_arrow_func
          keyword_function
        function_param
          paramlist
            param
              nama_identifier     x
        anon_expression
          ...
        * atau
        anon_statements
          ...
    non_arrow_func + function_param + anon_expression|anon_statements
    """
    # harus ada mode: arrow func atau normal func
    # default adlh arrow func
    # print('oprek anon func utk', tree.pretty())
    # arrow_func_mode = True
    # arrow_uses_expression = True
    kembali = ''
    if jumlahanak(tree) == 3:
      # normal func
      # oprek_config = child1(tree)
      # arrow_func_mode = False
      oprek_param = child2(tree)
      # print('anon func: normal func, oprek_param:', oprek_param)
      params = self.function_param(oprek_param, returning=True)
      # print('anon func: normal func, params:', params)
      oprek_body = child3(tree)
      if data(oprek_body) == 'anon_expression':
        hasil = self.anon_expression(oprek_body)
        # print('found expr:', hasil)
        # self.print(f'function {params} {{\n')
        # self.print(self.tab() + hasil)
        # self.print('\n}')
        kembali += f'function {params} {{' + hasil + '\n}'
      elif data(oprek_body) == 'anon_statements':
        # self.print(f'function {params} {{')
        # print('pre stmt body')
        badan_fungsi = self.anon_statements(oprek_body)
        badan_fungsi = '\n'.join(badan_fungsi)
        kembali += f'function {params} {{' + badan_fungsi + '\n}'
    else:
      # default/arrow func, gak perlu {} utk anon expr dan anon stats yg cuma 1 child
      # print('sblm function_param, child anon func #1')
      oprek_param = child1(tree)
      params = self.function_param(oprek_param, returning=True)
      # print('sblm body anon expr/stmt, child anon func #2')
      oprek_body = child2(tree)
      if data(oprek_body) == 'anon_expression':
        # print('hajar anon expressions')
        hasil = self.anon_expression(oprek_body)
        # self.print(f'{params} => {hasil}')
        kembali += f'{params} => {hasil}'
      elif data(oprek_body) == 'anon_statements':
        '''
        arrow.map(42, (x){x*2; y*5})
        '''
        # print('hajar anon statements')
        # self.print(f'{params} => {{')
        badan_fungsi = self.anon_statements(oprek_body)
        # print('badan_fungsi:', badan_fungsi)
        # cek jumlah statement dlm badan_fungsi
        if len(badan_fungsi) == 1:
          konten = badan_fungsi[0]
        else:
          # mungkin perlu self.tab() stlh \n
          # yup, bahkan perlu ;
          self.inc() # berlaku sblm panggil self.tab()
          badan_fungsi = [self.tab() + item + ';' for item in badan_fungsi]
          transform = '\n'.join(badan_fungsi)
          self.dec()
          konten = '{\n' + transform + '\n}'
        kembali += f'{params} => ' + konten

    return kembali


  def argument_list(self, tree):
    """
    argument_list
      argument
        named_values
          named_value
            nama_identifier   username
            tipe_identifier
              string
            nilai_identifier
              expression_item
                literal
                  literal_string      wieke
    """
    args = []
    for arg in anak(tree):
      # argument
      for tipearg in anak(arg):
        if data(tipearg) == 'named_values':
          # print('named_values #1')
          hasil = self.named_values(tipearg)
          # print('named_values #2', hasil)
          args.append(hasil)
        elif data(tipearg) == 'expression_item':
          hasil = self.expression_item(tipearg, returning=True)
          hasil = str(hasil)
          args.append(hasil)
        elif data(tipearg) == 'anonymous_function':
          hasil = self.anonymous_function(tipearg)
          args.append(hasil)
    
    # kembalikan list
    return args


  def function_call(self, tree):
    """
    function_call
      function_name print
      argument_list
        argument
          expression_item
            literal
              literal_number        1
        argument
          expression_item
            literal
              literal_number        2
    function_call
      function_name     print
      argument_list
        argument
          expression_item
            literal
              literal_string        hello
    function_call
      function_name             print
    function_call
      function_name
        nama_identifier_with_typeparams
          nama_identifier       MyClass
    """
    functionname, callparams = '', '()'
    for item in anak(tree):
      if data(item) == 'function_name':
        funcname = item # child1(tree)
        # funcname mesti beranak, apakah nama atau tree
        anak_nama_fungsi = child1(funcname)
        if istoken(anak_nama_fungsi):
          functionname = token(funcname)
        elif data(anak_nama_fungsi) == 'nama_identifier_with_typeparams':
          functionname = self.nama_identifier_with_typeparams(anak_nama_fungsi)
      elif data(item) == 'argument_list':
        argument_list = item # child2(tree)
        args = self.argument_list(argument_list)
        callparams = f'({", ".join(args)})'

    return self.tab() + f'{functionname}{callparams}'


  def function_name(self, tree):
    """
    function_name
      nama_identifier_with_typeparams
        nama_identifier       myfunc
    function_name: nama_identifier_with_typeparams
    """
    nama_identifier_with_typeparams = child1(tree)
    name = self.nama_identifier_with_typeparams(nama_identifier_with_typeparams)
    return name


  def function_item(self, cucu, returning=True):
    '''
    f:foo(){}
    selalu ada function_param ()
    dan function_content {}

    function_item
      keyword_function
      function_name     foo
      function_param
      function_content

    function_item
      function_name     foo
      function_param
        paramlist
          *
          param
            nama_identifier     satu
          param
            nama_identifier     dua
      function_content
        functioncontentlist
          functioncontent
    '''
    self.inc()
    kembali = ''
    for item in anak(cucu):
      if data(item) == 'keyword_function':
        pass
      elif data(item) == 'function_name':
        name = self.function_name(item)
        kembali += 'def ' + name
      elif data(item) == 'function_param':
        param = self.function_param(item, returning=True)
        kembali += param
      elif data(item) == 'function_content':
        content = self.function_content(item, returning=True)
        kembali += '\n' + content

    self.dec()
    kembali += '\nend'

    if returning:
      return kembali
    self.print(kembali)


  def constructor_content(self, ctor_method_field):
    """
    """
    kembali = f'\n{self.tab()}def __init__'
    # self.output += 
    self.inc()
    # function_param
    ctorparam = child1(ctor_method_field)
    kembali += self.function_param(ctorparam, add_self=True, returning=True)
    kembali += ':'
    # function_content
    ctorcontent = child2(ctor_method_field)
    kembali += self.function_content(ctorcontent, returning=True)
    self.dec()
    return kembali


  def method_content(self, tree, structname=None):
    """
    method_content
      function_name
        nama_identifier_with_typeparams
          nama_identifier       len
      function_param
      function_content
    """
    kembali = ''
    for item in anak(tree):
      # print('method content item:', item)
      if data(item) == 'function_name':
        nama_identifier_with_typeparams = child1(item)
        nama = self.nama_identifier_with_typeparams(nama_identifier_with_typeparams)
        
        instance = f'# {structname.lower()}1 = {structname}.new'
        calling = f'# {structname.lower()}1.{nama}'
        kembali += '\n' + self.tab()
        kembali += instance + '\n'
        kembali += self.tab()
        kembali += calling + '\n'
        kembali += self.tab()
        kembali += f'def {nama}'
        # print('peroleh func name:', kembali)
      elif data(item) == 'tipe_identifier':
        # tipe_identifier = self.tipe_identifier(item)
        pass
      elif data(item) == 'function_param':
        # print('mau func param:')
        kembali += self.function_param(item, add_self=True, returning=True)
        # kembali += ':'
        # print('peroleh func param:', kembali)
      elif data(item) == 'function_content':
        kembali += '\n'
        self.inc()
        kembali += self.function_content(item, returning=True)      
        self.dec()
        kembali += '\n' + self.tab() + 'end'
        # print('peroleh func content:', kembali)

    return kembali


  def fieldconfiglist(self, tree):
    """
    fieldconfig: "+" -> public
      | "-" -> private
      | "#" -> protected
      | "ro" -> read_only       // readonly name: string = "world"; hanya assign dlm ctor
      | "%" -> static
    """
    semua_modifier = []
    for nilai in anak(tree):
      if data(nilai) == 'public':
        hasil = 'public'
        semua_modifier.append(hasil)
      elif data(nilai) == 'private':
        hasil = 'private'
        semua_modifier.append(hasil)
      elif data(nilai) == 'protected':
        hasil = 'protected'
        semua_modifier.append(hasil)
      elif data(nilai) == 'read_only':
        hasil = 'readonly'
        semua_modifier.append(hasil)
      elif data(nilai) == 'static':
        pass
    if semua_modifier:
      return ' '.join(semua_modifier) + ' '
    return ''


  def field_content(self, tree):
    """
    field_content
      field_name        username
      tipe_identifier
        string
      declaration_value
        expression_item
          literal
            literal_string      usef
    field_content: 
      field_config? 
      field_name 
      tipe_identifier? 
      declaration_value?
    """
    from .common import ruby_struct_template
    paramlist = []
    paramvalues = {}
    fieldname, field_initialize_value, field_value = '', '', ''
    # default_field_config = 'self.'
    for item in anak(tree):
      if data(item) == 'field_config':
        # masih bermasalah: jk specify #, + dll, self.<nama> jadi hilang utk non-static
        # configlist = child1(item)
        # default_field_config = self.fieldconfiglist(configlist)
        pass
      elif data(item) == 'field_name':
        fieldname = token(item)
        paramlist.append(fieldname)
        field_initialize_value = f'@{fieldname} = {fieldname}'
      elif data(item) == 'tipe_identifier':
        # tipe_native = self.tipe_identifier(item)
        # kembali += f': {tipe_native}'
        pass
      elif data(item) == 'declaration_value':
        field_value = self.declaration_value(item)
        paramvalues[fieldname] = field_value

    __PARAMLIST__ = ', '.join(paramlist)
    fieldinitializer = [f'@{item} = {item}' for item in paramlist]
    __FIELDS_INITIALIZER__ = '\n'.join(fieldinitializer)
    def_initialize = ruby_struct_template \
      .replace('__PARAMLIST__', __PARAMLIST__) \
      .replace('__FIELDS_INITIALIZER__', __FIELDS_INITIALIZER__)
    
    # username, @username = username, 'wieke vlc'
    # return fieldname, field_initialize_value, field_value
    return {fieldname: field_value}


  def classcontent(self, tree, structname=None):
    """
    class_content -> classcontentlist -> classcontent
    classcontentlist
      classcontent
        method_content
          function_name
            nama_identifier_with_typeparams
              nama_identifier       len
          function_param
          function_content
      classcontent
        constructor_content
          function_param
            paramlist
              param
          function_content
            functioncontentlist
              functioncontent
    """
    if not beranak(tree):
      return None, None
    # constructor_content
    ctor_method_field = child1(tree)
    if ctor_method_field.data == 'constructor_content':
      item = self.constructor_content(ctor_method_field)
      # collected_content.append(item)
      return item, 'ctor'
    elif data(ctor_method_field) == 'method_content':
      item = self.method_content(ctor_method_field, structname=structname)
      return item, 'method'
    elif data(ctor_method_field) == 'field_content':
      kv = self.field_content(ctor_method_field)
      # print('kembalikan field:', kv)
      return kv, 'field'


  def classcontentlist(self, tree, structname=None):
    """
    class_content -> classcontentlist -> classcontent
    classcontentlist
      classcontent
      classcontent
    """
    def create_initialize_method(members):
      """
      return {fieldname: field_value}
      def initialize(id, name, addr)
        @cust_id = id
        @cust_name = name
        @cust_addr = addr
      end
      """
      no_objects = '@@no_of_instances = 0'
      hasil = no_objects + '\n'
      # cust1 = Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
      instance = f'# {structname.lower()}1 = {structname}.new({", ".join(members.values())})'
      hasil = instance + '\n'
      hasil += f'def initialize({", ".join(members.keys())})\n'
      self.inc()
      for k,v in members.items():
        hasil += self.tab() + f'@{k} = {k}\n'
      self.dec()
      hasil += 'end'
      # print('hasil create_initialize_method:', hasil)
      return hasil

    initialize_method_member = {}
    initmethod = ''
    collected_content = []
    for classcontent in anak(tree):
      hasil, jenis = self.classcontent(classcontent, structname=structname)
      if jenis is not None and jenis == 'field':
        # hasil = create_initialie_method(hasil)
        initialize_method_member.update(hasil)
        # print('temukan field:', hasil, 'dict jadi:', initialize_method_member)
      elif hasil:
        collected_content.append(hasil)
    if initialize_method_member:
      # return {fieldname: field_value}
      initmethod = create_initialize_method(initialize_method_member)
      # print('peroleh initmethod:', initmethod)

    if collected_content:      
      tabbed_class_contents = [self.tab() + item for item in collected_content]
      tabbed_class_contents = '\n'.join(tabbed_class_contents)
      if initmethod:
        initializer = [self.tab() + item for item in initmethod.splitlines()]
        initializer = '\n'.join(initializer)
        pemisah = f'\n{"#"*20}\n'
        kembali = '\n' + initializer + pemisah + '\n' + tabbed_class_contents + '\n'
      else:
        kembali = '\n' + tabbed_class_contents + '\n'
    elif initmethod:
      initializer = [self.tab() + item for item in initmethod.splitlines()]
      initializer = '\n'.join(initializer)      
      pemisah = f'\n{"#"*20}\n'
      kembali = '\n' + initializer
    else:
      # no content jadi {} utk ts dan pass utk python
      # self.print('{}')
      kembali = f'\n{self.tab()}# pass'

    return kembali


  def class_content(self, tree, structname=None):
    """
    class_content
      classcontentlist
        classcontent
    """
    # classcontentlist
    if not beranak(tree):
      return None
    classcontentlist = child1(tree)
    kembali = ''
    if beranak(classcontentlist):
      '''
      classcontent
        constructor_content
          function_param
            paramlist
              param
          function_content
            functioncontentlist
              functioncontent
      '''
      hasil = self.classcontentlist(classcontentlist, structname=structname)
      kembali += hasil

    # do something if we have content
    # if not collected_content:
    else:
      kembali += f'\n{self.tab()}# pass'
      
    return kembali


  def class_item(self, cucu):
    """
    class_item
      class_name        MyClass
      class_content
        classcontentlist
          classcontent
    """
    self.inc()
    kembali = ''
    # class_name
    class_name = child1(cucu)
    class_namestr = ''
    if chdata(class_name) == 'nama_identifier_with_typeparams':
      nama_identifier_with_typeparams = child1(class_name)
      class_namestr = chtoken(nama_identifier_with_typeparams)
    elif chdata(class_name) == 'nama_identifier':
      class_namestr = token(class_name)
    kembali += f'class {class_namestr}'
    # class_content
    class_content = child2(cucu)
    hasil = self.class_content(class_content, structname=class_namestr)
    kembali += hasil     
    self.dec()
    kembali += '\nend'
    self.print(kembali)


  def nama_jenis_identifier_array(self, tree):
    """
    array
      item_type
        integer
    """
    kembalian = '__JENIS[]'
    if beranak(tree):
      prim = child1(tree) # item_type
      primi = child1(prim) # integer
      primitive = data(primi)
      petakan = peta_tipe_data.get(primitive, primitive)
      kembalian = kembalian.replace('__JENIS', petakan)
      return kembalian
    kembalian = kembalian.replace('__JENIS', '')
    return kembalian


  def nama_jenis_identifier(self, tree):
    """
    nama_jenis_identifier
      nama_identifier   array
      tipe_identifier
        array
          item_type
            integer
    nama_jenis_identifier
      nama_identifier   satu
      tipe_identifier
        string
    number[]
    """
    nama = child1(tree)
    namaid = token(nama)
    return namaid


  def paramlist(self, tree):
    """
    function_param
      paramlist <- tree
        param
          nama_identifier     satu
    """
    all_params = []
    # print('paramlist tree', tree)
    for param in anak(tree):
      if not beranak(param):
        continue

      paramname_dan_tipe = ''
      paramchild = child1(param)

      if data(paramchild) == 'nama_identifier':
        paramname_dan_tipe = chtoken(param)
      elif data(paramchild) == 'named_values':
        paramname_dan_tipe = self.named_values(paramchild)
      elif data(paramchild) == 'nama_jenis_identifier':
        tipe_data = self.nama_jenis_identifier(paramchild)
        paramname_dan_tipe = tipe_data

      if paramname_dan_tipe:
        # print('param name+tipe:', paramname_dan_tipe)
        all_params.append(paramname_dan_tipe)
    
    # print('all_params:', all_params)
    return all_params


  def type_parameter_list(self, tree):
    all_params = []    
    for param in anak(tree):
      if data(param) == 'type_parameter' and chdata(param) == 'nama_identifier':
        paramname = chtoken(param)
        all_params.append(paramname)
    return all_params


  def type_parameters(self, tree):
    '''
    type_parameters <- ada ini
      type_parameter_list
        type_parameter
          nama_identifier T
    '''
    # type_parameters = child2(nama_identifier_with_typeparams)
    # param_jenis = self.type_parameters(type_parameters)
    paramlist = child1(tree)
    all_params = self.type_parameter_list(paramlist)
    return '<' + ', '.join(all_params) + '>'


  def nama_identifier_with_typeparams(self, tree):
    """
    nama_identifier_with_typeparams
      nama_identifier       a
      type_parameters
        type_parameter_list
          type_parameter
            nama_identifier T
    """
    nama_identifier = child1(tree)
    # print('tree adlh', data(tree))
    if sebanyak(tree, 2):
      '''
      nama_identifier_with_typeparams
        nama_identifier       a             <- tree child 1
        type_parameters                     <- tree child 2
          type_parameter_list
            type_parameter
              nama_identifier T
      '''
      # print('beranak 2 #1')
      type_parameters = child2(tree)
      param_jenis = self.type_parameters(type_parameters)
      # print(f'beranak 2 #2: {param_jenis}')
      class_namestr = token(nama_identifier) + param_jenis
    else:
      '''
      nama_identifier_with_typeparams
        nama_identifier       a
      '''
      # print('beranak 1 #1')
      class_namestr = chtoken(tree)
      # print(f'beranak 1 #1: {class_namestr}')

    return class_namestr


  def class_config(self, tree):
    """    
    class_config: "/" classconfiglist "/"
    classconfiglist: classconfig ("," classconfig)*
    classconfig: "+" -> public
      | "-" -> private    // perlu utk class?
      | "#" -> protected  // perlu utk class?
      | "i" -> interface  // interface declare
      | "i+" -> interface_add // buat class decl+interface decl
      | "t" -> type_alias // kita buat juga type_alias versi single statement
      | "t+" -> type_alias  // class+type
      | "@" nama_identifier   -> decorator
      | ":" nama_identifier   -> extends
      | "i:" nama_identifier  -> implements // interface (beda i dan i: = beda func decl dan call)
      | "^" -> abstract // juga perlu final dan strictfp
      | "F" -> final
      | "SF" -> strictfp
      | "D" -> default
    class_config
      classconfiglist        
        class_config
          classconfiglist
            public
            extends
              nama_identifier     Sports
        class_name
          nama_identifier_with_typeparams
            nama_identifier       Football
    """
    classconfiglist = child1(tree)
    semua_modifier = []
    prepender, appender = '', ''
    for nilai in anak(classconfiglist):
      # print('oprek nilai:', nilai)
      if data(nilai) == 'public':
        hasil = 'public'
        semua_modifier.append(hasil)
      elif data(nilai) == 'private':
        hasil = 'private'
        semua_modifier.append(hasil)
      elif data(nilai) == 'protected':
        hasil = 'protected'
        semua_modifier.append(hasil)
      # elif data(nilai) == 'read_only':
      #   hasil = 'readonly'
      #   semua_modifier.append(hasil)
      elif data(nilai) == 'static':
        hasil = 'static'
        semua_modifier.append(hasil)
      elif data(nilai) == 'async':
        hasil = 'async'
        semua_modifier.append(hasil)
      elif data(nilai) == 'extends':
        '''
        extends
          nama_identifier     Sports
        '''
        appender = 'extends ' + chtoken(nilai)

    if semua_modifier:
      prepender = ' '.join(semua_modifier)
      return prepender, appender
    return prepender, appender


  def class_name(self, tree):
    """
    class_name
      nama_identifier_with_typeparams
        nama_identifier       a
        type_parameters
          type_parameter_list
            type_parameter
              nama_identifier T
    """
    # if chdata(item) == 'nama_identifier_with_typeparams':
    nama_identifier_with_typeparams = child(tree)
    namakelas = self.nama_identifier_with_typeparams(nama_identifier_with_typeparams)
    return namakelas


  def create_module_and_class(self, ifacename, ifacecontent):
    """
    """
    kembali = f'module {ifacename} '
    self.inc()
    kembali += self.tabify_content(ifacecontent)
    self.dec()
    kembali += '\nend'
    
    kembali += '\n'*3
    self.inc()
    kembali += f'class {ifacename}Implementor\n{self.tab()}include {ifacename}'
    
    kembali += self.tabify_content(ifacecontent)
    self.dec()
    kembali += '\nend'
    return kembali


  def interface_item(self, tree):
    """
    interface_item
      interface_keyword
      class_name
        nama_identifier_with_typeparams
          nama_identifier       myinterafce
      class_content
        classcontentlist
          classcontent
    """
    kembali = ''
    ifacename, ifaceconfig, ifacecontent = '', '', ''
    self.inc()
    self.set_empty_content(self.tab() + 'raise "Not Implemented"')
    self.dec()
    for item in anak(tree):
      if data(item) == 'interface_keyword':
        pass
      elif data(item) == 'class_name':
        ifacename = self.class_name(item)
      elif data(item) == 'class_config':
        prepender, appender = self.class_config(item)
        print('appender dan prepender utk iface:', prepender, '&', appender)
        ifaceconfig = prepender + ' '
      elif data(item) == 'class_content':
        ifacecontent = self.class_content(item, ifacename)

    kembali = self.create_module_and_class(ifacename, ifacecontent)
    self.set_empty_content()
    return kembali


  def block_item(self, tree):
    kembali = ''
    for cucu in anak(tree):
      if cucu.data == 'function_item':
        kembali += self.function_item(cucu)
      elif cucu.data == 'class_item':
        kembali += self.class_item(cucu)
      elif cucu.data == 'interface_item':
        kembali += self.interface_item(cucu)
    if kembali:
      self.print(kembali)


  def import_item(self, tree):
    """
    I/sys
    import_item
      keyword_import
      import_things
        import_thing_enclose      <- gak ada efek utk python
          import_thing_default    sys
    Isys 
    import_item
      keyword_import
      import_things
        import_thing_default      sys

    Itreesitter|language,parser 
    import_item
      keyword_import
      import_container    treesitter
      import_things
        import_thing_default      language
        import_thing_default      parser
    """
    container = None
    merged_imports = []
    for kw_cont_thing in anak(tree):
      if data(kw_cont_thing) == 'import_container':
        container = token(kw_cont_thing)
      elif data(kw_cont_thing) == 'import_things':
        default_or_enclose = child1(kw_cont_thing)
        if data(default_or_enclose) == 'import_thing_enclose':
          thing = child1(default_or_enclose)
          item = token(thing)
          merged_imports.append(item)
        elif data(default_or_enclose) == 'import_thing_default':
          item = token(default_or_enclose)
          merged_imports.append(item)

    if container:
      hasil = f'from {container} import {", ".join(merged_imports)}'
    else:
      hasil = f'import {", ".join(merged_imports)}'

    self.output += hasil


  def do_generate(self):
    """
    self.root either item atau item_separator
    """
    # self.output += f'mengoprek data: {self.root.data}\n'
    # item
    self.indentno = 0
    if self.root.data == 'item':
      for dahan in anak(self.root):
        # block_item
        if dahan.data == 'block_item':
          self.block_item(dahan)
        elif dahan.data == 'statement_item':
          self.statement_item(dahan)
        elif data(dahan) == 'import_item':
          self.import_item(dahan)

    elif self.root.data == 'item_separator':
      if self.root.children: # jk bukan []
        newline_or_not = self.root.children[0].data
        self.output += f'\tSEP: {newline_or_not}\n'


  def generate(self):
    self.do_generate()
    return self.output


def generate(RootNode, program_context={}):
  # print('generate (py) called for ', RootNode)
  g = Generator(RootNode, program_context)
  return g.generate()

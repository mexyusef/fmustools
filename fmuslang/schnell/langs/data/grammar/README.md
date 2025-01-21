python main.py "data 1 User username:s(100) name:s email:s(100):e password:s:p mypass:b:<rahasia> nilai:i:ri(1,100)"
insn
  data_insn
    datanumber  1
    tablename   User
    column
      columnname        username
      columntype
        varchar 100
    column
      columnname        name
      columntype
        string
    column
      columnname        email
      columntype
        varchar 100
        email
    column
      columnname        password
      columntype
        string
        password
    column
      columnname        mypass
      columntype
        bcrypt
        bcrypt_value    rahasia
    column
      columnname        nilai
      columntype
        number
        random_int
          min_max
            min 1
            max 100


k=v => username=varchar
kolom:tipe:subtipe = username:varchar(100)

k=v => name=string
kolom:tipe:subtipe = name:string

k=v => email=varchar
Token #1 (kolom:<tipe>:subtipe): 100
kolom:tipe:subtipe = email:varchar(100):email

k=v => password=string
kolom:tipe:subtipe = password:string:password

k=v => mypass=bcrypt
Token #2 (kolom:tipe:<subtipe>): rahasia
kolom:tipe:subtipe = mypass:bcrypt:rahasia

k=v => nilai=number
kolom:tipe:subtipe = nilai:number:(1,100)
*** {'parent': AnyNode(name='root', type='root'), 'type': 'column', 'name': 'nilai', 'value': 'number', 'subclasstype': 'random_int', 'random_int_min': '1', 'random_int_max': '100'} 

AnyNode(name='root', type='root')
|-- AnyNode(name='email', subclasstype='email', type='column', value='varchar')
|-- AnyNode(name='password', subclasstype='password', type='column', value='string')
|-- AnyNode(name='mypass', subclasstype='rahasia', type='column', value='bcrypt')
+-- AnyNode(name='nilai', random_int_max='100', random_int_min='1', subclasstype='random_int', type='column', value='number')

python main.py "data 1 User username:s(100) name:s email:s(100):e password:s:p mypass:b:<rahasia> nilai:i:ri(1,100)"


Tree(
  'min_max', 
  [
    Tree('min', [Token('BILBUL_BERTANDA', '1')]), 
    Tree('max', [Token('BILBUL_BERTANDA', '100')])
  ]
)
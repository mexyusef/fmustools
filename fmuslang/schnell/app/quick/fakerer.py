from schnell.app.fakerutils import get_by_type_or_name, getfakers
from schnell.app.printutils import indah4, indah3
import json, re

convert_type = {
    's'             : 'string',
    'S'             : 'sentence',
    't'             : 'text',
    'p'             : 'paragraph',
    'i'             : 'integer',
    'f'             : 'float',
    'dt'            : 'date',
    'ts'            : 'timestamp',
    '[]'            : 'list',
    '{}'            : 'dict',
    '[[]]'          : 'matrix',
}

def handle_faker(request):
    """
    u -e"/(s/{word,paragraph,text,phone,citydll}"
           s/{word,paragraph,text,phone,citydll}

    u -e"/(type/params"

    u -e/(ts
    u -e/(dt
    u -e/(s
    u -e/(i
    u -e/(f
    u -e/(T
    u -e/([]
    u -e/({}

    u -e"/(s/{word,paragraph,text,phone,citydll}"
    u -e"/(dt/<format>,between,in year,from-to-now,quote-item/single-quote-item"
    u -e"/(ts/<format>,between,in year,from-to-now,quote-item/single-quote-item"
    u -e"/([]/num=5,types=[i,s],quote-items/single-quote-items"
    u -e"/([[]]/num=5,types=[i,s]"    2d/matrix
    u -e"/({}/num=5,types=[i,s]"
    u -e"/(i/between,num-digits,max=...,min=..."
    u -e"/(f/between,num-digits,max=...,min=...,digits=...,places=..."
    """

    # indah4(f'''
    # faker is handling {request}
    # ''', warna='magenta')

    parameters = ''
    funcparams = {}
    namadata = 'dummy'
    # pisahkan jenisdata (list, dict, string, etc) dari params jk ada /
    if '/' in request:
        jenisdata, parameters = request.split('/',1)
    else:
        jenisdata = request
    if ',' in jenisdata:
        jenisdata, namadata = jenisdata.split(',',1)
    tipedata = convert_type.get(jenisdata, 'string')

    if parameters: # tipedata/parameters
        pecah = parameters.split(',')
        # print('pecah:', pecah)
        if tipedata == 'list':
            '''
            handle list dulu yg memang kita pengen/butuhkan
            '''
            pertama = pecah[0] # ini adlh jumlah dulu...-e/([]/5
            if pertama.isdigit():
                namadata += f'_list_num{pertama}'
            if len(pecah)>1:
                kedua = pecah[1] # -e/([]/5,i
                # print('kedua:', kedua, type(kedua))
                if kedua == 's':
                    # u -e/([]/10,s
                    namadata += '_str'
                elif kedua == 'i':
                    # u -e/([]/10,i
                    namadata += '_int'
                elif kedua == 'F': # entah knp jk f gak masuk fakerer dari quick!
                    # u -e/([]/10,F
                    namadata += '_float'
                elif kedua in ['si', 'is']:
                    # u -e/([]/10,si
                    namadata += '_int_str'
                elif kedua.startswith('[') and pecah[-1].endswith(']'):
                    '''
                    ../([]/10,[1,10]
                    ../([]/10,[1,2,3,4,5]
                    random_element([])
                    '''
                    kedua = ','.join(pecah[1:])
                    # print('kedua:', kedua, type(kedua)) # str
                    import ast, random
                    args = ast.literal_eval(kedua)
                    # print('args:', args, type(args)) # list
                    # res = [getfakers('random_element',funcargs=args) for _ in range(int(pertama))]
                    res = [random.choice(args) for _ in range(int(pertama))]
                    indah3(str(res), warna='white')
                    return

                if len(pecah)>2:
                    ketiga = pecah[2] # u -e/([]/5,i,10-50
                    if kedua=='s':
                        if ketiga in ['first_name', 'fn', 'fname', 'firstname']:
                            # u -e/([]/10,s,fn
                            res = [getfakers('first_name') for _ in range(int(pertama))]
                        elif ketiga in ['last_name', 'ln', 'lname', 'lastname']:
                            # u -e/([]/10,s,ln
                            res = [getfakers('last_name') for _ in range(int(pertama))]
                        else:
                            # u -e/([]/10,s,country
                            res = [getfakers(ketiga) for _ in range(int(pertama))]
                            # https://stackoverflow.com/questions/32606599/return-a-variable-in-a-python-list-with-double-quotes-instead-of-single
                            # agar tiap entry dlm DQ
                            
                        res = json.dumps(res)
                        indah3(str(res), warna='white')
                        return
                    elif kedua=='i':
                        # u -e/([]/10,i,0-100
                        # u -e/([]/20,i,100-1000
                        get = re.match(r'(-?\d+)-(\d+)', ketiga)
                        if get:
                            min=int(get.group(1))
                            max=int(get.group(2))
                            res = [getfakers('pyint',funcargs=[min,max],as_is=True) for _ in range(int(pertama))]
                        indah3(str(res), warna='white')
                        return

        elif tipedata == 'dict':
            '''
            pydict(nb_elements=10, variable_nb_elements=True, value_types=None, *allowed_types)
            pydict(5,False,value_types='str')
            pydict(5,False,value_types='int')
            pydict(5,False,value_types=['int','str'])
            sementara kita proses jumlah elemen dan fixed saja
            '''
            if parameters and len(pecah):
                args = [int(pecah[0]), True]
                if len(pecah) == 2:
                    '''
                    ada value_types, bisa i, s, is atau si
                    '''
                    jenis = []
                    if 'i' in pecah[1]:
                        jenis.append('int')
                    if 's' in pecah[1]:
                        jenis.append('str')
                    if jenis:
                        args.append(jenis)
                funcparams.update({
                    'funcargs': args,
                })

        elif tipedata == 'string':
            # asumsikan gak ada , di parameters utk -e/(s/parameters
            if parameters in ['first_name', 'fn', 'fname', 'firstname']:
                # u -e/(s/fn
                res = getfakers('first_name')
            elif parameters in ['last_name', 'ln', 'lname', 'lastname']:
                # u -e/(s/ln
                res = getfakers('last_name')
            else:
                # u -e/(s/first_name_female
                # u -e/(s/last_name_male
                res = getfakers(parameters)
            indah3(str(res), warna='white')
            return

    funcparams.update({
        'tipedata': tipedata,
        'namadata': namadata,
    })

    # res = get_by_type_or_name(tipedata, namadata)
    res = get_by_type_or_name(**funcparams)

    indah3(str(res), warna='white')

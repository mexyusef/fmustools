import copy
from schnell.app.appconfig import command_prompt_data, command_prompt_data_extension, programming_data
from schnell.app.dictutils import get_key_paths
from schnell.app.jsonutils import json_dumps
from schnell.app.printutils import indah4
from schnell.app.windowsutils import hapus_iterate_by_title
from schnell.creator.context import context as global_context

delimiter = programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['editor_fmus_ketik']['join_delimiter']
if not delimiter:
    from startup import initialize_programming_data
    initialize_programming_data()
    delimiter = programming_data['j']['schnell']['gui']['system']['searcher']['widgets']['editor_fmus_ketik']['join_delimiter']

def list_command_prompt():
    data1 = str(command_prompt_data)
    data2 = str(command_prompt_data_extension)
    result = '============== command_prompt_data\n' + data1 + '\n============== command_prompt_data_extension\n' + data2
    return result

def set_or_get_programming_data(key, value, is_setter):
    if '/' in key:
        keys = key.split('/')
        if is_setter:
            current_dict = programming_data
            try:
                for key in keys[:-1]:
                    '''
                    kasus:
                    a/b/c=d
                    - gak ada a
                        bisa current_dict[key] = {} krn nanti b dst masuk sini
                    - gak ada b
                        bisa current_dict[key] = {} krn nanti c dst masuk sini
                    - gak ada c
                        jangan current_dict[key] = {} krn kita pengen assign value ke c
                    untungnya keys[:-1] pastikan c gak diproses di sini
                    '''
                    # jk key tidak di current dict...maka bikin dulu...tapi tipe nya apa?
                    if key not in current_dict:
                        current_dict[key] = {}
                    current_dict = current_dict[key]
                last_key = keys[-1]
                if value:
                    current_dict[last_key] = value
                return current_dict.get(last_key, None)
            except Exception:
                return None
        else: # getter
            current_dict = copy.deepcopy(programming_data)
            try:
                for key in keys[:-1]:
                    current_dict = current_dict[key]
                last_key = keys[-1]
                result = current_dict.get(last_key, None)
                if programming_data['debug']:
                    indah4(f"[set_or_get_programming_data] result /{result}/, type {type(result)}", warna='magenta')
                return result
            except Exception as err:
                if programming_data['debug']:
                    indah4(f"[set_or_get_programming_data] exception /{err}/", warna='red')
                return None
    return None

def process_ketik(command='list'):
    """
    ctrl shift "
    empty           list
    1=something     index=name
    """
    result = 'NOP'
    indah4(f"[process_ketik], command: {command}, type: {type(command)}.", warna='yellow')
    if isinstance(command, int):
        command = str(int)
    hapus_iterate_by_title() # selalu bersihkan yg gak ada
    if command in ['list', 'ls']:
        # data1 = json.dumps(command_prompt_data, indent=2, cls=HANDLEEncoder)
        # data2 = json.dumps(command_prompt_data_extension, indent=2)
        # data1 = str(command_prompt_data)
        # data2 = str(command_prompt_data_extension)
        # result = '============== command_prompt_data\n' + data1 + '\n============== command_prompt_data_extension\n' + data2
        data3 = json_dumps(programming_data)
        # data4 = json_dumps(global_context)
        # result = '============== programming_data\n' + data3 + '\n============== global_context\n' + data4 + '\n'
        # result += list_command_prompt()
        # biar singkat
        result = delimiter.join([i.lstrip() for i in data3.splitlines()]) + '\n'
        # result = data3 + '\n'
        return result

    elif command in ['reload', 'load']:
        from startup import initialize_programming_data
        initialize_programming_data(invalidate=['config.json', 'config_quick.json'])
        result = 'Reloaded'

    elif command in ['keys']:
        # return get_key_paths(programming_data)
        return '\n'.join(list(programming_data.keys()))

    elif command in ['tree', 'paths']:
        from schnell.app.dictutils import print_tree, dict_paths
        tree = print_tree(programming_data)
        paths = dict_paths(programming_data)
        return tree + '\n\n' + paths

    elif command.startswith('*'):
        '''
        * ctrlshift" print context
        kita pengen bisa ubah misalnya current_active_language
        current_active_language=py/go/rs/ts/java, dst.
        '''
        if command == '*': # get/list
            result = json_dumps(global_context)
        else: # set
            command = command.removeprefix('*').strip()
            if command and command.count('=')>0:
                k,v = command.split('=',1)
                if k in global_context:
                    global_context[k]=v
                    result = json_dumps(global_context)

    elif command.startswith('$'):
        '''
        $
        $k=v
        kita gunakan utk data programming biar bisa kerja cepat
        '''
        if command == '$': # get/list
            # result = json_dumps(programming_data)
            result = list_command_prompt()
        else: # set
            command = command.removeprefix('$').strip()
            # if command and command.count('=')>0:
            #     k,v = command.split('=',1)
            #     # if k in programming_data: # gak perlu ada duluan
            #     programming_data[k]=v
            #     result = json_dumps(programming_data)
            # elif command in programming_data:
            #     result = programming_data[command]
            if command.count('=')==1:
                '''
                $1=namaconsole
                '''
                index, console_name = command.split('=',1)
                if index.isdigit():
                    index = int(index)
                    if index in command_prompt_data:
                        title = command_prompt_data[1]['id']
                        command_prompt_data_extension[console_name] = {
                            'title': title,
                            'index': index,
                        }
                        result = list_command_prompt()
                        return result

    else:
        # jika cs" saja maka list
        if not command:
            result = json_dumps(programming_data,indent=2)
            result = delimiter.join([i.lstrip() for i in result.splitlines()])
        else:
            if command and command.count('=')>0: # setter
                k,v = command.split('=',1)
                if v.isdigit(): # detek jk digit berarti ini int-value
                    v = int(v)
                # if k in programming_data:
                # gak perlu ada duluan, bisa set on the fly, jd gak perlu "if k in programming_data:"
                # TODO: bisa a/b/c=d utk nyatakan programming_data[a][b][c]=d
                if '/' in k: # a/b/c=value, nested setter
                    result = set_or_get_programming_data(k,v,True)
                    if programming_data['debug']:
                        print('nested setter:', result, type(result))
                else: # a = value, direct setter
                    programming_data[k]=v
                    result = json_dumps(programming_data)
                    result = delimiter.join([i.lstrip() for i in result.splitlines()])
            elif command in programming_data or '/' in command: # getter
                if programming_data['debug']:
                    indah4(f"[nested or direct getter] {command} in programming_data or '/' in {command}", warna='green')
                # TODO: bisa a/b/c utk request programming_data[a][b][c]
                if '/' in command: # nested getter
                    result = set_or_get_programming_data(command,None,False)
                    if result is not None: # agar bisa proses 0
                        if programming_data['debug']:
                            print('nested getter:', result, type(result))
                        if isinstance(result, (dict, list)):
                            # hanya jk dict result, maka kita pengen lihat versi non-indented
                            # jk non-dict, kita pengen spt aslinya
                            result = json_dumps(result)
                            result = delimiter.join([i.lstrip() for i in result.splitlines()])
                            # result = delimiter.join([i.lstrip() for i in result.splitlines()])
                        elif isinstance(result, (int, bool, float)):
                            result = str(result)
                else: # direct getter
                    result = programming_data[command]
                    if isinstance(result, (dict, list)):
                        result = json_dumps(result)
                        result = delimiter.join([i.lstrip() for i in result.splitlines()])
                    elif isinstance(result, (int, bool, float)):
                        result = str(result)
            else:
                indah4(f"{command} with type {type(command)} is not handled, keys of programming_data = {list(zip(list(programming_data.keys()), [type(i) for i in programming_data.keys()]))}", warna='red')

    return result

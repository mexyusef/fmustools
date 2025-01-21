def replace_variables(s, variables, mark_start='#v:', mark_end='#'):
    """
    @params
    @returns

    @about
    kita pengen bisa oprek variables di fmusperintah
    cocok utk ganti namaproyek di supabase, dll
    """
    import re

    def repl(match):
        var_name = match.group(1)
        return str(variables.get(var_name, f"{mark_start}{var_name}{mark_end}"))

    return re.sub(rf"{mark_start}(.+?){mark_end}", repl, s)

def test_replace_variables():
    my_variables = {
        'name': 'wieke',
        'age': 25,
        'location': 'brussels'
    }

    mystr = 'my name is #v:name# and my age is #v:age#'
    mystr = replace_variables(mystr, my_variables)
    print(mystr)


if __name__ == '__main__':
    test_replace_variables()

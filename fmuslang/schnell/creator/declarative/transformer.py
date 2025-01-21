def transformer_function(txf, nilai):
    if txf == 'tx_single':
        nilai = f"'{nilai}'"
    elif txf == 'tx_double':
        nilai = f'"{nilai}"'
    elif txf == 'tx_braces':
        nilai = f'{{ {nilai} }}'
    elif txf == 'tx_brackets':
        nilai = f'[ {nilai} ]'
    elif txf == 'tx_parentheses':
        nilai = f'( {nilai} )'
    elif txf == 'tx_prepend_minus':
        nilai = f'- {nilai}'
    elif txf == 'tx_capitalize':
        nilai = f'{nilai.capitalize()}'
    elif txf == 'tx_lower':
        nilai = f'{nilai.lower()}'
    elif txf == 'tx_upper':
        nilai = f'{nilai.upper()}'
    return nilai


# create a python function that will accept a list of items and if len is > max_len then return as [item, item, ..., item, item] that is: first 5 items, ..., then last 4 items of the list, otherwise just return the list


def shorten_list(input_list, max_len=10):
    """
    caution:
    ... adlh str
    """
    if len(input_list) > max_len:
        return input_list[:max_len//2] + ['...'] + input_list[-((max_len//2)-1):]
    else:
        return input_list

def test_shorten_list():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    result = shorten_list(my_list)
    print(result)
    # [1, 2, 3, 4, 5, '...', 12, 13, 14, 15]

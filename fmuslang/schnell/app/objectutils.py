import copy


def salin(data):
    return copy.copy(data)


def hapus(data, kunci):
    del data[kunci]


def hapus_salin(data, kunci):
    baru = salin(data)
    hapus(baru, kunci)
    return baru


def hapus_salin_node(data, kunci):
    baru = salin(data)
    hapus(baru.__dict__, kunci)
    return baru


def hapus_salin_node_dalam(data, kunci):
    baru = copy.deepcopy(data)
    hapus(baru.__dict__, kunci)
    return baru

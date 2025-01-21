
import datetime, json, multiprocessing, os, pickle, re
import logging
from ast import literal_eval

# fiona
# bson
# geojson
# geojson_utils
# geopandas
# shapely
import geopandas
from geojson_utils import centroid
from geojson import Feature, FeatureCollection, Point, Polygon

# import redis
cache_operation_key = 'geojson:operations'
CACHE_KEY='geojson:sitarang'
CACHE_DATA = '' # redis.StrictRedis(db=os.environ['CACHE_DB'],port=os.environ['REDIS_PORT'],host=os.environ['REDIS_HOST'],password=os.environ['REDIS_PASSWORD'])
CENTER_KEY = f'center:{CACHE_KEY}'
# from sitarangbe.extensions import (
#   # CACHE_DATA, 
#   # CACHE_KEY,
#   # CENTER_KEY,
#   # cache_operation_key,
# )
# from sitarangbe.utils import logmsg
# from sitarangbe.config import geojsonpath

geojson_dir = '/mapdata'
geojson_filename = 'sitarang.json'
geojsonpath = os.path.join(geojson_dir, geojson_filename)
gdb_file = 'SiTarang.gdb'
gdb_path = os.path.join(geojson_dir, gdb_file)

# LOGGER = redis.StrictRedis(db=os.environ['LOG_DB'],port=os.environ['REDIS_PORT'],host=os.environ['REDIS_HOST'],password=os.environ['REDIS_PASSWORD'])
def logmsg(msg, kelas=__file__):
    waktu = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    kunci = f'{kelas}:{waktu}'
    # LOGGER.set(kunci, msg)
    print(f'[{kunci}]'+ msg)

# import logging
# logging.basicConfig(level=logging.DEBUG, filename=f'{__file__}.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.info('geoservice initial message: info')
# logging.warning('geoservice initial message: warning')
# logging.debug('geoservice initial message: debug')

# logmsg('where is the love?', __file__)
"""
banyak bermain dg:
geopandas.geodataframe.GeoDataFrame
pandas.core.series.Series
bisa dibilang: geodataframe itu table beserta isinya, series itu kolom dari table beserta isinya

krn geodataframe itu table, maka utk dapatkan row n, kita akses dg: geodataframe.iloc[n]
ada jg geodataframe[n] dan geodataframe.loc[n]

utk geometri kita punya:
geojson.geometry.Polygon dst

TODO
- gimana bikin semua yg nama kelurahan di kec xxx
"""

# def getlogger():
#     """
#     https://stackoverflow.com/questions/39863718/how-can-i-log-outside-of-main-flask-module
#     https://realpython.com/python-logging/
#     https://stackoverflow.com/questions/45923290/how-to-get-the-current-log-level-in-python-logging-module?rq=1
#     debug, info, warning, error, critical
#     """
#     from sitarangbe import APPNAME
#     logger = logging.getLogger(APPNAME)
#     # print(f'level: {logger.level}')
#     return logger

geojson_files = None # geodataframe
# from ipyleaflet import Map, GeoData, basemaps, LayersControl
# dasar_peta = [
#     basemaps.Esri.WorldTopoMap
# ]
concurrent_processes = 5
operation_pool = multiprocessing.Pool(processes=concurrent_processes)
save_operation = pickle # json

def reload_geojson():
    global geojson_files
    print(__file__, 'Check that /mapdata exists:', os.listdir('/'))
    exists = CACHE_DATA.get(CACHE_KEY)
    if exists is None:
        geojson_files = geopandas.read_file(geojsonpath)
        CACHE_DATA.set(CACHE_KEY, pickle.dumps(geojson_files))
    else:
        geojson_files = pickle.loads(exists)
    # print('geoservice.py: geojson files has been loaded.')
    # print(get_nrows(1))
    return geojson_files

def dataframe():
    if geojson_files is None:
        return reload_geojson()
    return geojson_files

def center_dataframe():
    """
    """
    if not CACHE_DATA.exists(CENTER_KEY):
        center = get_center_dataframe(geojson_files)
        CACHE_DATA.set(CENTER_KEY, str(center))
    else:
        center = literal_eval ( CACHE_DATA.get(CENTER_KEY).decode() )
    return center

def get_head():
    global geojson_files
    if geojson_files is None:
        return reload_geojson().head()
    return geojson_files.head()

def get_nrows(n):
    global geojson_files
    return geojson_files .loc [:n]
    # return geojson_files .iloc [:n]

def get_rowrange(start,end):
    global geojson_files
    return geojson_files .loc [start:end]

def get_size():
    """
    (rows, cols)
    """
    global geojson_files
    return geojson_files .shape

def get_row_size():
    """
    """
    global geojson_files
    return len(geojson_files.index)

def get_col_size():
    """
    """
    global geojson_files
    return len(geojson_files.columns)

def jumlah_baris_kolom(geodataframe):
    return geodataframe.shape

def get_value_for_row_col(row, col):
    """
    dapatkan value utk sebuah kolom (misal LUAS_M2) utk sebuah row/record/data/entry

    lebih cepat:
    df.iloc[row,col]
    """
    global geojson_files
    # from sitarangbe.extensions import applogger
    return geojson_files .iloc[row,col]

    # if row.isdigit() and col.isdigit():
    # logmsg(f"get_value_for_row_col: {row} dan {col} yang diminta", __file__)
    # # print("%d dan %d yang diminta" % (row, col))
    # colname = geojson_files.columns.values [col]
    # return geojson_files.iloc[row] [ colname ]

def get_value_for_toprows_col(nrow, col):
    """
    kembalian adlh Series, hrs di .to_json() kan

    lebih cepat:
    df.iloc[:nrow,col]
    """
    toprows = get_nrows(nrow)
    colname = geojson_files.columns.values [col]
    return toprows [colname]

def get_value_for_rowrange_col(rowstart, rowend, col):
    rowrange = get_rowrange(rowstart, rowend)
    colname = geojson_files.columns.values [col]
    return rowrange [colname]

def get_all_values_for_col(col):
    """
    geojson_files['LUAS_M2'] maka dapatkan semua luas
    allcamats =  sitarang['KECAMATAN']
    len(allcamats) = 3970
    coba sitarang[['KECAMATAN'],['KELURAHAN']]
    gak bisa, bisanya:
    sitarang[sitarang.columns[1:3]] <- dataframe
    """
    global geojson_files
    colname = geojson_files.columns.values [col]
    return geojson_files [colname]

def get_all_values_for_col_unique(col):
    series_to_dict = get_all_values_for_col(col) .to_dict()
    unique_values = set(series_to_dict.values())
    return list(unique_values) # set tdk json serializable

def get_columns_values():
    global geojson_files
    if geojson_files is None:
        return reload_geojson().columns.values
    return geojson_files.columns.values

def get_column_index(pola):
    kolom = get_columns_values() .tolist()
    # pastikan pola kita lower() utk cAmAt dsdt
    temukan = [item for item in kolom if pola.lower() in item.lower()]
    if len(temukan) == 0:
        return -1, None
    elif len(temukan) > 1:
        terpendek = min(temukan, key=len)
        return kolom.index(terpendek), terpendek
    else:
        return kolom.index(temukan[0]), temukan[0]

def children_of_parent(parentname, parenttype, childrentype):
    """
    contoh: 
    parentname = 'Kecamatan Payakumbuh Utara' // sementara exact dulu
    parenttype = camat/kecamatan
    childrentype = lurah/kelurahan
    dapatkan semua nama kelurahan di bawah payakumbuh utara
    """
    global geojson_files
    index, _ = get_column_index(parenttype)
    if index != -1:
        index2, _ = get_column_index(childrentype)
        if index2 != -1:
            # create dataframe of parent,child
            df = geojson_files.iloc[:,[index,index2]]
            parentseries = df[df.columns[0]] # 0 parent, 1 child
            # jk kita mau kirim dataframe camat/lurah
            # filtered = df [ parentseries == parentname]
            # jk pengen kirim geojson berisi geometry etc
            # filtered = geojson_files [ parentseries == parentname]
            # if filtered.shape[0] == 0:
            #     return None
            # kita pengen kirim list -> unique set...
            filtered = df [ parentseries == parentname] .iloc[:,1] # ambil child/lurah
            unik = set(filtered.tolist())
            if len(unik) == 0:
                return None
            return list(unik)
    return None 

def apply_criterion(kolom, mapfunc):
    """
    sitarang.columns.values [6]
        'LUAS_M2'
    sitarang.iloc[42].index[6]
        'LUAS_M2'
    sitarang.iloc[42] ['LUAS_M2']
        34412.7

    criterion = sitarang['LUAS_M2'].map(lambda x: x > 200000)
    mapfunc:
        lambda item: item > 100000
        lambda item: item != 'Budidaya'
    """
    global geojson_files
    criterion = geojson_files[kolom].map(mapfunc)
    return geojson_files[criterion]

def apply_criterion_by_pattern(pola, mapfunc):
    index, kolom = get_column_index(pola)
    if index != -1:
        return apply_criterion(kolom, mapfunc)
    return None

def apply_multiple_criterion(**kolom_mapfuncs):
    """
    """
    global geojson_files
    hasil = 1
    for kolom, mapfunc in kolom_mapfuncs.items():
        term = apply_criterion(kolom, mapfunc)
        hasil = hasil & term
    return geojson_files[hasil]

def apply_multiple_criterion2(**kolom_mapfuncs):
    """
    """
    global geojson_files
    hasil = None
    for kolom, mapfunc in kolom_mapfuncs.items():
        # term = apply_criterion(kolom, mapfunc) # ini jd ada operasi & utk float dan bool
        term = geojson_files[kolom].map(mapfunc)
        hasil = term if (hasil is None) else (hasil & term)
    if hasil is None:
        return None
    return geojson_files[hasil]

def apply_multiple_criterion3(pola1, func1, pola2, func2):
    """    
    """
    global geojson_files
    idx1, kol1 = get_column_index(pola1)
    idx2, kol2 = get_column_index(pola2)
    logmsg(f"apply_multiple_criterion3: {pola1} -> {idx1, kol1}, {pola2} -> {idx2, kol2}", __file__)
    # print(f"apply_multiple_criterion3: {pola1} -> {idx1, kol1}, {pola2} -> {idx2, kol2}")
    if idx1 != -1 and kol1 and idx2 != -1 and kol2:
        criterion = geojson_files[kol1].map(func1) & geojson_files[kol2].map(func2)
        return geojson_files[criterion]
    return None

def redis_key_for_dict(input_kamus):
    """
    input kamus adlh list of dicts
    [{'pola_kolom': 'camat', 'pola_atau_nilai': 'Kecamatan Payakumbuh Timur', 'type': 'str', 'oper': 'eq'}]
    """
    stringified = json.dumps(input_kamus).replace('[','').replace(']','').replace('{','').replace('}','').replace('"','').replace("'",'').replace(' ','').replace(",",'|')
    return f"{cache_operation_key}:{stringified}"

def check_cached_operation(input_kamus):
    kunci = redis_key_for_dict(input_kamus)
    logmsg(f'check_cached_operation: {kunci}', __file__)
    if CACHE_DATA.exists(kunci):
        return save_operation.loads(CACHE_DATA.get(kunci))
    return None

def save_operation_result(input_kamus, data):
    kunci = redis_key_for_dict(input_kamus)
    CACHE_DATA.set(kunci, save_operation.dumps( data ))
    logmsg(f'save_operation_result: {kunci} for input dict: {input_kamus}', __file__)

def apply_multiple_criterion4(**kolom_mapfuncs):
    """
    semua kolom adlh pola
    dari frontend:
    kamus.push({
        'pola_kolom': 'kawasan',
        'pola_atau_nilai': props.geo.filter.kawasan,
        'type': 'str',
        'oper': 'eq',
    })
    var filterset = {
        'kamus': kamus
    }
    add_geojson_filter_to_map(map, filterset, ..
    """
    global geojson_files
    hasil = None

    # cek cache
    # kunci = redis_key_for_dict(kolom_mapfuncs)
    # exists = CACHE_DATA.get(kunci)
    # if exists:
    #     return save_operation.loads(exists)

    for kolom, mapfunc in kolom_mapfuncs.items():
        index, column = get_column_index(kolom)
        logmsg(f"apply_multiple_criterion4: {kolom} -> {index, column}", __file__)
        # print(f"apply_multiple_criterion4: {kolom} -> {index, column}")
        if index != -1 and column:
            term = geojson_files[column].map(mapfunc)
            # TypeError: unsupported operand type(s) for &: 'float' and 'bool'
            # apply_criterion(column, mapfunc)
            hasil = term if (hasil is None) else (hasil & term)
            # kita bisa: 
            # import multiprocessing
            # p = multiprocessing.Process(target=lambda: CACHE_DATA.set..., args(,))
            # p.daemon = True
            # p.start()
            # pusing masalah: perlu join? kapan?
            # CACHE_DATA.set(kunci, save_operation.dumps(geojson_files[hasil]))
        # else:
        #     return None
    if hasil is None:
        return None
    return geojson_files[hasil]

def get_center(feature_geometry, dont_reverse=False):
    """
    feature_geometry adlh <Feature>.geometry atau <FeatureCollection>[feature_index].geometry
    lnglat adlh geojson friendly
        lola, cewek
    latlng adlh leaflet friendly
        lalo, cowok
    """
    lnglat_list = centroid(feature_geometry) ['coordinates']
    if dont_reverse:
        return tuple(lnglat_list)
    latlng_tuple = tuple(reversed(lnglat_list))
    return latlng_tuple

def fitur(n=0):
    global geojson_files
    df=geojson_files
    return Feature(geometry=df.iloc[n]['geometry'], properties={key:value for (key,value) in df.iloc[n].items() if key!='geometry'})

def fitur_df(n=0, df=geojson_files):
    return Feature(geometry=df.iloc[n]['geometry'], properties={key:value for (key,value) in df.iloc[n].items() if key!='geometry'})

def geometry(n=0):
    # global geojson_files
    # df=geojson_files
    # return fitur(n,df).geometry
    return fitur(n).geometry

def geometry_df(n=0, df=geojson_files):
    # global geojson_files
    # df=geojson_files
    # return fitur(n,df).geometry
    return fitur_df(n, df).geometry

def get_combined_geoms(feature_geometries):
    allgeoms = []
    for geom in feature_geometries:
        allgeoms += geom ['coordinates'][0]
    return [allgeoms]

def get_center_geometries(feature_geometries):
    """
    misal punya geodataframe, kita filter dg apply_criterion shg dapatkan df baru dg n feature.
    kita bisa;
    x = [geometry(n,new_df) for n in range(0,new_df.shape[0])]
    get_center_geometries(x)
    """
    newgeom = Polygon(get_combined_geoms(feature_geometries))
    return get_center(newgeom)

def get_center_dataframe(geodataframe):
    """
    utk dapatkan jumlah rows/records
    selain .shape[0] bisa juga len(.index)
    """
    x = [geometry_df(n,geodataframe) for n in range(0,geodataframe.shape[0])]
    return get_center_geometries(x)

def get_center_geojson():
    global geojson_files
    x = [geometry(n) for n in range(0,geojson_files.shape[0])]
    return get_center_geometries(x)

def get_center_dataframe_first_n(n, geodataframe):
    """
    indexing dg [:n] mungkin hrs diganti dg .iloc[:n]
    """
    newdataframe = geodataframe[:n]
    return get_center_dataframe(newdataframe)

def get_feature_from_geodataframe(index, geodataframe):
    """
    gak perlu int(numpy.int64)?
    """
    feature_geom = geodataframe.iloc[index] ['geometry']
    feature_props = {key:value for (key,value) in geodataframe.iloc[index].items() if key!='geometry'}
    return Feature(geometry=feature_geom, properties=feature_props)

def get_geometry_from_feature(index, geodataframe):
    """
    adlh dict berisi type: ... dan coordinates: ...
    coordinates sendiri [ [ [lnglat], [lnglat], .. ] ]
    """
    return get_feature_from_geodataframe(index, geodataframe).geometry

def get_featurelist_from_geodataframe(geodataframe):
    import numpy

    rows, cols = jumlah_baris_kolom(geodataframe)
    feature_list = []
    for row in range(0, rows):
        curprops = {}
        curgeom = None
        for col in range(0, cols):
            key = geodataframe.columns[col] # geodataframe.iloc[row].index[col]
            nilai = geodataframe.iloc[row] [key]
            if isinstance(nilai, numpy.int64):
                nilai = int(nilai)
            if key != 'geometry':
                curprops[key] = nilai
            else:
                curgeom = nilai

        feature_list.append(Feature(geometry=curgeom, properties=curprops))

    return feature_list

def get_featurecollection_from_geodataframe(geodataframe):
    return FeatureCollection(get_featurelist_from_geodataframe(geodataframe))

def get_unique_values(dataframe, col_index):
    """
    pertama ambil semua values dari sebuah kolom, jadi satu series vertikal
    tolist(), dari series ke list
    set() utk dapatkan nilai2 unik
    balik ke list lagi
    contoh:
    get_unique_values(sitarang, 1) utk semua kecamatan
    """
    return list(set(dataframe.iloc[:,col_index].tolist()))

def get_subdataframe(dataframe, col_indexes=[]):
    if col_indexes:
        return dataframe.iloc[:,col_indexes]
    return dataframe

def filter_dataframe_by_series_value(dataframe, series, value):
    """
    hasil adlh dataframe
    """
    return dataframe[ series == value ]

def dataframe_to_series(dataframe, col_index):
    """
    contoh pake: ambil semua kelurahan dari kecamatan xxx

    dfsub = get_subdataframe(geojson, [1,2])
    series = dataframe_to_series(dfsub, 0) # kecamatan
        series = dataframe_to_series2(dfsub, 0) # kecamatan
    filter = filter_dataframe_by_series_value(dfsub, series, 'Kecamatan Payakumbuh Utara')
    kelurahan = dataframe_to_series(filter, 1) # kelurahan, berbentuk series
        kelurahan = dataframe_to_series2(filter, 1) # kelurahan, berbentuk series
    hasil = kelurahan.tolist() # ini masih repeating
    hasil_akhir = uniqify_list(hasil)
    """
    return dataframe[dataframe.columns[col_index]]

def dataframe_to_series2(dataframe, col_index):
    return dataframe.iloc[:,col_index]

def uniqify_list(the_list):
    return list(set(the_list))

def get_columns(colname):
    """
    'OBJECTID_1', 
    'KECAMATAN', 
    'KELURAHAN', 
    'BWP', 
    'SUB_BWP', 
    'BLOK',       
    'LUAS_M2', 
    'KDB', 
    'KLB', 
    'KDH', 
    'GSB_DPN_M', 
    'GSB_SPG_M', 
    'GSB_BLK_M',
    'h_BANGUNAN', 
    'd_BEBASBLK', 
    'd_BEBASSPG', 
    'KODE_SUBZO', 
    'Zona',
    'Sub_Zona', 
    'Sub_Blok', 
    'Kawasan'
    """
    global geojson_files
    colkey = f'valuelist:{colname}'
    daftar = CACHE_DATA.lrange(colkey, 0, -1)
    if len(daftar) == 0:
        if geojson_files is None:
            geojson_files = reload_geojson()
        colvalues = geojson_files.loc[:,colname].unique().tolist()
        CACHE_DATA.lpush(colkey, *colvalues)
    else:
        colvalues = CACHE_DATA.lrange(colkey, 0, -1)

    return colvalues

def get_kdb():
    return get_columns('KDB')

def get_klb():
    return get_columns('KLB')

def get_kdh():
    return get_columns('KDH')

def get_bwp():
    return get_columns('BWP')

def get_subbwp():
    return get_columns('SUB_BWP')

def get_blok():
    return get_columns('BLOK')

def get_subblok():
    return get_columns('Sub_Blok')

def get_kodesubzona():
    return get_columns('KODE_SUBZO')

def get_zona():
    return get_columns('Zona')

def get_subzonas():
    global geojson_files
    subzona_key = 'valuelist:subzona'
    daftar = CACHE_DATA.lrange(subzona_key, 0, -1)
    if len(daftar) == 0:
        logmsg(f'key {subzona_key} is empty', __file__)
        if geojson_files is None:
            logmsg(f'geojson_filess {geojsonpath} is empty', __file__)
            geojson_files = reload_geojson()
        subzonas = geojson_files.loc[:,'Sub_Zona'].unique().tolist()
        logmsg(f'from empty: getting subzonas <{subzonas}>', __file__)
        CACHE_DATA.lpush(subzona_key, *subzonas)
    else:        
        subzonas = CACHE_DATA.lrange(subzona_key, 0, -1)
        logmsg(f'from content: getting subzonas <{subzonas}>', __file__)

    return subzonas

def string_in(needle):
    return lambda item: needle.lower() in item.lower()

def string_equal(needle):
    return lambda item: needle.lower() == item.lower()

def string_empty(needle):
    return lambda item: item == ''

def numify(stringnum, is_percent=False, is_comma=False, get_max=True):
    ranger = r'\s*(\d+)\s*-\s*(\d+)\s*'
    if stringnum == '':
        return 0.0
    match = re.match(ranger, stringnum)
    if match:
        start,end = match.groups()
        if get_max:
            return float(end)
        else:
            return float(start)
    if is_percent:
        return float (stringnum.replace('%','').strip())
    if is_comma:
        return float (stringnum.replace(',','.').strip())
    try:
        return float(stringnum)
    except:
        return 0.0

def stringnumeric_less(needle):
    return lambda item: numify(item) < needle

def stringnumeric_greater(needle):
    return lambda item: numify(item, get_max=False) > needle

def stringpercent_less(needle):
    return lambda item: numify(item, is_percent=True) < needle

def stringcomma_less(needle):
    return lambda item: numify(item, is_comma=True) < needle

def numeric_zero(needle):
    return lambda item: item == 0.0

def numeric_less(needle):
    return lambda item: item < needle

def numeric_greater(needle):
    return lambda item: item > needle
    
def numeric_equal(needle):
    return lambda item: needle == item

def percent_to_float(item):
    """
    kdb = "2%"
    kdh = "98%"
    """
    return float (item.replace('%','').strip())

def comma_to_float(item):
    """
    klb = "0,02"
    """
    return float (item.replace(',','.').strip())

"""
harus ada tipe:
str_to_float
comma_to_float
percent_to_float
range_to_float
"""

# https://leaflet-extras.github.io/leaflet-providers/preview/
layers = {
    '1': {
        'tile': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'OpenStreetMap_Mapnik',
    },

    '2': {
        'tile': 'https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'OpenStreetMap_DE',
    },

    # '3': {
    #     'tile': 'https://wxs.ign.fr/GeoportailFrance_maps/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE=normal&TILEMATRIXSET=PM&FORMAT=image/jpeg&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN-EXPRESS.STANDARD&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}',
    #     'attrib': '<a target="_blank" href="https://www.geoportail.gouv.fr/">Geoportail France</a>',
    #     'name': 'GeoportailFrance_maps',
    # },

    '4': {
        'tile': 'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',
        'attrib': '&copy; Openstreetmap France | &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'OpenStreetMap_France',
    },

    '5': {
        'tile': 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>',
        'name': 'OpenStreetMap_HOT',
    },

    '6': {
        'tile': 'https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles courtesy of <a href="http://www.openstreetmap.bzh/" target="_blank">Breton OpenStreetMap Team</a>',
        'name': 'OpenStreetMap_BZH',
    },

    '7': {
        'tile': 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
        'attrib': 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
        'name': 'OpenTopoMap',
    },

    '8': {
        'tile': 'https://wxs.ign.fr/choisirgeoportail/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE=normal&TILEMATRIXSET=PM&FORMAT=image/jpeg&LAYER=ORTHOIMAGERY.ORTHOPHOTOS&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}',
        'attrib': '<a target="_blank" href="https://www.geoportail.gouv.fr/">Geoportail France</a>',
        'name': 'GeoportailFrance_orthos',
    },

    '9': {
        'tile': 'https://dev.{s}.tile.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png',
        'attrib': '<a href="https://github.com/cyclosm/cyclosm-cartocss-style/releases" title="CyclOSM - Open Bicycle render">CyclOSM</a> | Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'CyclOSM',
    },

    '10': {
        'tile': 'https://maps.heigit.org/openmapsurfer/tiles/roads/webmercator/{z}/{x}/{y}.png',
        'attrib': 'Imagery from <a href="http://giscience.uni-hd.de/">GIScience Research Group @ University of Heidelberg</a> | Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'OpenMapSurfer_Roads',
    },

    '11': {
        'tile': 'https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png',
        'attrib': 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Hydda_Full',
    },

    '12': {
        'tile': 'https://{s}.tile.openstreetmap.se/hydda/base/{z}/{x}/{y}.png',
        'attrib': 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Hydda_Base',
    },

    '13': {
        'tile': 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.png',
        'attrib': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Stamen_Toner',
    },

    '14': {
        'tile': 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}{r}.png',
        'attrib': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Stamen_TonerBackground',
    },

    '15': {
        'tile': 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.png',
        'attrib': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Stamen_TonerLite',
    },

    '16': {
        'tile': 'https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.jpg',
        'attrib': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Stamen_Watercolor',
    },

    '17': {
        'tile': 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png',
        'attrib': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Stamen_Terrain',
    },

    '18': {
        'tile': 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}{r}.png',
        'attrib': 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'Stamen_TerrainBackground',
    },

    '19': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
        'name': 'Esri_WorldStreetMap',
    },

    '20': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Copyright: &copy;2012 DeLorme',
        'name': 'Esri_DeLorme',
    },

    '21': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community',
        'name': 'Esri_WorldTopoMap',
    },

    '22': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
        'name': 'Esri_WorldImagery',
    },

    # '23': {
    #     'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}',
    #     'attrib': 'Tiles &copy; Esri &mdash; Source: USGS, Esri, TANA, DeLorme, and NPS',
    #     'name': 'peta 23',
    # },

    '24': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Source: Esri',
        'name': 'Esri_WorldShadedRelief',
    },

    # '25': {
    #     'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}',
    #     'attrib': 'Tiles &copy; Esri &mdash; Source: US National Park Service',
    #     'name': 'peta 25',
    # },

    '26': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Sources: GEBCO, NOAA, CHS, OSU, UNH, CSUMB, National Geographic, DeLorme, NAVTEQ, and Esri',
        'name': 'Esri_OceanBasemap',
    },

    '27': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
        'name': 'Esri_NatGeoWorldMap',
    },

    '28': {
        'tile': 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',
        'attrib': 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
        'name': 'Esri_WorldGrayCanvas',
    },

    '29': {
        'tile': 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_Positron',
    },

    # '30': {
    #     'tile': 'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png',
    #     'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    #     'name': 'peta 30',
    # },

    # '31': {
    #     'tile': 'https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png',
    #     'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    #     'name': 'peta 31',
    # },

    '32': {
        'tile': 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_DarkMatter',
    },

    '33': {
        'tile': 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_DarkMatterNoLabels',
    },

    # '34': {
    #     'tile': 'https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}{r}.png',
    #     'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    #     'name': 'peta 34',
    # },

    '35': {
        'tile': 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_Voyager',
    },

    '36': {
        'tile': 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_VoyagerNoLabels',
    },

    '37': {
        'tile': 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_VoyagerOnlyLabels',
    },

    '38': {
        'tile': 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        'name': 'CartoDB_VoyagerLabelsUnder',
    },

    '39': {
        'tile': 'https://tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png',
        'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        'name': 'HikeBike_HikeBike',
    },

    # '40': {
    #     'tile': 'https://maps{s}.wien.gv.at/basemap/geolandbasemap/normal/google3857/{z}/{y}/{x}.png',
    #     'attrib': 'Datenquelle: <a href="https://www.basemap.at">basemap.at</a>',
    #     'name': 'peta 40',
    # },

    # '41': {
    #     'tile': 'https://maps{s}.wien.gv.at/basemap/bmapgrau/normal/google3857/{z}/{y}/{x}.png',
    #     'attrib': 'Datenquelle: <a href="https://www.basemap.at">basemap.at</a>',
    #     'name': 'peta 41',
    # },

    # '42': {
    #     'tile': 'https://maps{s}.wien.gv.at/basemap/bmapoverlay/normal/google3857/{z}/{y}/{x}.png',
    #     'attrib': 'Datenquelle: <a href="https://www.basemap.at">basemap.at</a>',
    #     'name': 'peta 42',
    # },

    # '43': {
    #     'tile': 'https://maps{s}.wien.gv.at/basemap/bmaphidpi/normal/google3857/{z}/{y}/{x}.png',
    #     'attrib': 'Datenquelle: <a href="https://www.basemap.at">basemap.at</a>',
    #     'name': 'peta 43',
    # },

    '44': {
        'tile': 'https://maps{s}.wien.gv.at/basemap/bmaporthofoto30cm/normal/google3857/{z}/{y}/{x}.jpeg',
        'attrib': 'Datenquelle: <a href="https://www.basemap.at">basemap.at</a>',
        'name': 'BasemapAT_orthofoto',
    },

    '45': {
        'tile': 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}{r}.png',
        'attrib': '<a href="https://wikimediafoundation.org/wiki/Maps_Terms_of_Use">Wikimedia</a>',
        'name': 'Wikimedia'
    },

    # mau nlmaps.standaard...55% lah
    # https://leaflet-extras.github.io/leaflet-providers/preview/
    # '45': {
    #     'tile': 'https://maps{s}.wien.gv.at/basemap/geolandbasemap/normal/google3857/{z}/{y}/{x}.png',
    #     'attrib': 'Datenquelle: <a href="https://www.basemap.at">basemap.at</a>'
    # },
    # ada open fire map
    # var OpenFireMap = L.tileLayer('http://openfiremap.org/hytiles/{z}/{x}/{y}.png', {
    #     maxZoom: 19,
    #     attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors | Map style: &copy; <a href="http://www.openfiremap.org">OpenFireMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    # });

    # minta time di sini
    '99': {
        'tile': 'https://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_CityLights_2012/default/{time}/{tilematrixset}{maxZoom}/{z}/{y}/{x}.jpg',
        'attrib': 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
        'name': 'NASAGIBS_ViirsEarthAtNight2012',
    },
}

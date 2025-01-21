from schnell.app.compressutils import gz, ungz, bz, unbz, zip5, unzip5


zip = zip5
unzip = unzip5

def compressor(request, bungkus=gz, bongkar=ungz):
    """
    /gz)
        ... = request
    /gz)input>output
    /gz)input>
        compress
    /gz)output<input
    /gz)output<input,ext to remove
    /gz)<input,ext to remove
        uncompress, bisa juga terima ext yg mau/perlu diremove
    """
    # mode = 'compress'
    if '>' in request:
        fileinput, fileoutput = [item.strip() for item in request.split('>')]
        if fileoutput:
            bungkus(fileinput, fileoutput)
        else:
            bungkus(fileinput)
    elif '<' in request:
        fileuncompress, filecompressed = [item.strip() for item in request.split('<')]
        # mode = 'uncompress'
        ext_to_remove = ''
        test_mode = False
        if filecompressed.endswith('*'):
            test_mode = True
            filecompressed = filecompressed.removesuffix('*')
        if ',' in filecompressed:
            filecompressed, ext_to_remove = [item.strip() for item in filecompressed.split(',')]
        if fileuncompress:
            if ext_to_remove:
                bongkar(filecompressed, fileuncompress, ext_to_remove)
            else:
                bongkar(filecompressed, fileuncompress)
        else:
            if test_mode:
                '''
                /zip)<python.zip*
                '''
                bongkar(filecompressed, dont_extract=True)
            else:
                bongkar(filecompressed)


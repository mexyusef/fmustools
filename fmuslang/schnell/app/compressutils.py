import os, sys, shutil
import zlib
import bz2
import lzma
import gzip
from .dirutils import tempdir
from .printutils import pp
"""
1 zlib
2 bz2
3 lzma/xz
4 gzip

https://tukaani.org/lzma/benchmarks.html

When there's need for a very fast compression, gzip is the clear winner. 
It has also very small memory footprint, making it ideal for systems with limited memory.

Decompression
In terms of speed, gzip is the winner again

https://towardsdatascience.com/all-the-ways-to-compress-and-archive-files-in-python-e8076ccedb4b
zlib is a library and Python module that provides code for working with Deflate compression and decompression format which is used by zip, gzip and many others. So, by using this Python module, you're essentially using gzip compatible compression algorithm without the convenient wrapper. More about this library can be found on Wikipedia.

bz2 is a module that provides support for bzip2 compression. This algorithm is generally more effective than the deflate method, but might be slower. It also works only on individual files and therefore can't create archives.

lzma is both name of the algorithm and Python module. It can produce higher compression ratio than some older methods and is the algorithm behind the xz utility (more specifically LZMA2).

gzip is a utility most of us are familiar with. It's also a name of a Python module. This module uses the already mentioned zlib compression algorithm and serves as an interface similar to the gzip and gunzip utilities.

shutils is a module we generally don't associate with compression and decompression, but it provides utility methods for working with archives and can be a convenient way for producing tar, gztar, zip, bztar or xztar archives.

zipfile - as the name suggests - allows us to work with zip archives in Python. This module provides all the expected methods for creating, reading, writing or appending to ZIP files as well as classes and objects for easier manipulation of such files.

tarfile - as with zipfile above, you can probably guess that this module is used for working with tar archives. It can read and write gzip, bz2 and lzma files or archives. It also has support for other features we know from tar utility - list of those is available at the top of above linked docs page.
"""

### zlib
def zip1(filename_in = "data", filename_out = "compressed_data"):
    with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
        data = fin.read()
        compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        print(f"Original size: {sys.getsizeof(data)}")
        # Original size: 1000033
        print(f"Compressed size: {sys.getsizeof(compressed_data)}")
        # Compressed size: 1024
        fout.write(compressed_data)

def unzip1(filename_out = "compressed_data"):
    with open(filename_out, mode="rb") as fin:
        data = fin.read()
        compressed_data = zlib.decompress(data)
        print(f"Compressed size: {sys.getsizeof(data)}")
        # Compressed size: 1024
        print(f"Decompressed size: {sys.getsizeof(compressed_data)}")
        # Decompressed size: 1000033


### bz2
def zip2(filename_in = "data", filename_out = "compressed_data.bz2"):
    with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
        fout.write(fin.read())

    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    # Uncompressed size: 1000000
    print(f"Compressed size: {os.stat(filename_out).st_size}")
    # Compressed size: 48

def unzip2(filename_out = "compressed_data.bz2"):
    data = None
    with bz2.open(filename_out, "rb") as fin:
        data = fin.read()
        print(f"Decompressed size: {sys.getsizeof(data)}")
        # Decompressed size: 1000033
    return data


### xz
lzc = lzma.LZMACompressor()
# cat /usr/share/dict/words | sort -R | head -c 1MB > data

def zip3(filename_in = "data", filename_out = "compressed_data.xz"):
    with open(filename_in, mode="r") as fin, open(filename_out, "wb") as fout:
        for chunk in fin.read(1024):
            compressed_chunk = lzc.compress(chunk.encode("ascii"))
            fout.write(compressed_chunk)
        fout.write(lzc.flush())

    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    # Uncompressed size: 972398
    print(f"Compressed size: {os.stat(filename_out).st_size}")
    # Compressed size: 736

def unzip3(filename_out = "compressed_data.xz"):
    with lzma.open(filename_out, "r") as fin:
        words = fin.read().decode("utf-8").split()
        print(words[:5])
        # ['dabbing', 'hauled', "seediness's", 'Iroquoian', 'vibe']


### gz
def zip4(filename_in = "data", filename_out = "compressed_data.tar.gz"):
    with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:
        # Reads the file by chunks to avoid exhausting memory
        # thanks to shutil.copyfileobj we get the chunked incremental compression without having to loop over the data like we did with lzma.
        shutil.copyfileobj(fin, fout)

    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    # Uncompressed size: 1000000
    print(f"Compressed size: {os.stat(filename_out).st_size}")
    # Compressed size: 1023

def unzip4(filename_out = "compressed_data.tar.gz"):
    data = None
    with gzip.open(filename_out, "rb") as fin:
        data = fin.read()
        print(f"Decompressed size: {sys.getsizeof(data)}")
        # Decompressed size: 1000033
    return data


import zipfile

# shuf -n5 /usr/share/dict/words > words.txt
# files = ["words1.txt", "words2.txt", "words3.txt", "words4.txt", "words5.txt"]
def zip5(files=[], archive = "output.zip", password = None, only_basename=True):
    """
    only_basename=True
    krn ternyata ini zipper memasukkan absolute path ke dalam zip...
    lambda aws jd tdk bs menemukan module karenanya
    
    we start by creating ZIP archive using ZipFile context manager in "write" ( w) mode and then add the files to this archive. You will notice that we didn't actually need to open the files that we're adding - all we needed to do is call write passing in the file name. After adding all the files, we also set archive password using setpassword method.

    In addition to creating a reading archives/files, ZIP allows us to also append files to existing archives. To do this, all we need to change is access mode to “append” ("a"):
    with zipfile.ZipFile(archive, "a") as zf:
        zf.write("words6.txt")
        print(zf.namelist())
        # ['words1.txt', 'words2.txt', 'words3.txt', 'words4.txt', 'words5.txt', 'words6.txt']
    """
    with zipfile.ZipFile(archive, "w") as zf:
        for file in files:
            if only_basename:
                zf.write(file, os.path.basename(file))
            else:
                zf.write(file)
        if password:
            zf.setpassword(password.encode('utf8'))

def unzip5(archive = "archive.zip", outfolder=tempdir(), password = None, dont_extract=False):
    """
    we open the archive. 
    Before reading any files we check CRC and file headers, 
    afterwards we retrieve information about all files present in the archive. 
    In this example we just print the list of ZipInfo objects, 
    but you could also inspect its attributes to get CRC, size, compression type, etc.
    After checking all the files we open and read one of them. 
    We see that it has the expected content, 
    so we can go ahead and extract it to file specified by path (/tmp/).
    """
    with zipfile.ZipFile(archive, "r") as zf:
        crc_test = zf.testzip()
        if crc_test is not None:
            print(f"Bad CRC or file headers: {crc_test}")

        info = zf.infolist()  # also zf.namelist()
        pp(info)  # See all attributes at https://docs.python.org/3/library/zipfile.html#zipinfo-objects
        # [ <ZipInfo filename='words1.txt' filemode='-rw-r--r--' file_size=37>,
        #   <ZipInfo filename='words2.txt' filemode='-rw-r--r--' file_size=47>,
        #   ... ]
        if not dont_extract:
            file = info[0]
            with zf.open(file) as f:
                print(f.read().decode())
                # Olav
                # teakettles
                # ...
            if password:
                zf.extract(file, outfolder, pwd=password.encode('utf8'))  # also zf.extractall()
            else:
                zf.extract(file, outfolder)

import tarfile

files = ["words1.txt", "words2.txt", "words3.txt", "words4.txt"]
def zip6(files, archive = "archive.tar.gz"):
    # we use access mode "w:gz" which specifies that we want to use GZ compression
    with tarfile.open(archive, "w:gz") as tar:
        # we add all our files to the archive. 
        # With tarfile module we can also pass in for example symlinks or whole directories that would be recursively added.
        for file in files:
            tar.add(file)  # can also be dir (added recursively), symlink, etc

        #  to confirm that all the files are really there, we use getmembers method. 
        # To get insight about individual files we can use gettarinfo, which provides all the Linux file attributes.
        print(f"archive contains: {tar.getmembers()}")
        # [<TarInfo 'words1.txt' at 0x7f71ed74f8e0>,
        #  <TarInfo 'words2.txt' at 0x7f71ed74f9a8>
        #  ... ]

        info = tar.gettarinfo("words1.txt")  # Other Linux attributes - https://docs.python.org/3/library/tarfile.html#tarinfo-objects
        # we change permission of a file by supplying filter argument which modifies the TarInfo.mode. 
        # This value has to be provided as octal number, here 0o100600 sets the permissions to 0600 or -rw-------..
        print(f"{tar.name} contains {info.name} with permissions {oct(info.mode)[-3:]}, size: {info.size} and owner: {info.uid}:{info.gid}")
        # .../archive.tar contains words1.txt with permissions 644, size: 37 and owner: 500:500

        def change_permissions(tarinfo):
            tarinfo.mode = 0o100600  # -rw-------.
            return tarinfo
        # To get the complete overview of files after doing this change we can run list method, which gives us output similar to ls -l.
        tar.add("words5.txt", filter=change_permissions)

        tar.list()
        # -rw-r--r-- martin/martin   37 2021-08-23 09:01:56 words1.txt
        # -rw-r--r-- martin/martin   47 2021-08-23 09:02:06 words2.txt
        # ...
        # -rw------- martin/martin   42 2021-08-23 09:02:22 words5.txt

def unzip6(archive, outfolder='/tmp'):
    """
    we open it with "r:gz" mode, 
    retrieve an info object ( member) using file name, 
    check whether it really is a file 
    and extract it to desired location
    """
    with tarfile.open(archive, "r:gz") as tar:
        member = tar.getmember("words3.txt")
        if member.isfile():
            tar.extract(member, outfolder)

# https://www.thepythoncode.com/article/compress-decompress-files-tarfile-python
# import tarfile
from tqdm import tqdm # pip3 install tqdm

def zip7(tar_file, members):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()
def unzip7(tar_file, path, members=None):
    """
    Extracts `tar_file` and puts the `members` to `path`.
    If members is None, all members on `tar_file` will be extracted.
    """
    tar = tarfile.open(tar_file, mode="r:gz")
    if members is None:
        members = tar.getmembers()
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        tar.extract(member, path=path)
        # set the progress description of the progress bar
        progress.set_description(f"Extracting {member.name}")
    # or use this
    # tar.extractall(members=members, path=path)
    # close the file
    tar.close()

def gz(fileinput, fileoutput=None, ext_to_remove='.gz'):
    if not fileoutput:
        fileoutput = fileinput + ext_to_remove
    zip4(fileinput, fileoutput)

def ungz(filecompressed, fileuncompress=None, ext_to_remove='.gz'):
    if not fileuncompress:
        fileuncompress = filecompressed.removeprefix(ext_to_remove)
    from .fileutils import file_write
    data = unzip4(filecompressed)
    if data:
        file_write(fileuncompress, data, 'wb')

def bz(fileinput, fileoutput=None, ext_to_remove='.bz2'):
    if not fileoutput:
        fileoutput = fileinput + ext_to_remove
    zip2(fileinput, fileoutput)

def unbz(filecompressed, fileuncompress=None, ext_to_remove='.bz2'):
    if not fileuncompress:
        fileuncompress = filecompressed.removeprefix(ext_to_remove)
    from .fileutils import file_write
    data = unzip2(filecompressed)
    if data:
        file_write(fileuncompress, data, 'wb')

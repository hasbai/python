import os, shutil, re
from rarfile import RarFile
from zipfile import ZipFile


def get_dirs(dir):
    dirs = []
    for name in os.listdir(dir):
        if os.path.isdir(name) and name[0] != '.': dirs.append(name)
    return dirs

def get_files(dir):
    files = []
    for name in os.listdir(dir):
        if os.path.isfile(name) and name[0] != '.' : files.append(name)
    return files

def unzip(name):
    with ZipFile(name, 'r') as f:
        namelist = f.namelist()
        if namelist[0][-1] == '/':
            cwd = os.getcwd()
            dirname = namelist[0][:-1]
            try: 
                os.mkdir(dirname)
            except: 
                pass
            os.chdir(dirname)
        for name in namelist:
            try:
                new_name = name.encode('cp437').decode('gbk')
            except:
                new_name = name
            new_name = new_name.split('/')[-1]
            if not new_name: continue
            with open(new_name, 'wb') as outputFile:
                with f.open(name, 'r') as inputFile:
                    shutil.copyfileobj(inputFile, outputFile)
        if namelist[0][-1] == '/':
            os.chdir(cwd)

def extract(dir):
    for name in get_files(dir):
        mime = name.split('.')[-1]
        if mime == 'rar':
            with RarFile(name, 'r') as f:
                f.extractall()
        if mime == 'zip':
            unzip(name)

def files():
    cwd = os.getcwd()

    for name in get_files(cwd):
        if re.findall('（.+）', name):
            for n in re.findall('（.+）', name):
                if len(n) > 15:
                    os.rename(name, name.replace(n, ''))
                    print(name)
 
    dirs = get_dirs(cwd)
    while dirs:
        os.chdir(os.path.join(cwd, dirs[0]))
        dirs.pop(0)
        files()
    
    
os.chdir('/mnt/hgst1/电子书/亚马逊镇店之宝系列')
files()



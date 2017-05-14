source = None #Set this to your web source

import zipfile
import os
import urllib2

def uqg(path):
    f = urllib2.urlopen(path)
    data=f.read()
    f.close()
    return data

def qg(path):
    f = open(path)
    data=f.read()
    f.close()
    return data

def version():
    if not os.path.isfile('version'):
        return 0
    else:
        return int(qg('version').strip())

def check_update():
    far_version = int(uqg(source+'/version').strip())
    return far_version > version()

def update():
    f=open('temp.zip','wb')
    f.write(uqg(source+'/archive.zip'))
    f.close()
    z = zipfile.ZipFile('temp.zip')
    z.extractall()
    os.remove('temp.zip')
    

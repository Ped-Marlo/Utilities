# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:35:37 2020

@author: Pedro Martinez
"""
from os import listdir
from os.path import isfile, join

folderpath = r'Z:\aie_load\A350\A350-XWB\Bricks\Site-Componentes\LGD\Multi-conf\Becario_Pedro\archivos_explorar\1024.zip'
#folderpath = r'Z:\aie_load\A350\A350-XWB'
extension = "cdf"

def search (folderpath= folderpath, extension=extension):
    if folderpath.endswith('.zip'):
        import zipfile
        ziper = zipfile.ZipFile(folderpath)
        all_files = ziper.namelist()
        ext_files = [f for f in all_files if f.endswith(extension)]
        
        
    else:
        import glob
        all_files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
        
        ext_files = glob.glob(folderpath+"\\*."+extension)
        
    return all_files, ext_files

all_files, ext_files = search()

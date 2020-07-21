# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:35:37 2020

@author: ng8569f
"""
from os import listdir
from os.path import isfile, join

#folderpath = r'Z:\aie_load\A350\A350-XWB\Bricks\Site-Componentes\LGD\Multi-conf\Becario_Pedro\archivos_explorar\1024.zip'
folderpath = r'Z:\aie_load\A350\A350-XWB'
if folderpath.endswith('.zip'):
        import zipfile
        ziper = zipfile.ZipFile(folderpath)
        all_files = ziper.namelist()
        
        
        
else:
    import glob
    extension = "*.pdf"
    all_files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    
    ext_files = glob.glob(folderpath+"\\"+extension)
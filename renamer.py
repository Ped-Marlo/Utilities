# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:43:34 2020

@author: c40441
"""

import os
#F stands for names of folders where files need to be renamed
for F in ['Retraction_right','Retraction_left','Extension_right','Extension_left']:
     for n in [1,2,3]:
          basedir0 = r"Z:\ba_NG8569F_Pedro\A350_MLGD_Multiflap_effect\900"
          basedir1=os.path.join(basedir0,F)
          basedir=os.path.join(basedir1,"BayesianRidge\order"+str(n))



          a=os.listdir(basedir)
          for fn in a:
               a1=fn.replace('n_iter=1000,','').rstrip(',')
               try:
                    os.rename(os.path.join(basedir, fn), os.path.join(basedir, a1))
               except FileExistsError:
          #          os.remove(os.path.join(basedir, fn))
                    os.rename(os.path.join(basedir, fn), os.path.join(basedir, '1'+a1))
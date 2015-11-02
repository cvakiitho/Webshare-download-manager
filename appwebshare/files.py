# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
import glob
from appwebshare.scripts import config

def get_file_list():
    without_dir = []
    for i in glob.glob(config.DIR + '*.*') :
        without_dir.append(i.replace(config.DIR, ""))
    return without_dir
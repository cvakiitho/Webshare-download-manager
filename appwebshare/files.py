# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
import glob
import config


def get_file_list():
    without_dir = []
    for i in glob.glob(config.DIR + '*.avi') + glob.glob(config.DIR + '*.mkv') + glob.glob(config.DIR + '*.mp4'):
        without_dir.append(i.replace(config.DIR, ""))
    return without_dir
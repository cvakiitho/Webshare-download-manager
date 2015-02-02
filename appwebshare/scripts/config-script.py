# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
import fileinput


def config():
    name = 'NAME = \"' + raw_input('enter your webshare name') + '\"'
    password = 'PASSWORD = \"' + raw_input('enter your webshare password hash') + '\"'
    dir_files = 'DIR = \"' + raw_input('enter directory to store files') + '\"'
    login = 'LOGIN = \"' + raw_input('enter login to this webapp') + '\"'
    flask_password = 'PASS = \"' + raw_input('enter password for this webapp') + '\"'

    for line in fileinput.input('config.py', inplace=True):
        if 'NAME =' in line:
            print name
        elif 'PASSWORD =' in line:
            print password
        elif 'DIR =' in line:
            print dir_files
        elif 'LOGIN =' in line:
            print login
        elif 'PASS =' in line:
            print flask_password
        else:
            print line,


config()
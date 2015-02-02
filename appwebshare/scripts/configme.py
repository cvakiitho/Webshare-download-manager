# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
import fileinput
import site


if site.getsitepackages()[0][0] == '/':
    path = site.getsitepackages()[0] + '/appwebshare/scripts/'
else:
    path = site.getsitepackages()[1] + '\\appwebshare\\scripts\\'


def main():
    name = 'NAME = \"' + raw_input('enter your webshare name') + '\"'
    password = 'PASSWORD = \"' + raw_input('enter your webshare password hash') + '\"'
    dir_files = 'DIR = \"' + raw_input('enter directory to store files') + '\"'
    login = 'LOGIN = \"' + raw_input('enter login to this webapp') + '\"'
    flask_password = 'PASS = \"' + raw_input('enter password for this webapp') + '\"'

    for line in fileinput.input(path + 'config.py', inplace=True):
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


if __name__ == '__main__':
    main()
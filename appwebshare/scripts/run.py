# -*- coding: UTF=8 -*-
_author__ = 'Tomas Hartmann'
from appwebshare import app

def main():
    app.run(host='localhost', port=5000, debug=True)


if __name__ == '__main__':
    main()

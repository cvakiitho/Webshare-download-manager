# -*- coding: UTF=8 -*-
_author__ = 'Tomas Hartmann'
from appwebshare import app


def production():
    app.run(host='0.0.0.0', port=5000, debug=False)


def dev():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    production()

# -*- coding: UTF=8 -*-
_author__ = 'Tomas Hartmann'
from appwebshare import app

def run():
    app.run(host='localhost', port=5000, debug=True)

run()

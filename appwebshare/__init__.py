# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
from flask import Flask

app = Flask(__name__)
app.secret_key = '\xc8V\xa2\xf6\xe2\x82U}QF<\xeb\x9e\x98\x02-\x01\xe2\xff\x99\xa9\xc1n\xe4'

import appwebshare.views
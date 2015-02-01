# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
from setuptools import setup, find_packages

setup(name='webshare-download-manager',
      version='0.1.3',
      description='Download manager for webshare.cz site. Flask + requests.',
      url='https://github.com/cvakiitho/Webshare-download-manager',
      author='Tomas Hartmann',
      author_email='cvakiitho@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'Flask>=0.10.1',
          'Jinja2>=2.7.3',
          'requests>=2.5.1'
      ]
)
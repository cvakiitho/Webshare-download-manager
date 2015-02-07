# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
from setuptools import setup, find_packages

setup(name='webshare-download-manager',
      version='0.2.1',
      description='Download manager for webshare.cz site. Flask + requests.',
      url='https://github.com/cvakiitho/Webshare-download-manager',
      author='Tomas Hartmann',
      author_email='cvakiitho@gmail.com',
      license='LICENSE.txt',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'Flask>=0.10.1',
          'Jinja2>=2.7.3',
          'requests>=2.5.1'],
      include_package_data=True,
      entry_points = {
        'console_scripts': [
            'config_server = appwebshare.scripts.configme:main',
            'run_server = appwebshare.scripts.run:production',
            'run_dev = appwebshare.scripts.run:dev'
        ]
      },
      package_data={
         'templates': 'appwebshare/templates/*',
        },


)
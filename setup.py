# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
from setuptools import setup, find_packages

setup(name='webshare-download-manager',
      version='0.1.5',
      description='Download manager for webshare.cz site. Flask + requests.',
      url='https://github.com/cvakiitho/Webshare-download-manager',
      author='Tomas Hartmann',
      author_email='cvakiitho@gmail.com',
      license='LICENSE.txt',
      long_description=open("README.md").read(),
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'Flask>=0.10.1',
          'Jinja2>=2.7.3',
          'requests>=2.5.1'],
      include_package_data=True,
      entry_points = {
        'console_scripts': [
            'load_data = appwebshare.scripts.config:config',
            'run_server = appwebshare.scripts.run:run'
        ]
      },
      package_data={
         'templates': 'appwebshare/templates/*',
        },


)
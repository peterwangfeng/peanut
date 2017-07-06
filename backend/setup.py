# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='peanut',
      version='0.1.0',
      description='花生米',
      url='www.easestrategy.com',
      author='EaseStrategy',
      author_email='contact@easestrategy.com',
      packages=['peanut'],
      package_data={
          '': ['*.py']
      },
      install_requires=[
                        'Flask==0.12',
                        'cx_Oracle==6.0rc1'
                        'redis==2.10.5',
                        'setuptools==20.10.1',
                        ],
      zip_safe=False)

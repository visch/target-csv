#!/usr/bin/env python

from setuptools import setup

setup(name='target-csv',
      version='0.3.3',
      description='Singer.io target for writing CSV files',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_csv'],
      install_requires=[
          'jsonschema==2.6.0',
          'singer-python>=5.1.0,<=5.3.1',
      ],
      entry_points='''
          [console_scripts]
          target-csv=target_csv:main
      ''',
)

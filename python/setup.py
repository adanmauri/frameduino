#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from setuptools import setup

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, '..', 'README.md')) as f:
    long_description = f.read()

setup(
    name='frameduino',
    version='0.2.3',
    description='Pinguino Board Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Adán Mauri Ungaro',
    author_email='adan.mauri@gmail.com',
    url='https://github.com/adanmauri/frameduino',
    packages=['frameduino', 'frameduino.drivers'],
    license='GPLv3'
)

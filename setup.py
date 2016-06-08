#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup

name='sslexpire'
description='Utility for checking how long until an SSL certificate expires.'
version='1'

author='Benedicte Emilie BrÃ¦kken'
author_email='b.e.brakken@usit.uio.no'

scripts=['bin/sslexpire']

setup(name=name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      scripts=scripts)

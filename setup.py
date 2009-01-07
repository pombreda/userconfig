#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2009 Pierre Raybaut
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
userconfig
==========

Module handling configuration files based on ConfigParser

Copyright © 2009 Pierre Raybaut
This software is licensed under the terms of the GNU General Public
License version 3 as published by the Free Software Foundation.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import userconfig

setup(
      name = 'userconfig',
      version = userconfig.__version__,
      description = 'Managing *easily* user configuration files (based on ConfigParser)',
      author = "Pierre Raybaut",
      author_email = 'contact@pythonxy.com',
      url = 'http://code.google.com/p/userconfig/',
      license = 'GPLv3',
      keywords = 'configuration file parser',
      platforms = ['any'],
      py_modules = ['userconfig','userconfig_test'],
      classifiers = ['Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.5',
        ],
    )

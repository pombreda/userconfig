#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
userconfig example
See 'test' module for more examples
"""

from userconfig import UserConfig

OPTIONS = [('Font',
            {'custom' : True,
             'family' : ['Arial', 'Verdana'],
             'size' : 10,
             'weight' : 'bold',
             }),
           ('Linestyle',
            {'width' : 2.5,
             'style' : 'dash',
             'color' : 'blue',
             }),
           ]

# Creating automatically a .ini file in user home directory
# named '.app_name.ini' containing options listed above:
# (if the .ini file already exists, its contents will override
# those defined above)
CONFIG = UserConfig('app_name', OPTIONS)
# or, you may (optional) add a version number to your configuration:
# (note that this will be the version number of the configuration file,
#  not of your application! -- at least if you want to keep user old settings)
# (when the version number change, the deprecated options are removed --
#  here 'deprecated' means: not present in defaults values - here 'OPTIONS')
CONFIG = UserConfig('app_name', OPTIONS, version='1.0.2')


# How to get options from .ini file:
print 'Custom font:', 'yes' if CONFIG.get('Font', 'custom') else 'no'
print 'Font family:', CONFIG.get('Font', 'family')

# How to get an option default value:
# (if .ini file wasn't modified externaly, result will be the same
# as the two previous lines)
print 'Custom font:', 'yes' if CONFIG.get_default('Font', 'custom') else 'no'
print 'Font family:', CONFIG.get_default('Font', 'family')

# Set an option:
CONFIG.set('Font', 'size', 18)

# Reset configuration to default options:
# (i.e. overwrite the current .ini file with default settings)
CONFIG.reset_to_defaults()

# Reset configuration to default options without overwriting
# the current .ini file settings:
CONFIG.reset_to_defaults(save=False)

# Removing .ini file (e.g. before uninstalling the application):
CONFIG.cleanup()

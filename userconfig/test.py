#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
userconfig unit tests
"""

import unittest, os

from userconfig import UserConfig

OPTIONS1 = {
            'category1/list' : [5, "kk"],
            'category1/tuple' : (None, "foo"),
            'category1/float' : 12.3,
            'category1/bool' : True,
            'category2/int' : 50,
            'category2/str' : 'text text',
            'category3/unicode' : u'ééǿùùàà',
            }

OPTIONS2 = [ ('category1',
              {'float' : 12.3,
               'bool' : True,
               }),
             ('category2',
              {'int' : 50,
               'str' : 'text text',
               }),
             ('category3',
              {'unicode' : u'ééǿùùàà',
               }),
            ]


def conf_modified_by_user(version=None):
    conf = UserConfig('testconfig2', OPTIONS2, version=version)
    conf_file = file(conf.filename())
    lines = conf_file.readlines()
    conf_file.close()
    lines = [line.replace('text text','other text') for line in lines]
    conf_file = file(conf.filename(),'w')
    conf_file.writelines(lines)
    conf_file.close()
    return UserConfig('testconfig2', OPTIONS2, version=version)

class TestFile(unittest.TestCase):
    def test_exist1(self):
        conf = UserConfig('testconfig1', OPTIONS1)
        self.assertTrue( os.path.isfile(conf.filename()) )
        
    def test_exist2(self):
        conf = UserConfig('testconfig2', OPTIONS2)
        self.assertTrue( os.path.isfile(conf.filename()) )
        
    def test_cleanup(self):
        conf = UserConfig('testconfig1', OPTIONS1)
        conf.cleanup()
        self.assertTrue( not os.path.isfile(conf.filename()) )
        
    def test_modified_by_user(self):
        conf = conf_modified_by_user()
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'other text')
        
    def test_reset_to_defaults(self):
        conf = conf_modified_by_user()
        conf.reset_to_defaults()
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'text text')
        
    def test_get_default(self):
        conf = conf_modified_by_user()
        o_str_default = conf.get_default('category2', 'str')
        self.assertEquals(o_str_default, 'text text')
        
    def test_load(self):
        conf_modified_by_user()
        conf = UserConfig('testconfig2', OPTIONS2)
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'other text')
        
    def test_load_false(self):
        conf_modified_by_user()
        conf = UserConfig('testconfig2', OPTIONS2, load=False)
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'text text')
        
    def test_new_config_version(self):
        conf_modified_by_user()
        conf = UserConfig('testconfig2', OPTIONS2, version='1.0.1')
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'text text')
        
    def test_changed_config_version(self):
        conf_modified_by_user(version='1.0.0')
        conf = UserConfig('testconfig2', OPTIONS2, version='1.0.1')
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'text text')
        
    def test_same_config_version(self):
        conf_modified_by_user(version='1.0.1')
        conf = UserConfig('testconfig2', OPTIONS2, version='1.0.1')
        o_str = conf.get('category2', 'str')
        self.assertEquals(o_str, 'other text')


class TestOptions1(unittest.TestCase):

    def setUp(self):
        self.conf = UserConfig('testconfig1', OPTIONS1)
        
    def tearDown(self):
        self.conf.cleanup()
        
    def test_get_list(self):
        o_list = self.conf.get(None, 'category1/list')
        self.assertEquals(o_list, [5, "kk"])

    def test_set_list(self):
        self.conf.set(None, 'category1/list', [14.5, "jj"])
        o_list = self.conf.get(None, 'category1/list')
        self.assertEquals(o_list, [14.5, "jj"])

    def test_get_tuple(self):
        o_tuple = self.conf.get(None, 'category1/tuple')
        self.assertEquals(o_tuple, (None, "foo"))

    def test_set_tuple(self):
        self.conf.set(None, 'category1/tuple', (False, 1238, 3.5))
        o_tuple = self.conf.get(None, 'category1/tuple')
        self.assertEquals(o_tuple, (False, 1238, 3.5))
        
    def test_get_float(self):
        o_float = self.conf.get(None, 'category1/float')
        self.assertEquals(o_float, 12.3)

    def test_set_float(self):
        self.conf.set(None, 'category1/float', 14.5)
        o_float = self.conf.get(None, 'category1/float')
        self.assertEquals(o_float, 14.5)

    def test_get_int(self):
        o_int = self.conf.get(None, 'category2/int')
        self.assertEquals(o_int, 50)

    def test_set_int(self):
        self.conf.set(None, 'category2/int', 10.0)
        o_int = self.conf.get(None, 'category2/int')
        self.assertEquals(o_int, 10)

    def test_get_bool(self):
        o_bool = self.conf.get(None, 'category1/bool')
        self.assertEquals(o_bool, True)

    def test_set_bool(self):
        self.conf.set(None, 'category1/bool', False)
        o_bool = self.conf.get(None, 'category1/bool')
        self.assertEquals(o_bool, False)

    def test_get_str(self):
        o_str = self.conf.get(None, 'category2/str')
        self.assertEquals(o_str, 'text text')

    def test_set_str(self):
        self.conf.set(None, 'category2/str', 'foobar')
        o_str = self.conf.get(None, 'category2/str')
        self.assertEquals(o_str, 'foobar')

    def test_get_unicode(self):
        o_unicode = self.conf.get(None, 'category3/unicode')
        self.assertEquals(o_unicode, u'ééǿùùàà')

    def test_set_unicode(self):
        self.conf.set(None, 'category3/unicode', u'ééǿùùàà')
        o_unicode = self.conf.get(None, 'category3/unicode')
        self.assertEquals(o_unicode, u'ééǿùùàà')


class TestOptions2(unittest.TestCase):

    def setUp(self):
        self.conf = UserConfig('testconfig2', OPTIONS2, load=False)
        
    def tearDown(self):
        self.conf.cleanup()
        
    def test_get_float(self):
        o_float = self.conf.get('category1', 'float')
        self.assertEquals(o_float, 12.3)

    def test_set_float(self):
        self.conf.set('category1', 'float', 14.5)
        o_float = self.conf.get('category1', 'float')
        self.assertEquals(o_float, 14.5)

    def test_get_int(self):
        o_int = self.conf.get('category2', 'int')
        self.assertEquals(o_int, 50)

    def test_get_bool(self):
        o_bool = self.conf.get('category1', 'bool')
        self.assertEquals(o_bool, True)

    def test_get_str(self):
        o_str = self.conf.get('category2', 'str')
        self.assertEquals(o_str, 'text text')

    def test_get_unicode(self):
        o_unicode = self.conf.get('category3', 'unicode')
        self.assertEquals(o_unicode, u'ééǿùùàà')

    def test_get_default(self):
        o_default = self.conf.get('category3', 'unknown', default=23)
        self.assertEquals(o_default, 23)


if __name__ == "__main__":
    unittest.main()


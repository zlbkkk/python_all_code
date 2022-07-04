import ddt
import unittest

import  unittest



# data = ['test_001', '获取广告位', 'yes', None, None, 'api3/getbanneradvertver2']






data =({'first':1,'second':2},{'first':3,'second':4})

@ddt.ddt
class FooTestCase(unittest.TestCase):

    @ddt.unpack # 从字典中取值要加上这个
    @ddt.data(*data)
    def test_show_value(self, first,second):
        print('value is %s和%s' %(first,second))
        print('case is over.\n')

if __name__ == '__main__':
    unittest.main()

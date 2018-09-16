# 测试Python mock

from unittest import mock
import unittest

from moduleMock import AddSum, Computer

class TestCount(unittest.TestCase):

    def test_add(self):
        addsum = AddSum()
        # add 函数没开始写时，我们可以先mock一个值
        addsum.sum = mock.Mock(return_value=13)
        result = addsum.sum(8,5)
        self.assertEqual(result,13)


class PersonTest(unittest.TestCase):
    def test_should_get_price(self):
        pc = Computer()
        
        # 不mock时，get_price应该返回5000
        self.assertEqual(pc.get_price(), 5000)
        
        # mock掉get_price方法，让它返回2000
        pc.get_price = mock.Mock(return_value=2000)
        self.assertEqual(pc.get_price(), 2000)
    
        
if __name__ == '__main__':
    unittest.main()


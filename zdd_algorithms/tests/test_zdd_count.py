import unittest
import zdd
f = frozenset

class TestZddCount(unittest.TestCase):

    def test_normal_case(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,3})}
        zdd1 = zdd.to_zdd(set1)
        count = zdd.count(zdd1)
        self.assertEqual(3, count)

    def test_small(self):
        zdd1 = zdd.get_node(4,zdd.get_node(1,zdd.empty(),zdd.base()),zdd.get_node(2,zdd.empty(),zdd.base()))
        count = zdd.count(zdd1)
        self.assertEqual(2, count)

    def test_empty(self):
        self.assertEqual(0, zdd.count(zdd.empty()))

    def test_base(self):
        self.assertEqual(1, zdd.count(zdd.base()))
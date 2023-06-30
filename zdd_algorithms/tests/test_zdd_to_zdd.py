import unittest
import zdd
f = frozenset

class TestZddToZdd(unittest.TestCase):
    
    def test_normal_case(self):
        set1 = {f({1}),f({2,4})}
        zdd1 = zdd.to_zdd(set1)
        self.assertEqual(2, zdd.count(zdd1))
        expected_result = zdd.get_node(4,zdd.get_node(1,zdd.empty(),zdd.base()),zdd.get_node(2,zdd.empty(),zdd.base()))
        self.assertEqual(expected_result, zdd1)

    def test_empty_set(self):
        set1 = set()
        zdd1 = zdd.to_zdd(set1)
        self.assertEqual(0, zdd.count(zdd1))
        self.assertEqual(zdd.empty(), zdd1)

    def test_set_with_empty_set(self):
        set1 = {f({})}
        zdd1 = zdd.to_zdd(set1)
        self.assertEqual(1, zdd.count(zdd1))
        self.assertEqual(zdd.base(), zdd1)
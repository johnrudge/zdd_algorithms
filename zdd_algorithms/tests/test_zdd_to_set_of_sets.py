import unittest
import zdd
f = frozenset

class TestZddToSetOfSets(unittest.TestCase):
    
    def test_normal_case(self):
        zdd1 = zdd.get_node(4,zdd.get_node(1,zdd.empty(),zdd.base()),zdd.get_node(2,zdd.empty(),zdd.base()))
        result = zdd.to_set_of_sets(zdd1)
        expected_result = {f({2,4}),f({1})}
        self.assertEqual(expected_result, result)

    def test_empty_set(self):
        self.assertEqual(set(), zdd.to_set_of_sets(zdd.empty()))

    def test_set_with_empty_set(self):
        self.assertEqual({f({})}, zdd.to_set_of_sets(zdd.base()))
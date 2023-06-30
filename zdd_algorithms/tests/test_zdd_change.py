import unittest
import zdd
f = frozenset

class TestZddChange(unittest.TestCase):
    
    def test_normal_case(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,3}),f({2,5})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.change(zdd1, 2)
        self.assertEqual(4, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,4}),f({2,3,4}),f({1,2,3}),f({5})}
        self.assertEqual(expected_result, result)

    def test_negative_ints(self):
        set1 = {f({-1,2,4}),f({3,-4}),f({1,3,6}),f({0,3,5}),f({1,-6}),f({1}),f({-1})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.change(zdd1, 1)
        self.assertEqual(7, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({-1,2,4,1}),f({3,-4,1}),f({3,6}),f({0,3,5,1}),f({-6}),f({}),f({-1,1})}
        self.assertEqual(expected_result, result)

    def test_empty_set_in_set(self):
        set1 = {f({}),f({0,1}),f({0}),f({1,3,5,6}),f({3,5,6}),f({0,3,4})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.change(zdd1, 0)
        self.assertEqual(6, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({0}),f({1}),f({}),f({1,3,5,6,0}),f({3,5,6,0}),f({3,4})}
        self.assertEqual(expected_result, result)

    def test_empty_set(self):
        set1 = set()
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.change(zdd1, 1)
        self.assertEqual(0, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = set()
        self.assertEqual(expected_result, result)

    def test_set_with_only_empty_set(self):
        set1 = {f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.change(zdd1, -1)
        self.assertEqual(1, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({-1})}
        self.assertEqual(expected_result, result)
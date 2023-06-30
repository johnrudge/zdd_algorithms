import unittest
import zdd
f = frozenset

class TestZddSubset0(unittest.TestCase):
    
    def test_normal_case(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,3})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset0(zdd1, 2)
        self.assertEqual(2, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({3,4}),f({1,3})}
        self.assertEqual(expected_result, result)

    def test_negative_ints(self):
        set1 = {f({-1,2,3}),f({-3,4}),f({1,3}),f({-5,-3}),f({2,7}),f({2,4}),f({4,-5}),f({1,-3})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset0(zdd1, -3)
        self.assertEqual(5, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({-1,2,3}),f({1,3}),f({2,7}),f({2,4}),f({4,-5})}
        self.assertEqual(expected_result, result)

    def test_empty_set(self):
        set1 = set()
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset0(zdd1, 1)
        self.assertEqual(0, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = set()
        self.assertEqual(expected_result, result)

    def test_empty_set2(self):
        set1 = {f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset0(zdd1, -1)
        self.assertEqual(1, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({})}
        self.assertEqual(expected_result, result)

    def test_empty_big_var(self):
        set1 = {f({-1,2,3}),f({-3,4}),f({1,3}),f({-5,-3}),f({2,7}),f({2,4}),f({4,-5}),f({1,-3})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset0(zdd1, 99)
        self.assertEqual(8, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({-1,2,3}),f({-3,4}),f({1,3}),f({-5,-3}),f({2,7}),f({2,4}),f({4,-5}),f({1,-3})}
        self.assertEqual(expected_result, result)  
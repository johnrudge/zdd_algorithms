import unittest
import zdd
f = frozenset

class TestZddSubset1(unittest.TestCase):
    
    def test_normal_case(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,3})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset1(zdd1, 2)
        self.assertEqual(1, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,2,4})}
        self.assertEqual(expected_result, result)

    def test_negative_ints(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,-3}),f({-3}),f({2,-3}),f({3,6}),f({4,5}),f({5,2})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset1(zdd1, -3)
        self.assertEqual(3, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,-3}),f({-3}),f({2,-3})}
        self.assertEqual(expected_result, result)

    def test_empty_set_in_set(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,-3}),f({-3}),f({1,2}),f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset1(zdd1, 1)
        self.assertEqual(3, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,-3}),f({1,2,4}),f({1,2})}
        self.assertEqual(expected_result, result)

    def test_only_empty_set_int_set(self):
        set1 = {f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset1(zdd1, 4)
        self.assertEqual(0, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = set()
        self.assertEqual(expected_result, result)

    def test_empty_set(self):
        set1 = set()
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset1(zdd1, 4)
        self.assertEqual(0, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = set()
        self.assertEqual(expected_result, result)


    def test_big_var(self):
        set1 = {f({1,2,4}),f({3,4}),f({1,-3}),f({-3}),f({2,-3}),f({3,6}),f({4,5}),f({5,2})}
        zdd1 = zdd.to_zdd(set1)
        zdd_result = zdd.subset1(zdd1, 99)
        self.assertEqual(0, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = set()
        self.assertEqual(expected_result, result)
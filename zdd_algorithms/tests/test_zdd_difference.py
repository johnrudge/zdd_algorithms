import unittest
import zdd
f = frozenset

class TestZddDifference(unittest.TestCase):

    def test_normal_case(self):
        set1 = {f({1,2,3}),f({3,4,8,9}),f({1,3,4,7})}
        set2 = {f({5,6}),f({2,6}),f({1,3,4,7}),}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(2, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,2,3}),f({3,4,8,9})}
        self.assertEqual(expected_result, result)

    def test_negative_ints(self):
        set1 = {f({1,2,3}),f({3,4}),f({1,3}),f({-3,4}),f({1,-2,5}),f({2,-5}),f({1,-6,7,8})}
        set2 = {f({5,6}),f({2,6}),f({1,3}),f({1,-2,5}),f({2,-5}),f({3,4})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(3, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,2,3}),f({-3,4}),f({1,-6,7,8})}
        self.assertEqual(expected_result, result)

    def test_empty_set(self):
        set1 = {f({1,3}),f({3,4,5}),f({2,-5}),f({1,4,7,8}),f({})}
        set2 = {f({1,-2}),f({2,-5}),f({3,4}),f({2,4,6,7}),f({3,4,5})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(3, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,3}),f({1,4,7,8}),f({})}
        self.assertEqual(expected_result, result)

    def test_empty_set_in_both(self):
        set1 = {f({2,-5}),f({1,4,7,8}),f({})}
        set2 = {f({1,-2}),f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(2, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({2,-5}),f({1,4,7,8})}
        self.assertEqual(expected_result, result)

    def test_emptyP(self):
        set1 = {f({})}
        set2 = {f({-2,-4}),f({-5})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(1, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({})}
        self.assertEqual(expected_result, result)

    def test_emptyP2(self):
        set1 = set()
        set2 = {f({-2,-4}),f({-5})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(0, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = set()
        self.assertEqual(expected_result, result)

    def test_emptyQ(self):
        set1 = {f({-2,-4}),f({-5})}
        set2 = {f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(2, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({-2,-4}),f({-5})}
        self.assertEqual(expected_result, result)

    def test_emptyQ2(self):
        set1 = {f({-2,-4}),f({-5})}
        set2 = set()
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.difference(zdd1, zdd2)
        self.assertEqual(2, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({-2,-4}),f({-5})}
        self.assertEqual(expected_result, result)
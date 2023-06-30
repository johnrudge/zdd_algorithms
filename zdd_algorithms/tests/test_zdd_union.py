import unittest
import zdd
f = frozenset

class TestZddUnion(unittest.TestCase):

    def test_normal_case(self):
        set1 = {f({1,2,3}),f({3,4}),f({1,3}),}
        set2 = {f({5,6}),f({2,6}),f({1,3}),}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(5, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({5,6}),f({2,6}),f({1,3}),f({1,2,3}),f({3,4})}
        self.assertEqual(expected_result, result)

    def test_union_negative_ints(self):
        set1 = {f({-1,2,3}),f({-3,4}),f({1,-3}),}
        set2 = {f({5,6}),f({2,6}),f({1,-3}),}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(5, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({5,6}),f({2,6}),f({1,-3}),f({-1,2,3}),f({-3,4})}
        self.assertEqual(expected_result, result)

    def test_union_empty_set(self):
        set1 = {f({1,2,3}),f({3,4}),f({6})}
        set2 = set()
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(3, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,2,3}),f({3,4}),f({6})}
        self.assertEqual(expected_result, result)

    def test_union_set_with_empty_set(self):
        set1 = {f({1,2,3}),f({3,4}),f({6}),f({})}
        set2 = {f({5,7}),f({1,2}),f({1,2,3})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(6, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({1,2,3}),f({3,4}),f({6}),f({}),f({5,7}),f({1,2})}
        self.assertEqual(expected_result, result)

    def test_union_empty_and_set_with_empty(self):
        set1 = {f({})}
        set2 = set()
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(1, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({})}
        self.assertEqual(expected_result, result)

    def test_union_emptyP(self):
        set1 = {f({})}
        set2 = {f({-1}),f({-4}),f({-4,-5})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(4, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({}),f({-1}),f({-4}),f({-4,-5})}
        self.assertEqual(expected_result, result)

    def test_union_emptyQ(self):
        set1 = {f({-1,-3}),f({-2})}
        set2 = {f({})}
        zdd1 = zdd.to_zdd(set1)
        zdd2 = zdd.to_zdd(set2)
        zdd_result = zdd.union(zdd1, zdd2)
        self.assertEqual(3, zdd.count(zdd_result))
        result = zdd.to_set_of_sets(zdd_result)
        expected_result = {f({}),f({-1,-3}),f({-2})}
        self.assertEqual(expected_result, result)

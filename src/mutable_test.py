#Author: Li Xiang
import unittest
from mutable import *
from hypothesis import given
import hypothesis.strategies as st


class TestMutableHash(unittest.TestCase):
    def test_hash_add(self):
        T = []
        hash = HashMap(T, 3)
        self.assertEqual(hash.hash_to_list(), [None, None, None])
        hash.hash_add(1)
        self.assertEqual(hash.hash_to_list(), [None, 1, None])
        hash.hash_add(2)
        self.assertEqual(hash.hash_to_list(), [None, 1, 2])

    def test_hash_remove(self):
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        self.assertEqual(hash.hash_to_list(), [1, 2, 3])
        hash.hash_remove(1)
        self.assertEqual(hash.hash_to_list(), [None, 2, 3])
        hash.hash_remove(2)
        self.assertEqual(hash.hash_to_list(), [None, None, 3])

    def test_hash_size(self):
        T = []
        hash = HashMap(T, 3)
        self.assertEqual(hash.hash_size(), 0)
        hash.hash_add(1)
        self.assertEqual(hash.hash_size(), 1)
        hash.hash_add(2)
        self.assertEqual(hash.hash_size(), 2)

    def test_hash_to_list(self):
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        self.assertEqual(hash.hash_to_list(), [1, 2, 3])

    def test_hash_from_list(self):
        test_data = [
            [1],
            [1, 2],
            [1, 2, 3]
        ]
        for e in test_data:
            hash = HashMap()
            hash = hash.hash_from_list(e)
            self.assertEqual(hash.hash_to_list(), e)

    def test_hash_find(self):
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        self.assertEqual(hash.hash_find(1), 0)
        self.assertEqual(hash.hash_find(2), 1)
        self.assertEqual(hash.hash_find(3), 2)

    def test_hash_filter(self):
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        hash.hash_filter(2)
        self.assertEqual(hash.hash_to_list(), [None, 2, 3])
        hash.hash_filter(3)
        self.assertEqual(hash.hash_to_list(), [None, None, 3])

    def test_hash_map(self):
        T = []
        hash = HashMap(T)
        hash.hash_map(str)
        self.assertEqual(hash.hash_to_list(), [])
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        hash.hash_map(str)
        self.assertEqual(hash.hash_to_list(), ["1", "2", "3"])

    def test_hash_reduce(self):
        T = []
        hash = HashMap(T)
        self.assertEqual(hash.hash_reduce(lambda st, e: st + e, 0), 0)
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        self.assertEqual(hash.hash_reduce(lambda st, e: st + e, 0), 6)

    def test_hash_mempty(self):
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        hash.hash_mempty()
        self.assertEqual(hash.hash_to_list(), [None, None, None])

    def test_hash_mconcat(self):
        T = [1, 2, 3]
        hash = HashMap(T, 3)
        T1= [1, 2]
        hash1 = HashMap(T1, 2)
        hash1 = hash1.hash_to_list()
        hash.hash_mconcat(hash1)
        self.assertEqual(hash.hash_to_list(), [1, 2, 3, 1, 2])

    def test_iter(self):
        x = [1, 2, 3]
        hash = HashMap()
        hash = hash.hash_from_list(x)
        hash = hash.__iter__()
        self.assertEqual(hash, x)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        hash = HashMap()
        hash = hash.hash_from_list(a)
        b = hash.hash_to_list()
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()

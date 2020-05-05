import unittest
from src.immutable import HashMap



class TestHashMap(unittest.TestCase):

    test = HashMap().geta();

    def test_size(self):
        self.test.clear()
        self.assertEqual(HashMap.size(None), 0)
        self.assertEqual(self.test.size(),0)
        self.assertEqual(self.test.add(5).size(), 1)

    def test_add(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).a,(None,None,None,None,None,5,None,None,None,None))
        self.test.clear()
        self.assertEquals(self.test.add(5).add(6).add(16).a, (None, None, None, None, None,5, 6, 16, None, None))

    def test_remove(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).remove(5).a, (None, None, None, None, None, None, None, None, None, None))

    def test_getValue(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).getValue(5), 5)
        self.test.clear()
        self.assertEquals(self.test.add(5).add(6).getValue(6), 6)

    def test_isContain(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).isContain(5), True)
        self.test.clear()
        self.assertEquals(self.test.add(6).isContain(5), False)

    def test_to_list(self):
        self.test.clear()
        self.assertEquals(self.test.to_list(), [None,None,None,None,None,None,None,None,None,None])
        self.assertEquals(self.test.add(5).to_list(), [None,None,None,None,None,5,None,None,None,None])

    def test_iterator(self):
        self.test.clear()
        self.assertEquals(self.test.iterator(), (None,None,None,None,None,None,None,None,None,None))




    if __name__ == '__main__':
        unittest.main()
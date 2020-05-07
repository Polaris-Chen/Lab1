#Author: ChenZhengHui
import unittest
from src.immutable import HashMap



class TestHashMap(unittest.TestCase):

    test = HashMap(hashmaplength=10);

    def test_a(self):
        self.test.clear()
        self.assertEqual(self.test.geta(),(None,None,None,None,None,None,None,None,None,None) )

    def test_length(self):
        self.test.clear()
        self.assertEqual(self.test.getLength(), 10)

    def test_size(self):
        self.test.clear()
        self.assertEqual(HashMap.size(None), 0)
        self.assertEqual(self.test.size(),0)
        self.assertEqual(self.test.add(5).size(), 1)

    def test_add(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).geta(),(None,None,None,None,None,5,None,None,None,None))
        self.test.clear()
        self.assertEquals(self.test.add(5).add(6).add(16).geta(), (None, None, None, None, None,5, 6, 16, None, None))

    def test_remove(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).remove(5).geta(), (None, None, None, None, None, None, None, None, None, None))

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

    def test_from_list(self):
        self.test.clear()
        self.assertEquals(self.test.from_list([1,3,4]), (None,1,None,3,4,None,None,None,None,None))

    def test_map(self):
        def pow2(x):
            return x*x
        self.test.clear()
        self.assertEquals(self.test.add(2).add(4).map(f=pow2), (None, None, 4, None, 16, None, None, None, None, None))


    def test_reduce(self):
        def sum(x,y):
            return x+y

        self.test.clear()
        self.assertEquals(self.test.add(2).add(4).reduce(f=sum), 6)


    def test_iterator(self):
        self.test.clear()
        self.assertEquals(self.test.iterator(), (None,None,None,None,None,None,None,None,None,None))




    if __name__ == '__main__':
        unittest.main()
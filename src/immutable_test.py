#Author: ChenZhengHui
import unittest

from hypothesis import given
import hypothesis.strategies as st

from src.immutable import HashMap



class TestHashMap(unittest.TestCase):

    #def __init__(self):
    test = HashMap(hashmaplength=10)

#####    property  __list  test #########



    def test_hash(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.getList(),(None,None,None,None,None,None,None,None,None,None) )


#######  property  __Length  test #########

    def test_length(self):
        self.test = HashMap(hashmaplength=10)
        newtest = HashMap()
        self.test.clear()
        self.assertEqual(newtest.getLength(), 0)
    #

    def test_size(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(HashMap.size(None), 0)
        self.assertEqual(self.test.size(),0)
        self.assertEqual(self.test.add(5).size(), 1)


    #
    def test_add(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.add(5).getList(),(None,None,None,None,None,5,None,None,None,None))
        self.test.clear()
        self.assertEqual(self.test.add(5).add(6).add(16).getList(), (None, None, None, None, None,5, 6, 16, None, None))

    def test_getValue(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.add(5).getValue(5), 5)
        self.test.clear()
        self.assertEqual(self.test.add(5).add(6).getValue(6), 6)

    def test_remove(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.add(6).remove(6).getList(), (None, None, None, None, None, None, None, None, None, None))


    #
    def test_isContain(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.add(5).isContain(5), True)
        self.test.clear()
        self.assertEqual(self.test.add(6).isContain(5), False)


    def test_to_list(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.to_list(), [None,None,None,None,None,None,None,None,None,None])
        self.assertEqual(self.test.add(5).to_list(), [None,None,None,None,None,5,None,None,None,None])



    def test__from_list(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        temp=[1,2,3]
        self.assertEqual(self.test.from_list(temp).getList(), (1,2,3))



    def test_map(self):
        self.test = HashMap(hashmaplength=10)
        def pow2(x):
            return x*x
        self.test.clear()
        self.assertEqual(self.test.add(2).add(4).map(f=pow2), (None, None, 4, None, 16, None, None, None, None, None))

    #
    def test_reduce(self):
        self.test = HashMap(hashmaplength=10)
        def sum(x,y):
            return x+y

        self.test.clear()
        self.assertEqual(self.test.add(2).add(4).reduce(f=sum), 6)


    def test_find(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.add(2).add(4).add(14).find(4),4)
        self.assertEqual(self.test.find(14), 5)


    def test_iterator(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.assertEqual(self.test.iterator(), (None,None,None,None,None,None,None,None,None,None))

    #
    def test_filiter(self):
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.test.add(2).add(5).add(7)
        self.assertEqual(self.test.filter(5),(None,None,2,None,None,None,None,7,None,None))


    def test_mconcat(self):
        self.test = HashMap(hashmaplength=10)
        self.test = HashMap(hashmaplength=10)
        self.test.clear()
        self.test.add(2).add(4)
        self.assertEqual(self.test.mconcat((10,11)),(None,None,2,None,4,None,None,None,None,None,10,11))

    a = [1, 2, 3,4,5]
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
    #def test_zzzz_from_list_to_list_equality(self, a):
        #self.test.clear()
        self.test = HashMap(hashmaplength=10)
        self.assertEqual(self.test.from_list(a).to_list(), a)


    if __name__ == '__main__':
        unittest.main()
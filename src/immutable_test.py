#Author: ChenZhengHui
import unittest

from hypothesis import given
import hypothesis.strategies as st

from src.immutable import HashMap



class TestHashMap(unittest.TestCase):

    test = HashMap(hashmaplength=10);

#####    property  __a  test #########

    def test_a(self):
        self.test.clear()
        self.assertEqual(self.test.geta(),(None,None,None,None,None,None,None,None,None,None) )


#######  property  __Length  test #########

    def test_length(self):
        newtest=HashMap()
        self.test.clear()
        self.assertEqual(newtest.getLength(), 0)

##########  size() test ###############
    def test_size(self):
        self.test.clear()
        self.assertEqual(HashMap.size(None), 0)
        self.assertEqual(self.test.size(),0)
        self.assertEqual(self.test.add(5).size(), 1)

##########  add() test ###############
    def test_add(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).geta(),(None,None,None,None,None,5,None,None,None,None))
        self.test.clear()
        self.assertEquals(self.test.add(5).add(6).add(16).geta(), (None, None, None, None, None,5, 6, 16, None, None))

########## remove() test ###############
    def test_remove(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).remove(5).geta(), (None, None, None, None, None, None, None, None, None, None))

##########  getValue() test ###############
    def test_getValue(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).getValue(5), 5)
        self.test.clear()
        self.assertEquals(self.test.add(5).add(6).getValue(6), 6)

##########  isContain() test ###############
    def test_isContain(self):
        self.test.clear()
        self.assertEquals(self.test.add(5).isContain(5), True)
        self.test.clear()
        self.assertEquals(self.test.add(6).isContain(5), False)

##########  to_list() test ###############
    def test_to_list(self):
        self.test.clear()
        self.assertEquals(self.test.to_list(), [None,None,None,None,None,None,None,None,None,None])
        self.assertEquals(self.test.add(5).to_list(), [None,None,None,None,None,5,None,None,None,None])

##########  from_list() test ###############
    def test_from_list(self):
        self.test.clear()
        self.assertEquals(self.test.from_list([1,3,4]).geta(), (1,3,4))

##########  from_list_to_list test ###############
    a=[1,2,3]
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        self.assertEqual(self.test.from_list(a).to_list(), a)

##########  map() test ###############
    def test_map(self):
        def pow2(x):
            return x*x
        self.test.clear()
        self.assertEquals(self.test.add(2).add(4).map(f=pow2), (None, None, 4, None, 16, None, None, None, None, None))

##########  reduce() test ###############
    def test_reduce(self):
        def sum(x,y):
            return x+y

        self.test.clear()
        self.assertEquals(self.test.add(2).add(4).reduce(f=sum), 6)

##########  find() test ###############
    def test_find(self):
        self.test.clear()
        self.assertEquals(self.test.add(2).add(4).add(14).find(4),4)
        self.assertEquals(self.test.find(14), 5)

##########  iterator() test ###############
    def test_iterator(self):
        self.test.clear()
        self.assertEquals(self.test.iterator(), (None,None,None,None,None,None,None,None,None,None))

###########  filiter() test ############
    def test_filiter(self):
        self.test.clear()
        self.test.add(2).add(5).add(7)
        self.assertEquals(self.test.filiter(5),(None,None,2,None,None,None,None,7,None,None))

###########  mconcat() test ############
    def test_mconcat(self):
        self.test.clear()
        self.test.add(2).add(4)
        self.assertEquals(self.test.mconcat((10,11,12)),(None,None,2,None,4,None,None,None,None,None,10,11,12))


    if __name__ == '__main__':
        unittest.main()
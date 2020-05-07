#Author: ChenZhengHui

class HashMap(object):

    __a=()
    __hashmaplength=0

    def geta(self):
        return self.__a
    def getLength(self):
        return self.__hashmaplength

    def __init__(self,hashmaplength):

        self.__hashmaplength=hashmaplength
        temp = []

        for i in range(hashmaplength):
            temp.append(None)

        self.__a = tuple(temp)

    def size(self):
        if self == None:
            return 0
        num = 0
        #print(len(self.a))
        for i in range(self.getLength()):
            if self.__a[i] is not None:
                num += 1
        return num

    def clear(self):
        temp=list(self.geta())
        #print(len(temp))
        for i in range(self.getLength()):
           temp[i]=None
        self.__a=tuple(temp)

    def add(self, value):
        index = value % len(self.__a)

        while self.__a[index] is not None:
            if index < self.getLength():
                index += 1
            else:
                index = 0;
        newa = list(self.__a)
        for i in range(len(self.__a)):
            if i != index:
                newa[i] = self.__a[i]
            else:

                newa[i] = value;


        self.__a = tuple(newa)

        return self

    def remove(self, value):
        index = value % len(self.__a)
        while self.__a[index] != value:
            if index < self.getLength():
                index += 1
            else:
                index = 0;
        newa = list(self.__a)
        newa[index] = None
        self.__a = tuple(newa)
        return self

    def to_list(self):
        return list(self.__a)

    def from_list(self,ListExample):
        self.clear()
        for i in range(len(ListExample)):
            if ListExample[i] is not  None:
                self.add(ListExample[i])
        return self.__a

    def getValue(self, num):
        return self.__a[num]

    def isContain(self, value):
        index = value % len(self.__a)
        while self.__a[index] is not None:
            if self.__a[index] != value:
                index += 1
            else:
                return True
        return False
    def map(self,f):
        temp=list(self.geta())
        for i in range(self.getLength()):
            if temp[i] is not None:
                temp[i]=f(temp[i])
        self.__a=tuple(temp)
        return self.__a

    def reduce(self,f):
        result=0
        for i in range(self.getLength()):
            if self.__a[i] is not None:
                result=f(result,self.__a[i])
        return result


    def mempty(self):
        return None

    def iterator(self):

        return self.__a




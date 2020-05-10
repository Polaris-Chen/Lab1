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

###### 5.10 update  ##########
    def from_list(self,ListExample):
        self.__a=tuple(ListExample)
        return self

        #self.clear()
        #for i in range(len(ListExample)):
         #   if ListExample[i] is not  None:
          #      self.add(ListExample[i])
        #return self.__a

######## update end ###############

    def getValue(self, num):
        if(num<self.__hashmaplength):
            return self.__a[num]
        return "out fo length"

    def isContain(self, value):
        index = value % len(self.__a)
        while self.__a[index] is not None:
            if self.__a[index] != value:
                index += 1
            else:
                return True
        return False

###### 5.10 update  ##########
    def find(self,value):
        if(self.isContain(value)):

            for x in range(self.__hashmaplength):
                if(self.__a[x]==value) :
                    return x
        else:
            return "No value"

    def filiter(self,value):
        temp = list(self.__a)
        for x in range(len(temp)):
            if temp[x]==value:
                temp[x]=None
        self.__a=tuple(temp)
        return self.__a

    def mconcat(self,b):
        if self.__hashmaplength == 0:
            return b
        else:
            temp=self.__a+b
            self.__a=temp
            return  temp

######## update end ###############

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




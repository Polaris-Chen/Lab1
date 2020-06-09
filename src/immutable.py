#Author: ChenZhengHui

class HashMap(object):

    __list=()
    __listmaplength=0

    def getList(self):
        return self.__list
    def getLength(self):
        return self.__listmaplength

    def __init__(self,hashmaplength=0):

        self.__listmaplength=hashmaplength
        temp = []

        for i in range(hashmaplength):
            temp.append(None)

        self.__list = tuple(temp)

    def size(self):
        if self == None:
            return 0
        if self.getLength()==0:
            return 0
        num = 0
        #print(len(self.a))
        for i in range(self.getLength()):
            if self.__list[i] is not None:
                num += 1
        return num

    def clear(self):
        if self.getLength()==0:
            return
        temp=list(self.getList())

        for i in range(len(temp)):
           #print(i)
           temp[i]=None
        self.__list=tuple(temp)

    def add(self, value):
        index = value % len(self.__list)

        while self.__list[index] is not None:
            if index < self.getLength():
                index += 1
            else:
                index = 0;
        newa = list(self.__list)
        for i in range(len(self.__list)):
            if i != index:
                newa[i] = self.__list[i]
            else:

                newa[i] = value;


        self.__list = tuple(newa)

        return self

    def remove(self, value):
        index = value % len(self.__list)
        while self.__list[index] != value:
            if index < self.getLength():
                index += 1
            else:
                index = 0;
        newa = list(self.__list)
        newa[index] = None
        self.__list = tuple(newa)
        return self

    def to_list(self):
        return list(self.__list)


    def from_list(self,ListExample):
        self.__list=tuple(ListExample)
        return self

        #self.clear()
        #for i in range(len(ListExample)):
         #   if ListExample[i] is not  None:
          #      self.add(ListExample[i])
        #return self.__list



    def getValue(self, num):
        if(num<self.__listmaplength):

            return self.__list[num]
        return "out fo length"

    def isContain(self, value):
        index = value % len(self.__list)
        while self.__list[index] is not None:
            if self.__list[index] != value:
                index += 1
            else:
                return True
        return False


    def find(self,value):
        if(self.isContain(value)):

            for x in range(self.__listmaplength):
                if(self.__list[x]==value) :
                    return x
        else:
            return "No value"

    def filter(self,value):
        temp = list(self.__list)
        for x in range(len(temp)):
            if temp[x]==value:
                temp[x]=None
        self.__list=tuple(temp)
        return self.__list

    def mconcat(self,b):
        if self.__listmaplength == 0:
            return b
        else:
            temp=self.__list+b
            self.__list=temp
            return  temp



    def map(self,f):
        temp=list(self.getList())
        for i in range(self.getLength()):
            if temp[i] is not None:
                temp[i]=f(temp[i])
        self.__list=tuple(temp)
        return self.__list

    def reduce(self,f):
        result=0
        for i in range(self.getLength()):
            if self.__list[i] is not None:
                result=f(result,self.__list[i])
        return result


    def mempty(self):
        return None

    def iterator(self):

        return self.__list

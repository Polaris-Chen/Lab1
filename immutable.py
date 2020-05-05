
class HashMap(object):

    __a=()

    def geta(self):
        return a

    def __init__(self):
        temp = []
        for i in range(10):
            temp.append(None)

        self.a = tuple(temp)

    def size(self):
        if self == None:
            return 0
        num = 0
        #print(len(self.a))
        for i in range(10):
            if self.a[i] is not None:
                num += 1
        return num

    def clear(self):
        self.a=a=(None,None,None,None,None,None,None,None,None,None)

    def add(self, value):
        index = value % len(self.a)

        while self.a[index] is not None:
            if index < 9:
                index += 1
            else:
                index = 0;
        newa = list(self.a)
        for i in range(len(self.a)):
            if i != index:
                newa[i] = self.a[i]
            else:

                newa[i] = value;


        self.a = tuple(newa)

        return self

    def remove(self, value):
        index = value % len(self.a)
        while self.a[index] != value:
            if index < 9:
                index += 1
            else:
                index = 0;
        newa = list(self.a)
        newa[index] = None
        self.a = tuple(newa)
        return self

    def to_list(self):
        return list(self.a)

    def getValue(self, num):
        return self.a[num]

    def isContain(self, value):
        index = value % len(self.a)
        while self.a[index] is not None:
            if self.a[index] != value:
                index += 1
            else:
                return True
        return False

    def mempty(self):
        return None

    def iterator(self):

        return self.a


s = (1, None)

a = HashMap()
#print(a.add(5).a)

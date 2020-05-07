# Author: Li Xiang
class HashMap(object):
    def __init__(self, T=[], size=0):
        if len(T) == 0:
            self.T = [None for i in range(size)]
        else:
            self.T = T
        self.size = size

    def hash_add(self, k):
        i = 0
        while i < self.size:
            j = self.hash_h1_h2(k, i)
            if self.T[j] == None:
                self.T[j] = k
                return j
            else:
                i += 1
        return "hash table overflow"

    def hash_remove(self, k):
        index = self.hash_find(k)
        if self.hash_find(k) != None:
            self.T[index] = None
        else:
            return "element doesn't exist"
        return self.T

    def hash_size(self):
        i = 0
        res = 0
        while i < self.size:
            if (self.T[i] != None):
                res += 1
                i += 1
            else:
                i += 1
        return res

    def hash_to_list(self):
        res = []
        i = 0
        while i < self.size:
            res.append(self.T[i])
            i += 1
        return res

    def hash_from_list(self, a):
        self.T = HashMap(a, len(a))
        return self.T

    def hash_find(self, k):
        i = 0
        while i < self.size:
            if self.T[i] == k:
                return i
            else:
                i += 1
        return None

    def hash_filter(self, k):
        i = 0
        while i < self.size:
            if self.T[i] == None:
                i += 1
            elif self.T[i] < k:
                self.T[i] = None
                i += 1
            else:
                i += 1
        return self.T

    def hash_map(self, f):
        i = 0;
        while i < self.size:
            if self.T[i] != None:
                self.T[i] = f(self.T[i])
                i += 1
            else:
                i += 1

    def hash_reduce(self, f, initial_state):
        state = initial_state
        i = 0
        while i < self.size:
            if self.T[i] != None:
                state = f(state, self.T[i])
                i += 1
            else:
                i += 1
        return state

    def hash_mempty(self):
        self.T = [None for i in range(self.size)]
        return self.T

    def hash_mconcat(self, a):
        if self.size == 0:
            return a
        self.size += len(a)
        self.T = self.T + list(a)
        return self.T

    def __iter__(self):
        return self.T

    def hash_h1_h2(self, k, i):
        return ((k % self.size + i * (1 + k % (self.size - 2)))) % self.size


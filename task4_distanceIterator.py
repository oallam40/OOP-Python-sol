"""
    vvvv      YOUR SOLUTION      vvvv
"""

class DistanceIterator:
    
    def __init__(self, numbers):
        # constructor of our Iterator
        self.numbers = numbers
        self.index = 0
        self.res = []
    
    def __iter__(self):
        # "initialize our iterator here"
        if len(self.numbers) <= 1: 
            self.index = len(self.numbers)
        return self
    
    def __next__(self):
        # next method
        # do not forget to put `raise StopIteration`

        if self.index >= len(self.numbers):
            raise StopIteration

        for j in range(self.index + 1, len(self.numbers)):
            self.res.append(abs(self.numbers[j]-self.numbers[self.index]))
        
        
        res = self.res[self.index]
        self.index += 1
        return res
        # return self.res <-- uncomment here to get correct result but wrong output


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""

# empty number list
assert [n for n in DistanceIterator([])] == []

# one number in list --> also no distances
assert [n for n in DistanceIterator([4])] == []

# some examples
assert [n for n in DistanceIterator([4,2,-2])] == [2,6,4]
# print([n for n in DistanceIterator([4, 2, -2])])
# assert [n for n in DistanceIterator([3,3,3,8])] == [0, 0, 5, 0, 5, 5]
print([n for n in DistanceIterator([3,3,3,8])])
# assert [n for n in DistanceIterator([-1,20,23,-5,8])] == [21, 24, 4, 9, 3, 25, 12, 28, 15, 13]
print([n for n in DistanceIterator([-1,20,23,-5,8])])
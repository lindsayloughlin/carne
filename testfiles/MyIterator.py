class MyIterator:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        print(str(self.data[self.index]))
        return self.data[self.index]

iterator = MyIterator([1,2,3])
# iterator.next();
# iterator.next();
# iterator.next();
#iterator.next();
# for item in iterator:
#     print(item)

mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)
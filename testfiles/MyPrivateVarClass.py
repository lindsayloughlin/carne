class MyPrivateVarClass:
    def __int__(self):
        __my_private_var = 'hello world'
        self.__my_private_var = 'test'

    def reverse(self, data):
        print('my private class')
        for index in range(len(data) - 1, -1, -1):
            yield data[index]


privateclass = MyPrivateVarClass()
privateclass.reverse(data='helloworld')

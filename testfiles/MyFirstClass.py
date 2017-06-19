class class_name:

    my_shared_variable = 10
    def __init__(self, x, y):

        self.x = x;

    def print_input_class(self, helloworld):
        print(self.x)
        print('shared ' + str(class_name.my_shared_variable))
        print('passed in arg ' + str(helloworld))


hello = class_name('hello', 'world')
hello.print_input_class('second arg')
print(str(hello.my_shared_variable))
hello.my_shared_variable = hello.my_shared_variable + 1
class_name.my_shared_variable = 5
print (class_name.my_shared_variable);
print(str(hello.my_shared_variable))

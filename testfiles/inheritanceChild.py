from testfiles.InheritanceParent import BaseClass


class ChildClass(BaseClass):

        def __int__(self):
            print(self.myvar);


        def print_var(self):
            print('hello wolrd')
        #def print_var(self):
            #print(self.myvar)

myChildClass = ChildClass()
#myChildClass.print_var()

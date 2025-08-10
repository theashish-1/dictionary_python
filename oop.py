class Student:
    def __init__(self):  # this is a constructor
        print(id(self))
        print("this will be called automatically when we create object of student")
s1 = Student()
print(id(s1))
#self is s1 is sent as to self it is the reference of the object
# we can observe that id of both self and object are same if we dont give self it gives error because init takes an argument ie. object itself






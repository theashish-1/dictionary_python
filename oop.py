class Student:
    def __init__(self,name,marks,rollNumber):  # this is a constructor
        #print(id(self))
        #print("this will be called automatically when we create object of student")
        #below is data member / variable
        # self.name = "John"
        # self.marks = 90
        # self.rollNumber = 103

        self.name = name
        self.marks = marks
        self.rollNumber = rollNumber
    #below is methord
    def study(self):
        print("I am "+self.name+ " I am studying ")
    def play(self):
        print("playing ")

s1 = Student("John" , 34 , 10034)
print(s1.name , s1.marks , s1.rollNumber)
print(s1.study())
print(s1.play())
# print(id(s1))
#self is s1 is sent as to self it is the reference of the object
# we can observe that id of both self and object are same if we dont give self it gives error because init takes an argument ie. object itself






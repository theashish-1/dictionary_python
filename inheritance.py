# class User:
#     _job = "IT"
#     def __init__(self,name,id,marks):
#         self.name = name
#         self.id = id
#         self._marks = marks
#     def login(self):
#         print(" P login in successfully")
#     def logout(self):
#         print("P logout done")
#
# #child class
# class Student(User):
#     def print(self):
#         return f"name : {self.name} id : {self.id} job : {self._job} marks : {self._marks}"
#     def changeMarks(self,marks):
#         self._marks = marks
#
#     def __init__(self,name , id , marks , age , passCode):
#         # here since name id marks is in __init__ of parent class we can directly access that init methord
#         super().__init__(name,id,marks)
#         self.age = age
#         self.passCode = passCode
#     def login(self):
#         print("OTP method implementation")
#         super().login()
# # s = Student("ashish",101,74)
# s1 = Student("omkar",102,90,18,"0000")
# print(s1.login())
# #here login is inherited from parent class ie.. User class
# print(s1.print())
# print("marks changed")
# s1.changeMarks(95)
# print(s1.print())
# print(s1.login())





class merchant:
    def __init__(self):
        self.website = "www.amazon.com"
        self._buyer = "amazon"
        self.__cost = 1200
    def getCost(self):
        return f"{self.__cost}"
    def login(self):
        return f"login successfully done "
class customer(merchant):
    def __init__(self):
        super().__init__()
        self.name = "ashish"
        self.website = "www.flipkart.com"
    def login(self):
        return super().login()
c = customer()
m = merchant()
print(m.getCost())

print(c.website , c._buyer)
print(c.login())





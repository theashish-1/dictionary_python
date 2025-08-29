
class Student:
    #global variables
    schoolName = "xyz School" # class variable / static variable
    __numberOfStudents = 0
    def __init__(self,name,marks,status):
        self.name = name
        self.marks = marks
        #intializing a global variable
        self.schoolName = Student.schoolName
        self.__numberOfStudents = Student.__numberOfStudents+1
        #private access modifier
        self.__status = status

    @staticmethod
    def getSchoolName():
        return Student.schoolName
    @staticmethod
    def setSchollName(newSchoolName):
        Student.schoolName = newSchoolName

    def __str__(self):
        return f"name:{self.name} mark:{self.marks} School : {self.schoolName}"
    def study(self):
        #this methord also throws a none
        print("I am "+ self.name + " and I am studying")

    #getters and setters



    def getStatus(self,passCode):
        if passCode == self.__auth():
            return self.__status
        else:
            return f"No access to modify "

    def setStatus(self,passCode,newStatus):
        if passCode == self.__auth():
            self.__status = newStatus
            return "Status updates succesfully"
        else:
            return "No access"

    #simple authentication
    def __auth(self):
        return "0000"


s = Student("john" , 89,"pass")
print(s)
print(s.study())
# print(s.getStatus())
# print(s.setStatus("fail"))
# print(s.getStatus())
print(s.setStatus("0000","fail"))
print(s.getStatus("0000"))
s.setSchollName("IIT")
print("fetching school name using static method ",s.getSchoolName())
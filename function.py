def add(a, b):
    return a+b
c = add(2,3)
print("sum",c)
#average of 3 numbers
def calculate_average(a ,b ,c):
    return (a+b+c)/3
average = calculate_average(1,2,3)
print("Average of 3 numbers is ",average)
#built in function
#end does not move to new line execute the below code for demo
print("Ashish",end=" ")
print("acharya")
print("Ashish",end="$")
print("acharya")

#keyword argument
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def unknow_parameter(**word):
    print("last name is ",word["lname"])
unknow_parameter(fname="ashish",lname="acharya")

# passing list as argument
def listArgument(list):
    for i in list:
        print(i,end=" ")
listArgument([1,2,"ashish"])
print()
#Note if are assigning a default parameter it should begin from last
#example note if we swap a and be in function defination then it gives error
def defaultParameter(b, a=20):
    return a*b
print(defaultParameter(2))

#factorial

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
print("factorial of number is",factorial(4))

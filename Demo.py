# print("demo code ")
# list = [1,2,"abc","abc",2,1]
# list2 = list.copy()
# list2.reverse()
# if(list==list2):
#     print("palindrome")
# else:
#     print("not palindrome")


# tuple = ('c','d','b','a','a','c','d')
# a = tuple.count('a')
# print(a)
# list = ['c','d','b','a','a','c','d']
# list.sort()
# print(list)

#dictionary and sets in pythons
#dictory are key- pair values
dict = {
      "name" : "Ashish",
      "cgpa" : 9.1,
      "marks" : [21 ,56,88]
}
print(dict)
print(dict["name"])
lst = dict["marks"]
print(lst[0])
print(dict["marks"])

#nested dictionary
student = {
      "name" : "ashish Acharya",
      "subject" : {
      "phy" : 45,
      "che" : 67,
      "maths" : 87
}
}
print(student)
print(student["subject"]["che"]) #accessing nested dictiory

#methords
print(student.keys()) #gives list of all keys only outside keys not nested keys
#to type cate this above to list then
#print(list(student.keys()))
print(list(student.keys()))
print(len(list(student.keys())))
print(dict.values())
#items gives all pairs
print(dict.items()) #gives in form of tuples
#another  way
tuple_ans = list(dict.items())
print("tuple ans is ",tuple_ans[2]) #output is in the form of tuple
#to acees value
print("to get value using key ",dict.get("name"))
#way 2
print(dict["name"])
#difference is
#if we try to access something that is not present as a key then ie.. if key is wrong
#example
print(dict.get("qweqweq")) #gives output as none
#print(dict["safasfa"]) #gives output as error
updated_dict = {"name" : "anush" , "age" :25}
dict.update(updated_dict)
print("updated dict dictionary is ",dict)
#null dictionary
null_dict = {}
null_dict["name"]= "ashish"
print(null_dict)
#set in python similar to hashset in java
collection = {1,2,3,4,5 ,4,}
print(type(collection))
print(collection)
print(len(collection)) # does not include duplicate values
#creating an empty set
empty_set1 = {} # does not create an empty set it created a  dictionary
print(type(empty_set1))
#correct way of creating an empty set is as below
empty_Set = set()
print(set)



#note : set are mutable but set's elements are immutable that is why we cannot pass dictionary and list

#set methords
empty_Set.add(1)
empty_Set.add(2)
empty_Set.add(2)
empty_Set.add((1,2,3,4))
#wile adding list we get am error
#empty_Set.add([1,2,"Ashish"])
#TypeError: unhashable type: 'list' means for example a tuple
#print(empty_Set)


#for loop
i=0
# for i in range(1,5):
#     print(i,end=" ")

j=0
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
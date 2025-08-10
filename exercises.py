# Write a program to find the sum of all elements in a list.
# nums = [1,6,12,19,25]
# sum = 0
# for i in nums:
#     #print(i)
#     sum = sum + i
# print(sum)


# problem 2 : Find the largest and smallest number in a list without using max() or min().
# nums = [1,6,12,19,25,9]
# maximum = -1
# for i in nums:
#     maximum = max(maximum,i)
# print("maximum value in the list is ",maximum)


#reverse list
# nums = [1,6,12,19,25,9]
# for i in range(len(nums)-1,-1,-1):
#     print(nums[i])
#

#remove duplicates
nums = [1,1,1,2]
# collection = set()
# for i in nums:
#     collection.add(i)
# print(collection)

#way 2
xorAns = 0
for i in nums:
    xorAns = xorAns ^ i
print(xorAns)

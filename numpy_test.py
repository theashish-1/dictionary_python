import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
total = 0
for i in arr:
    total += i
average = total / len(arr)
print(average)
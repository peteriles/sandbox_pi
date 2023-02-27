# Exercise 9-16
import array # Recommendation I'm reading is that if you want to do math, just import NumPy
import time

a = array.array('i',[2, 4, 5, 1, 3, 6]) # Here is the "array" data type. The "i" is for integer.

print(a)

b = [[1,2,3],[4,6,7]] # This is not a real array, but rather a list of lists!
print(b)
print(b[0][2])

print("The time is: ", time.time())
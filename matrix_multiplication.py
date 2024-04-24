# Program to multiply two matrices (vectorized implementation)
import numpy as np

n = int(2)
# Lines below reads inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter the 2 numbers of first row of A-Matrix separated by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter the 2 numbers of second row of A-Matrix separated by space : ").strip().split()))[:n]

list3 = list(map(int, 
	input("\nEnter the 2 numbers of first row of B-Matrix separated by space : ").strip().split()))[:n]
list4 = list(map(int, 
	input("\nEnter the 2 numbers of second row of B-Matrix separated by space : ").strip().split()))[:n]

# take a 2x2 matrix
A = [(list1),
    (list2)]
# take a another 2x2 matrix
B = [(list3),
    (list4)]
# result will be 2x2
result= [[0,0],
        [0,0]]
 
result = np.dot(A,B)
print("The Matrix multiplication result is: ")
for r in result:
    print(r)
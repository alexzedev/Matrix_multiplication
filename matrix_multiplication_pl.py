# Program do multiplikacji dwóch macierzy (impementacja wektorowa)
import numpy as np

n = int(2)
# # Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map()
list1 = list(map(int, 
	input("\nEnter the 2 numbers of first row of A-Matrix separated by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter the 2 numbers of second row of A-Matrix separated by space : ").strip().split()))[:n]

list3 = list(map(int, 
	input("\nEnter the 2 numbers of first row of B-Matrix separated by space : ").strip().split()))[:n]
list4 = list(map(int, 
	input("\nEnter the 2 numbers of second row of B-Matrix separated by space : ").strip().split()))[:n]

# tworzy macierz 2x2
A = [(list1),
    (list2)]
# tworzy kolejną macierz 2x2
B = [(list3),
    (list4)]
# wynik będzie macierzą 2x2
result= [[0,0],
        [0,0]]
 
result = np.dot(A,B)
print("The Matrix multiplication result is: ")
for r in result:
    print(r)
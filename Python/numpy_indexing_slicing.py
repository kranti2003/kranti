import numpy as np

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])

five_up = (a >= 5)
print(a[five_up])

divisible_by_2 = a[a%2==0]
print(divisible_by_2)

c = a[(a > 2) & (a < 11)]
print (c)

five_up = (a > 5) | (a == 5)
print (five_up)


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print (b)

list_of_coordinates= list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    print(coord)

print(a[b])


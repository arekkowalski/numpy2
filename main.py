import numpy as np

# Zad 1
# a=np.arange(3)
# b=np.arange(3)
# print(a*b)

# Zad2
# a=np.arange(9).reshape(3,3)
# b=np.arange(16).reshape(4,4)
# def SmallestValues(a):
#     answer = "Najmniejsze wartości w poszczególnych rzędach to: \n"
#     for x in a:
#         answer+= str(np.amin(x)) + "\n"
#     a = a.T
#     answer+="Najmniejsze wartości w poszczególnych kolumnach to: \n"
#     for y in a:
#         answer+=str(np.amin(y)) + "\n"
#     return answer
#
# print(SmallestValues(a))
# print(SmallestValues(b))

# Zad3
# a=np.arange(3)
# b=np.arange(3)
# print(a.dot(b))

# Zad4
# a=np.ones(3, dtype="int32")
# b=np.linspace(0,np.pi,3)
# print(a.dot(b))

# Zad5
# b=np.arange(6).reshape(2,3)
# a=np.sin(b)
# print(a)

# Zad6
# a=np.arange(6).reshape(2,3)
# b=np.cos(a)
# print(b)

# Zad8
# a = np.arange(9).reshape(3,3)
# for x in a:
#     print(x)
#     print(" ")
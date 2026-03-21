#Greatest Common Divisor - Phân số
from math import gcd
a, b = map(int, input("a, b = ").split())
g = gcd(a, b)  #Phân số
a_new = a // g
b_new = b // g
print(a_new, b_new)

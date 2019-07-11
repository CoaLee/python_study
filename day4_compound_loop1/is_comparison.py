# is_comparison.py

a = [1,2,3]
b = a
c = [1,2,3]

print(id(a))
print(id(b))
print(id(c))

print()
print(a == b)   # True
print(a == c)   # True 

print()
print(a is b)   # True
print(a is c)   # False

d = [1,2,3]
e = [1,2]

print()
print(id(d))
print(id(e))

print()
print(d == e)   # False
print(d is e)   # False
del d[2]
print(d == e)   # True
print(d is e)   # False
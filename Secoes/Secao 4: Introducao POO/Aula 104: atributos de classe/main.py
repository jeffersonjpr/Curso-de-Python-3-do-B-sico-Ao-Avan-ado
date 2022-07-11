class A:
    var = 123

a1 = A()
a2 = A()
    
print(a1.var)
print(a2.var)
print(A.var)

A.var = 456

print(a1.var)
print(a2.var)
print(A.var)
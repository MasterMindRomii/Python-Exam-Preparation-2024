#Operators in Python Programming

a=10
b=5
c=2

#a) Arithemetic Operator - Unary and Binary 

#Unary

print(+a)
print(-a)

#Binary 

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)

#b) Logical Operator - AND,OR & NOT

a=True
b=False

print(a and b)
print(a or b)
print(not a)
print(not b)

#c) Assignment Operator -

a += b
print(a)

a -= b
print(a)

a /= b
print(a)

a *= b 
print(a)

#d) Membership Operator - in & not in 

Number=[1,2,3,4,5]
print(5 in Number)
print(10 not in Number)

#e) Identity Operator - is and is not 

d=10
e=10

print(type(d) is int)
print(type(e) is not int)

#also

print(id(d))
print(id(e))

print(d is e)

#f) Bitwise Operator - 

print(a|b)
print(a^b)
print(~a)
print(a&b)
print(a<<1)
print(a>>1) 

#g) Comparision Operator - 

print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

print("All Done!")

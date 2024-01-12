#String Literals 

print("Ram Ram Ji") #Single Line 
print("Ram Ram \
    ji") #Multiline String
print('''Ram 
      Ram 
      Ji''')

#Numerical Literlas

# a) Integer Literlas - Decimal(0-9), Octal(Leading with 0o), Binary(0-1) and HexaDecimal(Leading with 0x)

a=10
print("Decimal:",a)

b=0o1276
print("Octal:",b)

c=0b10011
print("Binary:",c)

d=0x12787321abc
print("HexaDecimal:",d)

# b) Floating Point Literals 

e=19.5 
print("Floating point literlas:",e)

# c) Complex Literlas 

f=12j
g=12+5j

print("Complex:",f,g)
print(type(g))

#Boolean Literlas 

a=(1==True)
b=(1==False)
c=a+3
d=b+7
print(a,b,c,d)

#Special Literlas 

a=(None)
print(type(a))

#Collection Literlas - a) List Literals b) Tuple Literlas c) Dictionary Literlas d) Set Literals

a=[1,2,3,4,5]
b=(1,2,3,4,5)
c={"1":"Romi","2":"Suraj"}
d={'a','b','c','d','e'}

print(a,b,c,d)
print(type(a))
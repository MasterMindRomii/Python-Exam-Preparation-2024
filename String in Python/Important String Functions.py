# Join in String

Test = "India 2024"

# a) Simple join
Simple = "-".join(Test)
print(Simple)

# b) List join
List = list(Test)
New = "And".join(List)
print(New)

# c) Tuple join
t = tuple(Test)
new_t = "-".join(t)
print(new_t)

# d) Dictionary join
dic = {"India": 1, "Australia": 2, "England": 3}
new_dic = "-".join(dic)
print(new_dic)

# e) Set Join

s = {"a", "e", "i", "o", "u"}
s_new = "-".join(s)
print(s_new)


#Split in String 

str="Happy-New-Year"
print(str.split('-'))
print(str.split('-',0))
print(str.split('-',1))
print(str.split('-',2))
#Default Arguments
def add(x,y=50):
    z=x+y
    print(z)
add(10)

#Postional Arguments
def Details(Name,Age):
    print("My Name is:",Name)
    print("Age is:",Age)
Details("Romi Gupta",20)
Details(20,"Romi Gupta") #Gives Error 

#Keyword Arguments 
def Person(Name,Age,Address):
    print("Person name is:",Name)
    print("Age is:",Age)
    print("Address of person:",Person)
Person(Name="Romi Gupta",Age=20,Address="Najafgarh")

#Variable lenght Arguments -

# 1.*args for variable number of arguments
def myFun(*argv):
	for arg in argv: #if it is present the next line all output
		print(arg) #if only this present(not just above) then in 'tuple' form answer or agrv you got in output!
myFun('Romi',20,'Delhi',9910028128)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# 2.**kwargs for variable number of keyword arguments
def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))
myFun(Name='Romi',Age=20,City='Delhi',Mob=9910028128)
myFun(first='Geeks', mid='for', last='Geeks')


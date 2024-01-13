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
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# 2.**kwargs for variable number of keyword arguments
def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


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
def 
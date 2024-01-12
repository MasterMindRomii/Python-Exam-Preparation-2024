#Formatting of string in python 

# a) Default Formatting 

string="{}{}{}".format('Happy','New','Year')
print(string)

# b) Positional Formatting 

string="{1}{0}{2}".format('New','Happy','Year')
print(string)

#c) Keyword Formatting 

string="{H}{Y}{N}".format(H="Happy",N="New",Y="Year")
print(string)


#Updating a String 

Word = "Happy New Year 2023"
str1=list(Word)
for i in range(len(str1)):
    if(str1[i]=="3"):
        str1[i]="4"
    
Str2=''.join(str1)
print(Str2)
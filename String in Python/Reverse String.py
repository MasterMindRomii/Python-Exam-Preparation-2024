#Reversing the string

#Using Indexing -
Event="Happy New Year 2024"
print(Event[::-1])
print(Event[-1::-1])

#Using for loop -

New_Event=""
for char in Event:
    New_Event=char+New_Event

print(New_Event)

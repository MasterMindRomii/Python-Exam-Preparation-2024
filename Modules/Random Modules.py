import random

# 1. Syntax : random.random() - Floating point number
print(random.random())

# 2. Syntax : random.randrange(a,b,stepvalue) - Integer
print(random.randrange(2,10,3))

# 3. Syntax : random.randint(a,b) return int number including both limits - Integer
print(random.randint(2,18))

# 4. Syntax : uniform(a,b) - return any floating number b/w two numbers
print(random.uniform(12,14))

# 5. Syntax : Choice()  - return any floating or integer number from list,tuple or any sequence.
l=[12,14,15,17,19]
print(random.choice(l))

# 6. Syntax : Shuffle()  - return distinct order every time from list,tuple or any sequence.
l=[12,14,15,17,19]
print(random.shuffle(l))
#!/usr/bin/env python3


# casing
x=str(2)
y=str(30.0)
z=str("20")
print(x)
print(y)
print(z)

# Variable type
print(x, type(x))

print(True and False)

#########################################  Conditions ########################################
name = 'Bob'
if name == 'Alice':
 print('Hi, Alice.')
elif name=="Bob":
 print('Bob found')
else:
 print('Hello, stranger.')
 

 

#########################################     LOOPS  ########################################
for i in range(0, 10, 1):
 print(i)

for i in range(5):
 print(i)



########################################    Functions     ########################################
def hello(name):
 print('Hello {}'.format(name))
hello('Alice') #Hello Alice
hello('Bob') #Hello Bob

import random #Syntax to import Python libraries
def getAnswer(answerNumber):
    if answerNumber == 1:
     return 'It is certain'
    elif answerNumber == 2:
     return 'It is decidedly so'
    elif answerNumber == 3:
        return 9
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

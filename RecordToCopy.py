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
else:
 print('Hello, stranger.')

#########################################     LOOPS  ########################################
for i in range(0, 10, 1):
 print(i)

for i in range(5):
 print(i)






############# REVERSE LIST FUNCTION #############

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()

print('Reversed List:', prime_numbers)
def reverseList(rev):
   rev.reverse()
   return rev

h=reverseList(["h","e","l","l","o"])
print(h)




######################### FILING #########################################

# Program to show various ways to read and
# write data in a text file.

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

#i assigned ["This is Lagos \n","This is Python \n","This is Fcc \n"]
#to variable L

#The \n is placed to indicate End of Line

file.write("Hello There \n")
file.writelines(L)
file.close()
# use the close() to change file access modes



file = open("myfile.txt","r+") 
print("Output of the Read function is ")
print(file.read())
print()

# The seek(n) takes the file handle to the nth
# byte from the start.
file.seek(0) 

print( "The output of the Readline function is ")
print(file.readline()) 
print()

file.seek(0)

# To show difference between read and readline

print("Output of Read(12) function is ") 
print(file.read(12))
print()

file.seek(0)

print("Output of Readline(8) function is ") 
print(file.readline(8))

file.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file.readlines()) 
print("changed a line")
file.close()



branch = open("testBranching.txt","w+")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]
branch.writelines(L)
branch.seek(0)
print(branch.read())
branch.seek(0)
print(branch.readlines()) 
branch.seek(0)
print(branch.readlines(6)) 


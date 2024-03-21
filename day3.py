#eg:3
#take values of length and breadth of a fram user and check if it is square or not
'''
length=int(input("enter the value:"))
breadth=int(input("enter the value:"))
if length==breadth:
    print("it is square")
else:
    print("its not square")
                      
#eg:4

a=int(input("enter the number"))
if a%5==0 and a%7==0:
    print("it is integer")
else:
    print("not an integer")
'''

#eg:5
'''
a=int(input("enter the price of a bike:"))
amount=0
if a>=100000:
   discount=100000*(6/100)
   value=a-discount
   amount=value*(15/100)
   total=value+amount
else:
    a<100000
    amount=a*(5/100)
    print("amount")

'''
#if ,elif ,else
    #eg:1
#a=7
#b=9
#c=3
'''
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    c>a and c>b
    print("c is greater")

#a school has following rules for grading system:

#a=int(input("enter the marks"))
#if a < 25:
    #print("f")
#elif a == 25 and a <= 45:
    #print("e")
#elif a == 45 and a <= 50:
    #print("d")
#elif a == 50 and a <= 60:
    #print("c")
#elif a == 60 and a <= 80:
    #print("b")
#elif a == 80 and a <= 100:
    #print("a")



# short hand rules:

# 1) Statement inside the if condition have to be present at first.
# 2) Elif cannot be used in short hand if else.
# 3) Always it have to end with else.


# print("A") if a>b else print ("B")_     


# Code to check the given char is vowel or consonent
#char = input("Enter the char: ")
#if char=="a" or char=='e' or char=='i' or char=='o' or char== 'u':
      #print("is a vowel")

#else:
   # print("its consonent")
    
# or

#str1="aeiouAEIOU"
#if char in str1:
    #print("vowel")
#else:
   # print("consonent")


# shorthand if else


#char=input("Enter the char: ")
#str1="aeiouAEIOU"
#print("vowels")if char in str1 else print("consonent")

'''

# ---> elif ladder using short hand ifelse
# Eg:1
# Find greeatest among 3 variables using short hand if else
'''
a=8
b=5
c=9
print("a is greater ") if a>b and a>c else print("b is greater") if b>a and b>c else print ("c is greater")

'''

# ----> looping

# looping can be implemented using
# for loop
# while loop

#---> for loop

#for loop is used for iteration, if we know the number of times the loop  have to run
# It is used to iterate the iterables eg(string, list, tuple, etc....)

# ---> Syntax for loop


# for syntax in c
# for(i=0;i<10;i++){
# print("hello");
# }



# for syntax in python
# for user defined_variable in range(start, end, step): default step value is 1
# statement
# statement
# statement

# Eg:1
# To print the value from 1 to 10 using for loop
'''
for i in range (0, 10):
    print("hello")
'''
'''
#Eg:2
for val in range(1,15,2):
     print(val)


#Eg:3
for val in range(1,15,3):
     print(val)

'''

#Eg:4
# To decrement the value
'''
for val in range (10, 0, -1):
    print(val)

'''

# Eg:4
# print the output of 7th multiplication table from 21 to 43
'''
for val in range (1,10+1):
    print("the value is",val*7)


for val in range (1,10+1):
    print('7','x',val,'=',val*7)


for val in range (1,10+1):  ----> method 1
    print('7','x',val,'=',val*7)





for val in range (1,10+1): ----> method 2
    ans="7x{}={}"
    print(ans.format(val, val*7))




for val in range (1,10+1):     ----> method 3
    print(f"7x{val}={val*7}")

'''

# Eg:5
# break ---> used to terminate the loop
'''
for val in range(1,10):
    if val==6:
        break
    print(val)

'''

# Eg:7
'''
for val in range(1,10):
    if val==6:
        print(val)
        break

'''

# continue

# Eg:1
'''
for val in range(1,10):
    if val==6:
        continue
    print(val)
'''

# Practise problems
# Print the even number between 20 to 40
'''
for val in range (20,40,2):
    print(val)
'''

'''
for val in range (20,40):
    if val %2==0:
          print(val)
  
'''

# ---> While loop

#while loop is used when we do not know the number of times the loop have to run to iterate the non iterable elements while loop is used.

# Syntax

# initialisation
# while condition
# statement
# incre or decre


#  Eg:1

# to literate number from 1 to 10
'''
i=0
while i<11:
    print(i)
'''


# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432



# Write a program to display sum of odd numbers and even


print("Hello {0[0]} and {[1]}".format(('foo','bin')))



















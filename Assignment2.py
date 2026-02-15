                            # Part A: Loops (Very Easy)

# Q1. Print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)
print("-"*30)


# Q2. Print even numbers from 2 to 20 using a for loop.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("-"*30)


# Q3. Print all characters of the string "Python" using a loop.

word = "Python"
for char in word:
    print(char)
print("-"*30)


# Q4. Print numbers from 5 to 1 using a loop.

i = 5
while i > 0:
    print(i)
    i -= 1
print("-"*30)


# Q5. Use a while loop to print numbers from 1 to 5.

i = 1
while i <= 5:
    print(i)
    i += 1
print("-"*30)



                                # Part B: Functions (Very Easy)

# Q6. Create a function that prints "Hello Python" when called.

def call():
    print("Hello Python")
call()
print("-"*30)


# Q7. Create a function that takes one number and prints it.

def num(a):
    print(a)
num(5)
print("-"*30)


# Q8. Create a function that takes two numbers and prints their sum.

def add(a, b):
    sum = a + b
    print(sum)
add(5, 10)
print("-"*30)
    

# Q9. Create a function that takes one number and checks whether it is even or odd.

def check(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check(5)
print("-"*30)


# Q10. Create a function that prints numbers from 1 to 5 using a loop.

def numbers(n):
    for i in range(1, n+1):
        print(i)
numbers(10)
print("-"*30)


                                # Mini Project
                                # Tables

def numberTable():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num," * ", i, " = ", num*i)

numberTable()
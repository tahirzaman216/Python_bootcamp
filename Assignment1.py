                                # Part A
                  
#Q1. Create a variable name and store your name in it. Print the variable

name = "Tahir Zaman"
print("Your name is: ", name)


# Q2. Create two variables age and height. Print both values.

age = 21
height = 5.9
print("Age: ", age, "Height: ", height)


# Q3. Store a number in a variable and print its data type using type().

num = 56
print(type(num))

# Q4. Create a variable is student and store True in it. Print the value.

student = True
print(student)


# Q5. Take one number from the user and store it in a variable. Print the number.

phone_no = int(input("Enter your phone: "))
print(phone_no)



                                    #  Part B
# Q6. Take two numbers from the user and print their sum.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
sum = num1 + num2
print("Sum = ", sum)

# Q7. Take two numbers and check which one is greater using if.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
if num1 > num2:
    print("Num1 is greater than num2")
else:
    print("Num2 is greater")


# Q8. Take one number and check whether it is even or odd.

num1 = int(input("Enter a first number: "))
if num1 % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# Q9. Take marks as input and print:
# • Pass if marks are 50 or above
# • Fail otherwise

marks = int(input("Enter Marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# Q10. Take a number and check:
# • Less than 10
# • Equal to 10
# • Greater than 10

num = int(input("Enter a number: "))
if num < 10:
    print("Num is less than 10")
elif num == 10:
    print("Num is equal to 10")
else:
    print("Num is greater than 10")



                                # Mini Project


num = int(input("Enter a number: "))
if num > 0:
    print("Number is positive")
else:
    print("Number is negative")
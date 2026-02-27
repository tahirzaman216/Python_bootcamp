                                # Set Questions
# 1.	Create a set of your favorite 5 fruits. Add one more fruit and remove one fruit from the set. Print the final set.
fruits = {"Mango", "Apple", "Banana", "Watermelon", "Orange"}
fruits.add("Gawa")

print(fruits)


# 2.	Write a program to find the union and intersection of the following sets:
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}

union = set1.union(set2)
print(union)


intersection = set1.intersection(set2)
print(intersection)

                                # Tuple Questions
# 3.	Create a tuple with 5 numbers. Print the first and last number.

number = (1, 2, 3, 4, 5)
print(number[0])
print(number[len(number)-1])

# 4.	Given the tuple (10, 20, 30, 40, 50), write a program to find the sum of all elements.
tup = (10, 20, 30, 40, 50)
sum = 0 
for i in tup:
    sum += i
print("sum = ", sum)

# 5.	Try to change the second element of the tuple (1, 2, 3) to 5. Observe what happens and explain why.
num = (1, 2, 3)
# num[1] = 5  
        # it gives error because it tuple is immutable

# 6.	Create a list of 5 cities. Add one more city at the end and insert another city at the second position. Print the updated list.
cities = ["Mardan", "Sawabi", "Peshawar", "Swat", "Dir"]
cities.append("Islamabad")
cities.insert(1, "Multan")
print(cities)

# 7.	Given the list [2, 4, 6, 8, 10], write a program to double each number and store it in the same list.
num = [2, 4, 6, 8, 10]
for i in range(len(num)):
    num[i] = num[i] * 2

print(num)

# 8.	Create a dictionary to store student marks for 3 subjects. Print the marks of one subject.

subjects = {"English" : 88,
            "Urdu" : 77,
            "Computer Science" : 95}

print(subjects["Computer Science"])

# 9.	Update the marks of one subject and add a new subject with marks. Print the updated dictionary.

subjects["English"] = 66
print(subjects)

subjects["Pak Studies"] =  82
print(subjects)

# 10.	Write a program to loop through a dictionary and print all keys and values in the format:
# Subject: Marks

for subject, marks in subjects.items():
    print(f"{subject} : {marks}")


                                # Mini Project

sub = {}
for i in range(3):
    subj = input("Enter subject name: ")
    mar = int(input("Enter the Obtained Marks: "))
    sub[subj] = mar

print("Subjects and Marks\n", sub)

total = sum(sub.values())
average = total / len(sub)

if 80 <= average <= 100:
    print("Grade A")
elif 60 <= average < 80:
    print("Grade B")
elif average < 60:
    print("Grade C")
else:
    print("Invalid Average")


        

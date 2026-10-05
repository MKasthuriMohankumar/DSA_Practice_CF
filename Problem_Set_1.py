#Prob 1

# Input:  2 Name y

# Expected Output:

# 2

# Name

# y

# num = int(input("Enter a number: "))
# name = input("Enter a string: ")
# character = input("Enter a character: ")
# print(num); print(name); print(character)

#---------------------------------------------

# Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

# If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.

# Input: 45 45 45

# Expected Output: 

# Triangle cannot be formed

# Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output.

angle_1 = int(input("Enter the first angle: "))
angle_2 = int(input("Enter the second angle: "))
angle_3 = int(input("Enter the third angle: "))

total = angle_1 + angle_2 + angle_3

if total == 180 and angle_1>0 and angle_2>0 and angle_3>0:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")

#-------------------------------------------------------

# Prob 3: 

# Given mark of student, Print the Grade

# Grade A if mark is greater than or equal to 90

# Grade B if mark is greater than or equal to 80

# Grade C if mark if greater than or equal to 60

# Grade D if mark if greaer than or equal to 35

# Fail if mark is lesser than 35

# Input: 95

# Expected Output:

# Grade A

# Explanation: Here 95 is greater than or equal to 90 so its Grade A

# mark = int(input("Enter your mark: "))

# if mark >= 90:
#     print("Grade A")
# elif mark >= 80:
#     print("Grade B")
# elif mark >= 60:
#     print("Grade C")
# elif mark >= 35:
#     print("Grade D")
# else:
#     print("Fail")
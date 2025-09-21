# Task_1
# Program to check if a number is even or odd

# 1. Take integer input from the user
num = int(input("Enter an number: "))

# 2. Check whether the number is even or odd
if num % 2 == 0:

# 3. Display result
    print(num, "is an Even number.")

else:
    print(num, "is an Odd number.")



# Task_2
# Program to find the sum of integers from 1 to 50

# Step 1: initialize
total = 0

# Step 2: use for loop from 1 to 50
for i in range(1, 51):
    total = total + i

# Step 3: print  result
print("The sum of numbers from 1 to 50 is:", total)

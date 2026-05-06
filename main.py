# ================================
# Task 1: Variables & Data Types
# ================================

name = "Rosemary"
age = 25
height = 5.6
is_student = True
fruits = ["apple", "banana", "orange", "mango", "grape"]

print("=== Task 1: Variables & Data Types ===")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Fruits: {fruits}, Type: {type(fruits)}")


# ==========================================
# Task 2: User Input & Conditional Logic
# ==========================================

print("\n=== Task 2: Voting Eligibility ===")

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ================================
# Task 3: Loops
# ================================

print("\n=== Task 3: Loops ===")

print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\nEven numbers from 1 to 20:")
num = 2
while num <= 20:
    print(num)
    num += 2


# ===================================
# Task 4: Mini Challenge
# ===================================

print("\n=== Task 4: Fruits in Uppercase (Skipping Banana) ===")

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit.upper())

"""
1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
"""

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n_terms = int(input("Enter the number of terms: "))

if n_terms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n_terms):
       print(fibonacci(i))

"------------------------------------------------------------------------------------------------------------------"


"""
2. Write a Python Program to Find Factorial of Number Using Recursion?
"""

def factorial(n):
   if n == 1:
       return n
   else:
       return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", factorial(num))

"------------------------------------------------------------------------------------------------------------------"

"""
3. Write a Python Program to calculate your Body Mass Index?
"""

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your Body Mass Index (BMI) is: {:.2f}".format(bmi))

if bmi < 18.5:
   print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
   print("You are of normal weight.")
elif bmi >= 25 and bmi < 30:
   print("You are overweight.")
else:
   print("You are obese.")

"------------------------------------------------------------------------------------------------------------------"


"""
4. Write a Python Program to calculate the natural logarithm of any number?
"""

import math

num = float(input("Enter a number: "))

if num <= 0:
   print("Invalid input. Please enter a positive number")
else:
   ln = math.log(num)
   print("The natural logarithm of", num, "is", ln)

"------------------------------------------------------------------------------------------------------------------"

"""
5. Write a Python Program for cube sum of first n natural numbers?
"""

n = int(input("Enter a number: "))

sum = 0

for i in range(1,n+1):
   sum += i**3

print("The cube sum of first", n, "natural numbers is", sum)
"------------------------------------------------------------------------------------------------------------------"


# str1 = "apna"
# str2 = "college"
# print(str1+str2)
# str1 = "apna college"
# print(str1[6:])

# str = "i am studying python from apna college"
# print(str.replace("o", "a"))

# def welcome_message():
#     print("Welcome to Python Functions!")
# welcome_message()

# def multiply(a,b):
#     return a*b
# multiply(5,3)
# result = multiply(5,8)
# print(result)

# num_str = input("enter a number as a string: ")
# num_int = int(num_str)
# result = num_int+5
# print(result)

def factorial(n):
    if n==1 or n == 0:
        return 1
    return n * factorial(n-1)
n = int(input("enter a number: "))
print(factorial(n))


#recursion question ------>

import math

# 1️⃣ Factorial (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 2️⃣ Fibonacci Sequence (Recursive)
def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)
fibonacci(10)

# 3️⃣ Sum of Natural Numbers (Recursive)
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

# 4️⃣ Power Function (Recursive)
def power(base, exp):
    if exp == 0:
        return 1 
    else:
        return base * power(base, exp - 1)

# 5️⃣ Reverse a String (Recursive)
def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# 💡 Challenge-Level Coding Questions

# 6️⃣ Recursive Digit Sum
def digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + digit_sum(n // 10)

# 7️⃣ Palindrome Check (Recursive)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# 8️⃣ GCD (Recursive)
def gcd(a, b):
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)

# 9️⃣ Sum of Squares of first n numbers (Recursive)
def sum_of_squares(n):
    if n == 0:
        return 0
    else:
        return n**2 + sum_of_squares(n - 1)

# 🔟 Menu-Driven Program
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Addition of two numbers")
        print("2. Factorial of a number (Recursive)")         
        print("3. Area of Circle")
        print("4. Square Root of a number")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Addition =", a + b)
        elif choice == '2':
            n = int(input("Enter a number: "))
            print(f"Factorial of {n} =", factorial(n))
        elif choice == '3':
            r = float(input("Enter radius of circle: "))
            print(f"Area of Circle = {math.pi * r**2}")
        elif choice == '4':
            x = float(input("Enter number: "))
            print(f"Square Root = {math.sqrt(x)}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

# Uncomment below lines to test individual functions:
# print(factorial(5))

# print(sum_natural(10))
# print(power(2, 5))
# print(reverse_string("hello"))
# print(digit_sum(12345))
# print(is_palindrome("racecar"))
# print(gcd(48, 18))
# print(sum_of_squares(5))

# Start the menu-driven program
menu()
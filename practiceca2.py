def add_numbers(a,b):
    sum = a+b
    return sum
print(add_numbers(5,7))


def is_even(n):
    return n%2==0
print(is_even(5))


num_str = input("enter a number: ")
num = int(num_str)
result = num*2
print(result)


a = 8
b = 8.5
result = a + b
print(result)
print(type(result))


import math
def circle_area(radius):
    return math.pi*radius**2
print("area ", circle_area(6))

def print_info(name,age,city):
    print(f"My name is{name}, my age is {age}, My city is {city}")
print_info("shivam", 14,"baghpat")

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
nums = [1,2,4,5,6]
print(sum_list(nums))

def man_list(lst):
    if len(lst) == 1:
        return lst[0]
    sub_max = man_list(lst[1:])
    return lst[0] if lst[0]>sub_max else sub_max
print(man_list([3,5,4,7,9]))

def reverse_str(s):
    if len(s)==0:
        return s
    return s[-1] + reverse_str(s[:-1])
s = "Shivam"
print(reverse_str(s))

import math
radius = float(input("Enter a value: "))
area = math.pi*radius**2
area_round = round(area, 2)
print(area_round)

def freq_dict(arr):
    freq={}
    for num in arr:
        freq[num] = freq.get(num,0)+1
    return freq
arr = [1,2,4,5,6,7,9]
result=freq_dict(arr)
print(result)

text = "hello world"
freq = {}

for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

print(freq)

def calc_interest(principal, year):
    interest = principal * 0.05 * year
    return interest
principal = int(input(10))
year = int(input(4))
total_int = calc_interest(principal, year)
print(f"{total_int:.2f}")


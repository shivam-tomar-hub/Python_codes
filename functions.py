def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum
calc_sum(5, 10)
calc_sum(12, 17)

# #average of  3 numbers

def calc_avg(a, b,  c):
    sum =  a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(98, 97, 95)

def cal_prod(a=1, b=1):
    print(a * b)
    return a * b
cal_prod()

# cities = ["delhi", "gurgaon", "noida", "pune", "chennai"]     
# heroes = ["thor", "ironman", "america", "shktiman"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)
                                 
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact  *= i
# print(fact)

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(73)

# #print n to 1 backwwards
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)


# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg
# calc_avg(9,4,2)
# def calc_prod(a,b=6):
#     print(a*b)
#     return a*b
# calc_prod(3)

# n = 5 
# fact = 1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)

#function with arguments   

def goodDay(name,ending):
    print("Good day," + name)
    print(ending)
goodDay("harry","ok")
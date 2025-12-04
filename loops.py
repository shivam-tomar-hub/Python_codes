hhh#ques 1
i = 1
while i <= 100:
    print(i)
    i += 1

#ques 2
i = 100
while i >= 1:
    print(i)
    i -= 1

#ques 3
i  = 1
while i <= 10:
    print(4*i)
    i+=1

#ques 4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx  = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
#QUES 5
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
#ques 6
nums = [1,2,3,4,5,6]
for val in nums:
    print(val)

#qus 7
str = "apnacollege"
for char  in  str:
    print(char)

#using for
nums = (1,4,9,16,25,36,49,64,81,100)
x  = 49
idx = 0
for el in  nums:
    if(el == x):
        print("number found at idx", )
    idx += 1

n = int(input("enter number : "))
for i in range(1, 11):
    print(n * i)

n  = 5
sum = 0
for i in range(1,n+1):
    sum  += i

    print("total sum : ", sum)

for i in range(0,100):
    if i % 2 == 0:
        print(i)
i = 1
while i<=20:
    if (i%2!=0):
        i+=1
        continue
    print(i)
    i+=1

for i in range(2, 100, 2):
    print(i)
info = {
    "Name" : "Shivam Tomar",
    "Age" : "13",
    "marks" : [9, 6, 4]
}
print(info["Name"])
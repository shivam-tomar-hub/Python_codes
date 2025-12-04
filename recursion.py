def show(n):
    
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END")
show(5)

#factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("enter a number: "))
print(f"The factorail of this number is : {factorial(n)}")

#greatest of three number 
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 1
b =2
c =3 
print(greatest(a,b,c))

#pattern
def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)
pattern(4)
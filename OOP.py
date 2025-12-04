# class Student:
   
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")

# s1 = Student("karan", 88)
# print(s1.name, s1.marks)
# s2 = Student("arjun", 97 )
# print(s2.name, s2.marks)


# class Student:
#     college_name = "ABC college"
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks

#     def Welcome(self):
#         print("Welcome student", self.name)
# s1 = Student("karan", 97)
# s1.Welcome()


# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#             print("hi", self.marks, "your avg marks is: ", sum/3)
# s1 = Student("tony stark", [99,98.96])
# s1.get_avg()


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started..")
# car1 = Car()
# car1.start()


# class Person:
#     name = "Harry"
#     occ  = "Developer"

#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a  = Person()
# a.name = 'Harry'
# a.occ =  "HR"
# a.info()


#Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
# car1 = ToyotaCar("fortuner")
# car2= ToyotaCar("prius")

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage = str((self.phy + self.math + self.chem) / 3) + "%"
    
#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.math + self.chem) / 3) + "%"
    
# stu1 = Student(98, 97, 90)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# print(stu1.percentage)


#Polymorphism: Operator Overloading
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img=img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
num1 = Complex(4,6)
num1.showNumber()

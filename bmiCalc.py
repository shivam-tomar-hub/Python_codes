# BMI Calculator
# Underweight = <18.5
# Normalweight = 18.5-24.9
# Overweight = 25-29.9
# Obesity = BMI of 30 or greater
while True:


   height = float(input("Enter your height in cm: "))
   height = height / 100
   weight = float(input("Enter your weight in kg: "))

   BMI = round(weight / (height * height), 2)
   print(f"your body mass index(BMI) is {BMI}")
   if(BMI<=18.5):
      print("You are underweight")
   elif(BMI<=24.9):
      print("You are healthy")
   elif(BMI<=29.9):
      print("You are overweight")
   else:
      print("You are obese")
   UserWantsToContinue = input("Do you want to continue? (yes/No): \n")
   if(UserWantsToContinue == "no"):
      print("over")
      break
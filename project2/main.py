import time


print("Interactive Symptom Checker")
print("👋 Hello there! Let's check how you're doing today.")

print("👋 Hello there! Let's check how you're doing today.")

print(".👤 Personal Detail")

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
gender=["male","female","other"]
city=input("Please enter your city: ")

#🤒 2. Health Inputs
print("choose your symptoms from the list below:")
Main_symptoms=input(["fever","cough","headache","fatigue","breathlessness","chest pain"])
               
Body_emperature=float(input("Please enter your body temperature in Fahrenheit: ")) 
Number_of_sick_day=int(input("Please enter the number of sick days you have taken: "))
Smoking_habit=input("Do you smoke? (yes/no): ").lower()
sleep_hours=int(input("Please enter the number of hours you sleep: "))
Mood=input("How do you feel today? (happy/sad/angry/anxious/calm/irritable): ").lower()
Pre_existing_conditions=input("Do you have any pre-existing conditions? (yes/no): ").lower()
#Risk Scoring Logic

if  Body_emperature >= 102  and  Main_symptoms["Fever"] or Number_of_sick_day > 3:
    health_point1=2
elif age >= 60 and Main_symptoms["Fever"]:
    health_point2=2
elif Number_of_sick_day >= 5 and Main_symptoms["Cough"]:
    health_point3=2
elif age> 30 and Main_symptoms["Fatigue"]:
    health_point4=2 
elif Main_symptoms["Headache"] and Body_emperature > 100:
    health_point5=2 
elif Main_symptoms["Chest pain"]:
    health_point6=2
elif Main_symptoms["Breathlessness"]:
  health_poin7t=4
elif Smoking_habit== "yes":
    health_point8=2
elif sleep_hours < 6:
  health_point9=1
elif Mood== "anxious" or "irritable" or "sad":
     health_point10=1
elif Pre_existing_conditions== "yes":
    health_point11=2
else:
    print("No points")

    #📊 4. Health Risk Result
    health_point =health_point1 + health_point2+health_point3+health_point4+health_point5+health_point6+health_point7+health_point8+health_point9+health_point10+health_point11
if health_point >= 3:
    print("🟢 Low Risk.")
elif health_point ==4 < 6:
    print("🟡 Medium Risk.")
elif health_point >= 7:
    print("🔴 High Risk.")





print(f"Processing your input data.......")
time.sleep(2)

print(f"Your Health Summary for {name}:")
print(f"Name: {name}")
print(f"{health_point}: Monitor closely. Seek advice if it continues.")
print(f"✅ Thank you {name} for using QuickHealth Pro Max. Get well soon! 💙")
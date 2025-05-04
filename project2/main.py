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

if  Body_emperature >= 102  and  Main_symptoms["Fever"]or Number_of_sick_day > 3:
    print("+3 points")
elif age >= 60 and Main_symptoms["Fever"]:
    print("+2 points")
elif Main_symptoms["Cough"]>= 5:
    print("+2 points")
elif Main_symptoms["Fatigue"]== age> 30:
     print("+2 points")  
elif Main_symptoms["Headache"] and Body_emperature > 100:
     print("+2 points") 
elif Main_symptoms["Chest pain"]:
    print("+2 points")
elif Main_symptoms["Breathlessness"]:
    print("+4 points")
elif Smoking_habit== "yes":
    print("+2 points")
elif sleep_hours < 6:
    print("+1 points")
elif Mood== "anxious" or "irritable" or "sad":
    print("+1 points")
elif Pre_existing_conditions== "yes":
    print("+2 points")
else:
    print("No points")

    #📊 4. Health Risk Result
 health_risk_score = str(sleep_hours)+str(Pre_existing_conditions)+str(Smoking_habit)+str(Main_symptoms)
if health_risk_score >= 3:
    print("🟢 Low Risk.")
elif health_risk_score ==4 < 6:
    print("🟡 Medium Risk.")
elif health_risk_score >= 7:
    print("🔴 High Risk.")
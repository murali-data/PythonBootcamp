
from asyncio import sleep
import datetime
import time
#get user name 
user_name=input("enter the user name:")
#get user age
user_age=int(input("enter the user age:"))
# Convert to months
age_in_months =user_age*12
#get user city 
user_city=input("enter the user city:")
#get user favorite food 
user_favorite_food=input("enter your favorite food:") 
#get user favorite colour
user_favorite_colour=input("enter your favorite colour:") 
#get user spirit animal
user_spirit_animal=input("enter your spirit animal:") 
#get user love to doing
user_loveto_doing=input("enter one thing you love doing:\n")
personality_code=user_name[:2].upper() + str(user_age)[-1] + user_spirit_animal[0] + user_favorite_colour[0]
print("=" * 140)
print("Let's discover who you really are with some fun data magic!")
print("=" * 140)
print("Scanning colors, foods, and animal energies...")
time.sleep(3)
print("=" * 140)
print(" Calculating your personality type using complex non-scientific logic...")
time.sleep(5)
print("=" * 140)
print(f"Hey {user_name}, here's your fun personality report!")
print(f"🌆You're from {user_city}, a place of dream")
print(f"🍿You love {user_favorite_food} and enjoy doing {user_loveto_doing}.")
print(f"🎨You vibe with the color {user_favorite_colour} and your spirit animal is the {user_spirit_animal}.")
print(f"📅You've lived approximately {age_in_months} months already.")
if user_age < 18:
   Young_Explorer ="Young Explorer"
   print(f"🧩You belong to the {Young_Explorer} tribe.")
elif 18 <= user_age <= 30:
   Adventurer="Adventurer"
   print(f"🧩You belong to the {Adventurer} tribe.")
elif user_age > 30:
   Wise_Owel="Wise Owl"
   print(f"🧩You belong to the {Wise_Owel} tribe.")
print(f"🔐 Your Secret Personality Code is: 💡 {personality_code}")





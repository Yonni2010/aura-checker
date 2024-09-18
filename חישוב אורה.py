age = float(input("מה הגיל שלך:"))
mewing_in_a_day = float(input("כמה שעות אתה עושה מיוינג ביום:"))
place = str(input("איפה אתה גר:"))
name = str(input("מה שמך:"))

aura = float(0)

if (age > 12 and age<16):
    aura==aura + 10000
    
elif (age < 5):
    print("ילד מה אתה עושה פה")
    aura = -50000
    
else:
       aura=aura + 300
    

if (mewing_in_a_day > 5):
    aura=aura + 20000
    
elif (mewing_in_a_day == 0):
    aura = aura - 500
    
else:
       aura=aura + 3000
    

if (place == "צכיה" or place == "צ'יכה" or place == "שמיר"):
    aura=aura + 20000
    
elif (place == "להבות"):
    aura = aura - 50000
    
else:
       aura=aura + 3000
    

if (name == "יוני" or name == "קציצה" or name == "ניצן" or name == "נקציצן"):
    aura = "אינסוף"
    
elif (name == "נהוראי"):
    aura = aura - 50000
    
else:
       aura=aura + 3000

print(":נקודות אורה")
print("...מחשב")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(":נקודות אורה "+aura)


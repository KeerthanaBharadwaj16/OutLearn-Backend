import json

datas = open("ques.json")
data = json.load(datas)

score = 0.0
age = int(input("Enter your age: "))

if age > 5 and age <= 10:
    score = 1.0
    
elif age > 10 and age <= 15:
    score = 2.0
elif age > 15 and age <= 20:
    score = 3.0
else:
    score = 4.0

print("Your initial score is: ", score)

for i in data:
    print(i.get("Questions"))
    print(i.get("Option 1"))
    print(i.get("Option 2"))
    print(i.get("Option 3"))
    print(i.get("Option 4"))
    choice = input("Enter your choice: ")
    print("-" * 30)

    if int(i.get("Index")) == 1:
        if choice == "yes|YES":
            if age>5 and age<=10:
                score += 1.0
            elif age>10 and age<=15:
                score+=1.0
            elif (age>15 and age<=20) or age>20:
                pass
        else:
            if age>5 and age<=10:
                pass
            elif age>10 and age<=15:
                pass
            elif (age>15 and age<=20) or age>20:
                score -= 1.0

    elif int(i.get("Index")) == 2:
        if choice == "yes|YES":
            score += 1.0
        else:
            score -= 1.0

    elif int(i.get("Index")) == 3:
        pass

    elif int(i.get("Index")) == 4:
        if choice == str(i.get("Answers")) or choice == "I don’t know":
            score += 0.5

    elif int(i.get("Index")) == 5:
        if choice == str(i.get("Answers")) or choice == "I don’t know":
            score += 0.5

    elif int(i.get("Index")) == 6:
        if choice == str(i.get("Option 1")):
            if score >= 3.0: score = 2.0
            else: score = 1.0
        if choice == str(i.get("Option 2")):
            if score >= 3.0: score = 2.0
            else: score = 2.0
        if choice == str(i.get("Option 3")):
            if score >= 3.0: score = 3.0
            else: score = 2.0

    elif int(i.get("Index")) == 7:
        pass

    elif int(i.get("Index")) == 8:
        pass

print("Your final score is: ", score)
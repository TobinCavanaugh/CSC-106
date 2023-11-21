ADULT = "ADULT"
CHILD = "CHILD"
BABY = "BABY"
TEMP = "TEMPERATURE"
AGE = "AGE"

age = input("Age")
temp = float(input("Temperature"))

if(temp <= 95):
    print("Hypothermia, Seek Care")

elif(temp >= 95.1 and temp <= 96.9):
    if(age == BABY):
        print("Low, Seek Care")
    else:
        print("Low, Possibly normal")
    
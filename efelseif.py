marks = int(input("Enter Marks :"))

if marks > 80 and marks <= 100:
    print("you have an A")
elif marks > 60 and marks <= 80:
    print("you have B")
elif marks > 50 and marks <= 60:
    print("you have a C")
else:
    print("you failed")

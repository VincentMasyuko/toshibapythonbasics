# list are ordered mutable
fruits = ['Mangoes', "Oranges", "Banana", "Watermelon", ]
fruits.sort()
num = [11, 3, 7, 0, 14, -3, 2]
num.sort()
num[3] = 9
rep = num * 2
print(len(num))

print(fruits)
fruits[1] = "Apples"
print(f" I love eating {fruits[1]}")
print(num)
print(rep)

# Tuples immutables ordered
cars = ("Toyota", "Mercedes", "nissan", "nissan")
# cars[0]="vw"
print(cars[0])
tup = cars * 3
print(tup)
print(tup.count("nissan"))

# sets unordered
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
print(days)

# dictionaries

staff_details = {"Name": "Vincent", "Age": 30, "company": "eMobolis", "gender": "male", "salary": 564756}
print(staff_details)
print(f"Name  %s" % staff_details["Name"])
print(f"Age %d" % staff_details["Age"])
print(f"company %s" % staff_details["company"])


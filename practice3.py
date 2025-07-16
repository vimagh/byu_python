first = int(input("What is the first number? "))
second = int(input("What is the second number? "))

if first > second:
    print("The fist number is greater. ")
else:
    print("The first number is not equal. ")

if first == second:
    print("The numbers are equal. ")
else:
    print("The numbers are not equal. ")

if second > first:
    print("The second is greater then the first. ")
else:
    print("The second is not greater than the first. ")

print()

animal = input("What is your favourite animal? ")

if animal.lower() == "Bear":
    print("That's my favourite animal too! ")
else:
    print("That one is not my fave. ")
grade = float(input("What is the percentge? "))

letter = ""

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else: 
    letter = "F"
#Showing the Sign of the grade.

sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

if letter == "A" and sign =="-":
    sign = ""
elif letter == "F" and sign == "-" or sign == "+":
    sign = ""

print(f"Your grade is {letter}{sign}")

if grade >= 70:
    print("Congratulations, you made the cut")
else:
    print("Please take the course again")
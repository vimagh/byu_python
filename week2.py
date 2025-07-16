import math
# For creativity, an if statement was added where the user is prompted to give the Change to charity.
# The user gets a prompt based on the answer they choose.

child = float(input("What is the price of a child's meal? $"))
adult = float(input("What is the price of an adult's meal? $"))

child_number = int(input("How many children are there? " ))
adult_number = int(input("How many adults are there? "))

childtotal = (child * child_number)

adulttotal = (adult * adult_number)


subtotal = float(childtotal + adulttotal)
print(f"the subtotal is ${subtotal}")

tax_rate = float(input("What is the sales tax rate? "))
sales_tax = float(subtotal * tax_rate)
total = float(subtotal + sales_tax)

print(f"The total payment is ${total}")

payment_amount = int(input("What is the payment amount? "))
change = float(payment_amount-total)

print(f"The change is ${change: .2f}")

donate = input("Will you like to donate your change to Charity? Yes / No ")
if donate == "Yes":
  print("Thank you for giving for a good cause!.")
else:
  print("Thank you for the patronage.")

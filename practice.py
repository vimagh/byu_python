"""
Author: Vimagh Solomon
Purpose: Creatig an ID Badge

"""
print("Enter the details below")

print()

first_name = input("First name:")
last_name = input("Last name: ")
email = input("Emial:")
phone_number = input("Phone number:")
job_title = input("Job title:")
id_number = input("ID:")

print("The ID card is:")

print("--------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"{id_number}")
print()
print(f"{email.lower()}")
print(f"{phone_number}")
print("---------------------------------")

x = 2
y = 3
z = 4  

w = x + y * z  

print(w)
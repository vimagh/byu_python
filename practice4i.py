fave = input("what is your favurite letter? ")
word = "success"

for i in word:
    if i.lower() == fave.lower():
        print(i.upper(), end = "")
    else:
        print(i.lower(), end = "")
fave = input("what is your favurite letter? ")
word = "success"

for i in word:
    if i.lower() == fave.lower():
        print("_", end = "")
    else:
        print(i.lower(), end = "")

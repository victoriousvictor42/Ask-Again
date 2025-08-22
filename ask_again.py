name=input("What is your name: ")

while name=="":
    print("You did not type anything!")
    name=input("What is your name: ")
    

print(f"Your name is {name}")
import random
name = input("What is your name? ")
name = "Marvin"
adjectives = ["Sneaky", "Silent", "Shadow", "Swift", "Clever", "Mysterious"]
adjectives = "Shadow"
animals = ["Otter", "Fox", "Tiger", "Eagle", "Panther", "Wolf"]
animals = "Fox"
codename = "Shadow" + "Marvin" + "Fox"
lucky_number = random.randint(1, 99)
print(f"Agent {name}, your codename is {codename}!")
print(f"Your lucky number is {lucky_number}!")
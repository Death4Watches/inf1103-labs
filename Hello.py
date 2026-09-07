# Remember to cd INF1103-Labs'''

# === COMMANDS ===
# git init: initialize git repository
# git status: check the repo status
# git add: add file to the repository
# git commit -m <File Name>: create a commit
# git log: check git history
# git diff: check the difference between repo files
# git restore: restore previous commited file
# git log >log.txt: Create Log into Text File


# ACTIVITY 1: 
print("==========")
print("Welcome Here!")
print("My first post!")
print("==========")


# ACTIVITY 2: 
username = "Death4Watches"
bio = "N/A"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)


# ACTIVITY 3: 
followers = 100
followers += 50

print("Day 1:", followers)

followers += 20
print("Day 2:", followers)

followers -= 10
print("Day 3:", followers)


# Activity 4:
username = input("Enter Username: ")
age = input("Enter Age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("==========")
print("Username: ", username)
print("Age: ", age)
print("Category: ", category)


# Activity 5:
username = input("Enter Username: ") 
age = int(input("Enter your Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("==========")
print("Username: ", username)
print("Age: ", age)
print("Category: ", category)

if age>40 and category == "fun" or "funny":
    print("You are old, what is fun for you???")


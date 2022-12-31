# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedName = name1 + name2
loweredCase = combinedName.lower()

total = 0
total2 = 0
total += loweredCase.count("t")
total += loweredCase.count("r")
total += loweredCase.count("u")
total += loweredCase.count("e")
total2 += loweredCase.count("l")
total2 += loweredCase.count("o")
total2 += loweredCase.count("v")
total2 += loweredCase.count("e")

number = str(total)+str(total2)
intNumber = int(number)

if intNumber<10 or intNumber>90:
    print(f"Your score is {intNumber}, you go together like coke and mentos.")
elif intNumber>40 and intNumber<50:
    print(f"Your score is {intNumber}, you are alright together.")
else:
    print(f"Your score is {intNumber}.")

# importing random
import random

# intro
print("You have 4 chances to solve 4 sums\nGood Luck!!!\n\n")

# score
scr = 0

# for Q1
number1 = (random.randint(1,99))
number2 = (random.randint(1,99))

# Question 1
print("Here's question 1 :-\n")
print(number1 , "+" , number2)
s1 = number1 + number2
u1 = int(input("Enter your answer..."))
if(u1 == s1):
    print("\nYou got it right!\n\n")
    scr = scr + 1
else:
    print("\nOops...Incorrect!\nThe answer was" , s1 , "\n\n")

# for Q2
number3 = (random.randint(50,99))
number4 = (random.randint(1,50))

# Question 2
print("Here's question 2 :-\n")
print(number3 , "-" , number4)
s2 = number3 - number4
u2 = int(input("Enter your answer..."))
if(u2 == s2):
    print("\nYou got it right!\n\n")
    scr = scr + 1
else:
    print("\nOops...Incorrect!\nThe answer was" , s2 , "\n\n")

# for Q3
number5 = (random.randint(1,10))
number6 = (random.randint(1,50))

# Question 3
print("Here's question 3 :-\n")
print(number5 , "x" , number6)
s3 = number5 * number6
u3 = int(input("Enter your answer..."))
if(u3 == s3):
    print("\nYou got it right!\n\n")
    scr = scr + 1
else:
    print("\nOops...Incorrect!\nThe answer was" , s3 , "\n\n")

# for Q4
number7 = (random.randint(1,50)*2)
number8 = (random.randint(1,5)*2)

# Question 4
print("Here's question 4 :-\n")
print(number7 , "÷" , number8)
s4 = number7 / number8
u4 = float(input("Enter your answer..."))
if(u4 == s4):
    print("\nYou got it right!\n\n")
    scr = scr + 1
else:
    print("\nOops...Incorrect!\nThe answer was" , s4 , "\n\n")

# printing score and comments
print("Your total score is " , scr,"/4")

if(scr == 4):
    print("WOW!..Amazing performance!")
elif(scr == 3):
    print("Good")
elif(scr == 2):
    print("Better luck next time")
elif(scr<=1):
    print("You can improve yourself")

import random

run_num = random.randint(1, 9)

answer =0
while run_num != answer:
    answer = int(input("What is the magic number? "))
    if answer != run_num:
        print("Wrong! Try again.")
        
print (f"{answer} is correct! The magic number was {run_num}.")
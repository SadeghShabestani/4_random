import termcolor2
import random

computer = random.randint(0, 20)
user = -1
numbers = []
while computer != user:
    user = int(input("Enter Number: "))
    numbers.append(user)
    if computer == user:
        print(termcolor2.colored(f"*GoodJob*", color="green"))
        print(f"User Numbers: {len(numbers)}")
    elif computer > user:
        print(termcolor2.colored(f"*Enter Larger Number*", color="red"))
    elif computer < user:
        print(termcolor2.colored(f"*Enter Smaller Number*", color="red"))
    else:
        print(termcolor2.colored(f"Please! TrayAgain", color="red"))

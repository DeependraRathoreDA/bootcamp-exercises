import random
import os
def one():
    top = ' '
    bottom = ' '
    for i in range(10):
        top += '--'
    print(top)
    for left_side in range(10):
        print('--                 --')
        if left_side == 4:
            print('--       0         --')
    for i in range(10):
        bottom += '--'
    print (bottom)
def two():
    top = ' '
    bottom = ' '
    for i in range(10):
        top += '--'
    print(top)
    for left_side in range(10):
        print('--                 --')
        if left_side == 4:
            print('--       0         --')
        if left_side == 6:
            print('--       0         --')
    for i in range(10):
        bottom += '--'
    print (bottom)
def three():
    top = ' '
    bottom = ' '
    for i in range(10):
        top += '--'
    print(top)
    for left_side in range(10):
        print('--                 --')
        if left_side == 2:
            print('--       0         --')
        if left_side == 4:
            print('--       0         --')
        if left_side == 6:
            print('--       0         --')
    for i in range(10):
        bottom += '--'
    print (bottom)
def four():
    top = ' '
    bottom = ' '
    for i in range(10):
        top += '--'
    print(top)
    for left_side in range(10):
        print('--                 --')
        if left_side == 4:
            print('--       0   0     --')
        if left_side == 6:
            print('--       0   0     --')
    for i in range(10):
        bottom += '--'
    print (bottom)
def five():
    top = ' '
    bottom = ' '
    for i in range(10):
        top += '--'
    print(top)
    for left_side in range(10):
        print('--                 --')
        if left_side == 4:
            print('--       0     0   --')
        if left_side == 5:
            print('--          0      --')
        if left_side == 6:
            print('--       0     0   --')
    for i in range(10):
        bottom += '--'
    print (bottom)
def six():
    top = ' '
    bottom = ' '
    for i in range(10):
        top += '--'
    print(top)
    for left_side in range(10):
        print('--                 --')
        if left_side == 2:
            print('--       0     0   --')
        if left_side == 4:
            print('--       0     0   --')
        if left_side == 6:
            print('--       0     0   --')
    for i in range(10):
        bottom += '--'
    print (bottom)
def operation():
    a = random.randint(1,6)
    if a == 1:
        one()
    elif a == 2:
        two()
    elif a == 3:
        three()
    elif a == 4:
        four()
    elif a == 5:
        five()
    elif a == 6:
        six()
    else:
        pass
print('The Dice Simulator')
os.system('Pause')
print()
operation()
user = input("Do you want to Continue ? (Y or N) ")
user = user.lower()
while user == 'y':
    operation()
    user = input("Do you want to Continue ? (Y or N) ")
    user = user.lower()
    if user == 'n':
        break
    elif user not in('y' or 'n'):
        user = input("Please enter the valid input ? ")
        if user not in('y' or 'n'):
            print("Existing the Simulator")

from random import randint

def roll():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    return dice_1, dice_2


def main():
    a = input("press enter to start the game")
    d1, d2 = roll()
    sum = d1 + d2
    print(f"{d1} + {d2} = {sum}")
    if sum in [7, 11]:
        print("you won")
    elif sum in [2, 3, 12]:
        print("you loose ")
    else:
        goal = sum
        print("Now your goal is ", goal)
        while True:
            a = input("press enter to roll dice again")
            d1, d2 = roll()
            sum = d1 + d2
            print(f"{d1} + {d2} = {sum}")

            if sum == goal:
                print("you won")
                break
            elif sum == 7:
                print("Crap, you loose :(")



if __name__ == '__main__':
    main()

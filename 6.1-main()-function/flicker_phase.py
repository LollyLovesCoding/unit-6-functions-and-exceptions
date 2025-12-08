import random
import os
import time


def main():
    for i in range(100000):
        r = random.randrange(1, 6)
        if r == 1:
            first()
            time.sleep(0.25)
        if r == 2:
            second()
            time.sleep(0.25)
        if r == 3:
            third()
            time.sleep(0.25)
        if r == 4:
            fourth()
            time.sleep(0.25)
        if r == 5:
            fifth()
            time.sleep(0.25)
                
        os.system("clear")  # clear console

    print("I pledge allegiance to the flag.");


def first():
    print("I                               ");


def second():
    print("  pledge                        ");


def third():
    print("         allegiance             ");


def fourth():
    print("                    to the      ");


def fifth():
    print("                           flag.");


if __name__ == "__main__":
    main()

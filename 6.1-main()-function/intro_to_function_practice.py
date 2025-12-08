# 1.
def main():
    name = input("Enter your name: ")

    if name == "":
        name = "User"

    print(f"Hello, {name}")

# 2.
def greet():
    print("Welcome to the awesome area calculator!")
    print()

def main():

    greet()

    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()

    area = length * width

    print(f"The area is {area} units squared")

if __name__ == "__main__":
    main()

# 3.

PRICE = 13.95

def main():
    tickets = int(input("How many tickets would you like?: "))

    print(f"Your total cost is ${round(PRICE * tickets, 2)}")

if __name__ == "__main__":
    main()
  

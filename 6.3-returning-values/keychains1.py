def add_keychains():
    print("ADD KEYCHAINS")

def remove_keychains():
    print("REMOVE KEYCHAINS")

def view_order():
    print("VIEW ORDER")

def checkout():
    print("CHECKOUT")

def main():
    print("Ye Olde Keychain Shoppe\n")

    while True:
        print("1. Add Keychains to Order\n2. Remove Keychains from Order\n3. View Current Order\n4. Checkout\n")
        choice = int(input("Please enter your choice: "))
        print("")

        if choice == 1:
            add_keychains()
        elif choice == 2:
            remove_keychains()
        elif choice == 3:
            view_order()
        elif choice == 4:
            checkout()
            break
        else:
            print("Invalid")

        print()

if __name__ == "__main__":
    main()

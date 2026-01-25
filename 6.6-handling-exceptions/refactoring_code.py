# Display menu options
print("1 - Option One")
print("2 - Option Two")
print("3 - Option Three")
print()

choice = ""

try:
    # get choice
    choice = int(input("> "))
except ValueError:
    print("Invalid option.")

# handle choice
if choice == 1:
    print("You chose OPTION ONE.")
elif choice == 2:
    print("You chose OPTION ONE.")
elif choice == 3:
    print("You chose OPTION ONE.")
else:
    print("Invalid option.")

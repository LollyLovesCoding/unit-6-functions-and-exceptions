def main():
    print("Welcome to Lilyana's fantastic birth-o-meter!")
    print()
    print("All you have to do is enter your birthday, and it will tell you")
    print("the day of the week on which you were born.")
    print()
    print("Some automatic tests....")
    print(f"12 10 2003 => {weekday(12, 10, 2003)}")  # Wednesday, December 10, 2003
    print(f"2 13 1976 => {weekday(2, 13, 1976)}")  # Friday, February 13, 1976
    print(f"2 13 1977 => {weekday(2, 13, 1977)}")  # Sunday, February 13, 1977
    print(f"7 2 1974 => {weekday(7, 2, 1974)}")  # Tuesday, July 2, 1974
    print(f"1 15 2003 => {weekday(1, 15, 2003)}")  # Wednesday, January 15, 2003
    print(f"10 13 2000 => {weekday(10, 13, 2000)}")  # Friday, October 13, 2000

    print("Now it's your turn!  What's your birthday?")
    print("Birth date (mm dd yyyy): ")
    mm = int(input("mm: "))
    dd = int(input("dd: "))
    yyyy = int(input("yyyy: "))

    birth_date = weekday(mm, dd, yyyy)
    
    print(f"\nYou were born on {birth_date}")

def weekday(mm: int, dd: int, yyyy: int) -> str:
    years_since_1900 = yyyy - 1900
    total = years_since_1900 // 4

    total += years_since_1900
    total += dd - 1
    total += month_offset(mm)
    
    if is_leap and mm == 1 or 2:
        total += 1

    weekday = weekday_name(total // 7)

    date_string = f"{weekday}, {month_name(mm)}, {yyyy}"
    return date_string

def month_name(month: int) -> str:
    result = ""
    if 0 < month < 13:
        month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for i in range(len(month_names)):
            if month == i + 1:
                result = month_names[i]
    else:
        result = "Error"
    
    return result

def month_offset(month: int) -> int:
    result = -1

    if month == 1:
        result = 1
    elif month == 2:
        result = 4
    elif month == 3:
        result = 4
    elif month == 4:
        result = 0
    elif month == 5:
        result = 2
    elif month == 6:
        result = 5
    elif month == 7:
        result = 0
    elif month == 8:
        result = 3
    elif month == 9:
        result = 6
    elif month == 10:
        result = 1
    elif month == 11:
        result = 4
    elif month == 12:
        result = 6

    return result

def weekday_name(num: int) -> str:
    if num == 1:
        return "Monday"
    elif num == 2: 
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Invalid"

def is_leap(year: int) -> bool:
    # years which are evenly divisible by 4 are leap years,
    # but years divisible by 100 are not leap years,
    # though years divisible by 400 are leap years

    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    
    return result

if __name__ == "__main__":
    main()

def main():
    print("Month 1: " + month_name(1))
    print("Month 2: " + month_name(2))
    print("Month 3: " + month_name(3))
    print("Month 4: " + month_name(4))
    print("Month 5: " + month_name(5))
    print("Month 6: " + month_name(6))
    print("Month 7: " + month_name(7))
    print("Month 8: " + month_name(8))
    print("Month 9: " + month_name(9))
    print("Month 10: " + month_name(10))
    print("Month 11: " + month_name(11))
    print("Month 12: " + month_name(12))
    print("Month 43: " + month_name(43))

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

if __name__ == "__main__":
    main()
  

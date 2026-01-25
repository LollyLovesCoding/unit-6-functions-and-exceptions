def convert_percent_values(percent_value: float) -> str:
    """
    Converts a given percent value in the range 0.0 - 1.0 into a string in the range "0%" to "100%".
    """
    if percent_value < 0.0 or percent_value > 1.0:
        raise ValueError("Percent value is out of range.") 
    if type(percent_value) is not float:
        raise ValueError("Percent value must be a float.")
    
    percent = round(percent_value * 100)
    return f"{percent}%" 

def main():
    percent_value = convert_percent_values(0.67)
    print(percent_value)

if __name__ == "__main__":
    main()
    

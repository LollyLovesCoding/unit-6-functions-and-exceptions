# 1. This file produces the exact same output as "herons_formula_no_function.py".
# 2. This file contains 25 lines of code whereas the other file has 48 lines of code (excluding most commends and including line spaces).
# 3. It was easier to fix the file that had a function because I only had to do it once.
# 4. It was considerably less difficult to add the values to the functions file because I only had to write 2 lines of code.

import math

def main():
    area = triangle_area(3, 3, 3)
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    area = triangle_area(3, 4, 5)
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    area = triangle_area(7, 8, 9)
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    area = triangle_area(5, 12, 13)
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    area = triangle_area(10, 9, 11)
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    area = triangle_area(8, 15, 17)
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")

    area = triangle_area(9, 9, 9)
    print(f"A triangle with sides 9, 9, 9 has an area of {area}")

def triangle_area(a: int, b: int, c: int) -> float:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area
    # ^ after computing the area, "return" it

if __name__ == "__main__":
    main()
  

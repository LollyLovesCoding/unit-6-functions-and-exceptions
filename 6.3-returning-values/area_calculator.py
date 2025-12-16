import math

def area_circle(radius: int) -> float:
    """Calculates the area of a circle"""
    return math.pi * radius ** 2
    
def area_rectangle(length: float, width: float) -> float:
    """Calculates the area of a rectangle"""
    return length * width

def area_square(side: float) -> float:
    """Calculate the area of a square"""
    return side ** 2

def area_triangle(base: float, height: float) -> float:
    """Calculate the area of a triangle"""
    return base * height / 2

def main():
    
    print("Shape Area Calculator version 0.1 (c) 2025 Lilyana Zhang")

    keep_going = True

    while keep_going:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")
        shape = int(input("Which shape: "))
        print("\n")

        if shape == 1:
            base = int(input("Base: "))
            height = int(input("Height: "))
            print(f"\nThe area is {area_triangle(base, height)}.")
        elif shape == 2:
            length = int(input("Length: "))
            width = int(input("Width: "))
            print(f"\nThe area is {area_rectangle(length, width)}.")
        elif shape == 3:
            side = int(input("Side: "))
            print(f"\nThe area is {area_square(side)}.")
        elif shape == 4:
            radius = int(input("Radius: "))
            print(f"\nThe area is {area_circle(radius)}.")
        else:
            print("Goodbye.")
            keep_going = False
        print("\n")

if __name__ == "__main__":
    main()
        

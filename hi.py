def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def main():
    print("Rectangle Area Calculator")
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_area(length, width)
        print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

    #fjweiofjeofckefkjeijsdceiofeiocjekjceoj ooicmeek


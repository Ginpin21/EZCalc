import math
def trigonometric():
    while(True):
        print("""
=========================================================================
        Trigonometric Functions
=========================================================================
        1. Sin function
        2. Cos function
        3. Tan function
        4. Cosec function
        5. Sec function
        6. Cot function
=========================================================================
        """)
        try:
            ch=int(input("Enter your choice: "))
            angle=float(input("Enter the angle(in degrees): "))
            rad=math.radians(angle)
            if ch==1:
                print("sin",angle,"= ",round(math.sin(rad),2))
                break
            elif ch==2:
                print("cos",angle,"= ",round(math.cos(rad),2))
                break
            elif ch==3:
                print("tan",angle,"= ",round(math.tan(rad),2)) 
                break
            elif ch==4:
                print("cosec",angle,"= ",round(1/math.sin(rad),2))
                break
            elif ch==5:
                print("sec",angle,"= ",round(1/math.cos(rad),2))
                break
            elif ch==6:
                print("cot",angle,"= ",round(1/math.tan(rad),2))
                break
            else:  
                print("Invalid choice")
        except ValueError:
            print("Please enter an integer")

def arithmetic():
    while(True):
        print("""
=========================================================================
            Arithmetic Functions
=========================================================================
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Power
            6. Back to menu
=========================================================================
        """)
        try:
            ch3=int(input("Enter your Choice: "))
            if ch3 == 1:
                a=float(input("Enter the first number: "))
                b=float(input("Enter the second number: "))
                print(f"{a} + {b} =".format(a,b),a+b)
                break
            elif ch3 == 2:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"{a}- {b} = ".format(a,b),a - b)
                break
            elif ch3 == 3:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"{a} * {b} = ".format(a,b),a * b)
                break
            elif ch3 == 4:
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))
                print(f"{a} / {b} = ".format(a,b),a / b)
                break
            elif ch3 == 5:
                a = float(input("Enter your number: "))
                b = float(input("Enter the power: "))
                print(f"{a} ^ {b} = ".format(a,b),a ** b)
                break
            elif ch3 == 6:
                 break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter an integer")

def decimaltobinary():
    try:
        decimal = int(input("Enter a decimal number: "))
        binary = 0
        count = 0
        temp = decimal
        while(temp > 0):
            binary = ((temp%2)*(10**count)) + binary
            temp = int(temp/2)
            count += 1
        print("Binary of",decimal,"is : ",binary)
    except ValueError:
        print("Please enter an integer")



def calculate_area():
    while True:
        print("""
=========================================================================
            Area Functions
=========================================================================
            1. Rectangle
            2. Triangle
            3. Circle
            4. Back to menu
            
            Note: All values entered will be considered in metres
=========================================================================
        """)
        try:
            ch4=int(input("Enter your choice: "))
            if ch4 == 1:
                l = int(input("Enter rectangle's length: "))
                b = int(input("Enter rectangle's breadth: "))
                rect_area = l * b
                print("The area of rectangle is",rect_area,"m²")
                break
            elif ch4==2:
                h = float(input("Enter triangle's height: "))
                b = float(input("Enter triangle's base: "))        
                tri_area = 0.5 * b * h
                print("The area of the triangle is",tri_area,"m²")
                break
            elif ch4==3:
                r = float(input("Enter circle's radius: ")) 
                circ_area = round(math.pi*(r**2),2)
                print("The area of the circle is",circ_area,"m²")
                break
            elif ch4==5:
                break                       
            else:
                print("Sorry, this shape is not available")
        except ValueError:
            print("Please enter a numeric value.")


def factorial():
    try:
        num=int(input("Enter the number whose factorial is to be calculated: "))
        f=1
        if num>1:
            for i in range(1,num+1):
                f*=i
        print(num,"! = ",f)
    except ValueError:
        print("Please enter an integer.")




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
    print("""
=========================================================================
        Arithmetic Functions
=========================================================================
          1. Add
          2. Subtract
          3. Multiply
          4. Divide
          5. Power
=========================================================================
    """)
    try:
        ch3=int(input("Enter your Choice: "))
        if ch3 == 1:
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print(a+b)
        elif ch3 == 2:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(a - b)
        elif ch3 == 3:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(a * b)
        elif ch3 == 4:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
            print(a / b)
        elif ch3 == 5:
            a = float(input("Enter your number: "))
            b = float(input("Enter the power: "))
            print(a ** b)
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








while True:
    print("1)Addition")
    print("2)Subtraction")
    print("3)Multiplication")
    print("4)Division")
    print("5)Exit")
    n = int(input("Enter your choice from 1-5: "))
    a = int(input("Enter the First Number: "))
    b = int(input("Enter the Second Number: "))

    if n == 1:
         print("Addition is: ",(a+b))
         print()
    elif n == 2:
        print("Subtraction is: ",(a-b))
        print()
    elif n == 3:
        print("Multiplication is: ",(a*b))
        print()
    elif n == 4:
        print("Division is: ",(a/b))
        print()
    elif n == 5:
        print("EXITED FROM CALCULATOR")
        print()
        break
    else:
        print("ENTERED NUMBER IS INVALID")
        print()

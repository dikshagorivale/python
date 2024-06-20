while True:
    print("1)Celcius to Farenheit")
    print("2)Farenheit to Celcius")
    print("3)Exit")

    n = int(input("Enter your choice from 1-5: "))
    temp = float(input("Enter temperature: "))

    if n == 1:
        print("Celcius to Farenheit is: ", ((temp * 9/5) + 32))
        print()
    elif n == 2:
        print('Farenheit to Celcius is: ',((temp - 32) * 5/9))
        print()
    elif n == 3:
        print("EXITED FROM CODE")
        print()
        break
    else:
        print("ENTERED NUMBER IS INVALID")
        print()
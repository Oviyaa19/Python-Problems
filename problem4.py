size = int(input("Enter your size: "))

match size:
    case 29:
        print("Small")
    case 30:
        print("Medium")
    case 38:
        print("Large")
    case 42:
        print("X Large")
    case _:
        print("Invalid size")

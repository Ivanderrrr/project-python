def add(x, y):
    result = x + y
    print(str(x) + "+" + str(y) + "=" + str(result) + "\n")

def sub(x, y):
    result = x - y
    print(str(x) + "-" + str(y) + "=" + str(result) + "\n")

def multi(x, y):
    result = x * y
    print(str(x) + "*" + str(y) + "=" + str(result) + "\n")

def div(x, y):
    result = x / y
    print(str(x) + "/" + str(y) + "=" + str(result) + "\n")
    

while True:
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. divide")
    print("E. exit")
    
    choice = input(("What your chose: "))
    
    if choice == "a" or choice == "A":
        x = int(input("enter the number: "))
        y = int(input("enter the number: "))
        add(x, y)
    elif choice == "b" or choice == "B":
        x = int(input("enter the number: "))
        y = int(input("enter the number: "))
        sub(x, y)
    elif choice == "c" or choice == "C":
        x = int(input("enter the number: "))
        y = int(input("enter the number: "))
        multi(x, y)
    elif choice == "d" or choice == "D":
        x = int(input("enter the number: "))
        y = int(input("enter the number: "))
        div(x, y)
    elif choice == "e" or choice == "E":
        print("Program ended.")
        quit()
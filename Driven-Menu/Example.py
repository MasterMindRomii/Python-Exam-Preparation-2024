def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def exp(x):
    return x * x

def exit_program():
    print("Exiting program")
    exit()

def Display_Menu(Menu):
    print("Menu:")
    for key, value in Menu.items():
        print(key, value.__name__)

def main():
    Menu = {
        1: add,
        2: sub,
        3: mul,
        4: exp,
        5: exit_program
    }
    
    while True:
        Display_Menu(Menu)
        
        try:
            Choice = int(input("Enter Your Choice (1-5): "))
            if Choice in Menu:
                if Choice == 4:
                    num = float(input("Enter a number: "))
                    result = Menu[Choice](num)
                    print(f"Result: {result}")
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    result = Menu[Choice](num1, num2)
                    print(f"Result: {result}")

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Invalid Choice! Please enter a valid number (1-5).")

if __name__ == "__main__":
    main()

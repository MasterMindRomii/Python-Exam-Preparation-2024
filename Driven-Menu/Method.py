def option1():
    print("Option 1 selected")

def option2():
    print("Option 2 selected")

def option3():
    print("Option 3 selected")

def exit_program():
    print("Exiting program")
    exit()

def display_menu(menu):
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value.__name__}")

def main():
    menu = {
        1: option1,
        2: option2,
        3: option3,
        4: exit_program
    }

    while True:
        display_menu(menu)

        try:
            choice = int(input("Enter your choice: "))
            if choice in menu:
                menu[choice]()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

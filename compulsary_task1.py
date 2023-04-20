# Task 10: Compulsory Task 1

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("The operations below are performed by the calculator below: ")
print("1: Add\n")
print("2: Subtract\n")
print("3: Multiply\n")
print("4: Divide\n")

while True:
    # input from the user
    choice = input("Please enter your choice from the menu above (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Please enter your first number: \n"))
            num2 = float(input("Please enter your second number: \n"))
        except ValueError:
            print("Type error. Please enter a valid number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Would you like to do another calculation ? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")


    def write_file(value):

        # Use of exception handling if the file does not exist
        # Prompts the user to write a file name using input
        # Write user data
        # Close file

        text_file = None
        try:
            text_file_write = input(
                "\n\nPlease enter the name of the file you would like to save the calculations to, followed by .txt:\n\n").lower()
            text_file = open(text_file_write, "a+")

            text_file.write(value)

            text_file.close()

        except FileNotFoundError as error:
            print("This file does not exist")
            print(error)

        finally:
            if text_file is not None:
                text_file.close()

        print(f"\n\nThank you, your calculation has been added to {text_file_write}.\n")


    def open_file():

        # Using exception handling if the file does not exist
        # Prompt user to choose file name to open
        # Print data
        # Close file

        text_file = None

        try:
            text_file_name = input(
                "\n\nPlease enter the name of the file you would like to open, followed by .txt:\n\n").lower()

            text_file = open(text_file_name, "r")

            print("The list of the calculations you performed is shown below")

            for lines in text_file:
                print(f'''
                    {lines}''')

            print("\n--------------------------END----------------------------------\n")

            text_file.close()

        except FileNotFoundError as error:
            print("\nThis file does not exist")
            print(error)

        finally:
            if text_file is not None:
                text_file.close()


    # =========================================================MENU=====================================================================#

    # Use a loop to go through menu choices

    while True:
        try:
            input_choice = int(input('''\nPlease select from the following:\n
                                    1. Add\n
                                    2. Subtract\n
                                    3. Multiply\n
                                    4. Divide\n
                                    5. View all calculations\n
                                    6. Quit\n'''))

            # If user selects 1, add num_1 and num_2
            # Print results and call write_file() function

            if input_choice == 1:
                user_num_1 = int(input("\nPlease enter your first number:\n\n"))
                user_num_2 = int(input("\nPlease enter your second number:\n\n"))

                answer = (f"The sum of {user_num_1} and {user_num_2} is {add(user_num_1, user_num_2)}\n")

                print("\n", answer)
                write_file(answer)

            # If user selects 2, subtract num_1 and num_2
            # Print results and call write_file() function

            elif input_choice == 2:
                user_num_1 = int(input("\nPlease enter your first number:\n\n"))
                user_num_2 = int(input("\nPlease enter your second number:\n\n"))

                answer = (f"The subtraction of {user_num_1} and {user_num_2} is {subtract(user_num_1, user_num_2)}\n")

                print("\n", answer)
                write_file(answer)

            # If user selects 3, subtract num_1 and num_2
            # Print results and call write_file() function

            elif input_choice == 3:
                user_num_1 = int(input("\nPlease enter your first number:\n\n"))
                user_num_2 = int(input("\nPlease enter your second number:\n\n"))

                answer = (
                    f"The multiplication of {user_num_1} and {user_num_2} is {multiply(user_num_1, user_num_2)}\n")

                print("\n", answer)
                write_file(answer)

            # If user selects 4, divide num_1 and num_2
            # Use a try except if the user tries to divide by 0
            # Print results and call write_file() function

            elif input_choice == 4:
                while True:
                    try:
                        user_num_1 = int(input("\nPlease enter your first number:\n\n"))
                        user_num_2 = int(input("\nPlease enter your second number:\n\n"))

                        answer = (
                            f"The division of {user_num_1} and {user_num_2} is {divide(user_num_1, user_num_2)}\n")
                        print("\n", answer)
                        write_file(answer)
                        break
                    except:
                        ValueError(print("\nDivision by 0 is not defined. Please select a number greater than 0."))

            # If user selects 5, call open_file() function

            elif input_choice == 5:
                open_file()

            # If user selects 6, break the loop

            elif input_choice == 6:
                print("\nHave a lovely day!\n")
                break

            # If the user selects a number out of range, prompt accordingly

            elif input_choice > 6:
                print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

        # Use a try except ValueError if the user inputs letters instead of numbers

        except ValueError:
            print("\nYou have selected an invalid option. Please try again by entering a number.\n")
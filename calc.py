import time
import os
import webbrowser

# Enable ANSI Escape Codes on Windows
if os.name == 'nt':  # Check if the system is Windows
    os.system('')  # Enables the ANSI escape codes in terminal

# Function to clear the terminal
def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Function to clear the current line
def clear_line():
    """Clears the current line in the terminal."""
    print("\r" + " " * 50 + "\r", end="", flush=True)

# ASCII Art for the Calculator
ascii_art = """
========================================
   ####     ##     ####       ####   ##   ##  ####       ##     ######    #####   ######
  ##  ##   ####     ##       ##  ##  ##   ##   ##       ####    # ## #   ##   ##   ##  ##
 ##       ##  ##    ##      ##       ##   ##   ##      ##  ##     ##     ##   ##   ##  ##
 ##       ##  ##    ##      ##       ##   ##   ##      ##  ##     ##     ##   ##   #####
 ##       ######    ##   #  ##       ##   ##   ##   #  ######     ##     ##   ##   ## ##
  ##  ##  ##  ##    ##  ##   ##  ##  ##   ##   ##  ##  ##  ##     ##     ##   ##   ##  ##
   ####   ##  ##   #######    ####    #####   #######  ##  ##    ####     #####   #### ## by admx

========================================
"""

# Loading Screen Function
def loading_screen():
    print(f"\n{nigga_color}Loading", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
        # Overwrite the loading line with spaces
        clear_line()
        print(f"{nigga_color}Loading", end="", flush=True)
        for i in range(_ + 1):
            print(".", end="", flush=True)
    # Clear the loading line after it finishes
    clear_line()
    print("\n", end="", flush=True)

# Blue Color Code (ANSI Escape)
blue_color = '\033[94m'
nigga_color = '\u001b[31m'
reset_color = '\033[0m'  # Reset color to default

# URL to open when quitting
quit_url = 'https://realadmx.netlify.app'  # Change this to your desired URL

# Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main Function to Display Menu and Get User Input
def calculator():
    clear_terminal()  # Clear terminal before starting

    print(f"{blue_color}{ascii_art}{reset_color}")
    
    # Show loading screen
    loading_screen()

    # Menu options
    menu = f"""
{blue_color}                                     Select an operation:


                                              |
                                              |
                                              |
                                             \|/


                                  [1]  ->Add
                                  [2]  ->Subtract
                                  [3]  ->Multiply
                                  [4]  ->Divide
{reset_color}
    """

    while True:
        print(menu)
        choice = input(f"{blue_color}Enter your choice (1/2/3/4) or 'q' to quit: {reset_color}").strip().lower()
        
        if choice == 'q':
            print(f"{blue_color}Thank you for using the calculator. Goodbye!{reset_color}")
            # Open the web browser
            webbrowser.open(quit_url)
            break  # Exit the while loop and end the program

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input(f"{blue_color}Enter first number: {reset_color}"))
                num2 = float(input(f"{blue_color}Enter second number: {reset_color}"))
            except ValueError:
                print(f"{blue_color}Invalid input. Please enter a valid number.{reset_color}")
                continue

            if choice == '1':
                print(f"\n{blue_color}Result: {num1} + {num2} = {add(num1, num2)}{reset_color}")
            elif choice == '2':
                print(f"\n{blue_color}Result: {num1} - {num2} = {subtract(num1, num2)}{reset_color}")
            elif choice == '3':
                print(f"\n{blue_color}Result: {num1} * {num2} = {multiply(num1, num2)}{reset_color}")
            elif choice == '4':
                print(f"\n{blue_color}Result: {num1} / {num2} = {divide(num1, num2)}{reset_color}")
                
            next_calc = input(f"\n{blue_color}Do you want to perform another calculation? (yes/no): {reset_color}").strip().lower()
            if next_calc == 'no':
                print(f"{blue_color}Thank you for using the calculator. Goodbye!{reset_color}")
                # Open the web browser
                webbrowser.open(quit_url)
                break  # Exit the while loop and end the program
        else:
            print(f"{blue_color}Invalid choice. Please select a valid option.{reset_color}")

# Run the Calculator
calculator()

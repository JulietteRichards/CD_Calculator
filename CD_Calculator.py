#This code was created to calculate the potential earned interest of a CD
#Based off user input of the APY Term Length in Months and Initial Investment
#Created by Juliette Richards 12/02/2024
def cd_calculator():
    # Function to get a float input
    def get_float_input(prompt, error_message):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print(error_message)

    # Get inputs from the user
    apy = get_float_input("Enter the APY as a decimal (e.g., 0.05 for 5%): ", 
                          "Error: Please enter the APY as a decimal number.")
    term_length_months = get_float_input("Enter the term length in months: ", 
                                         "Error: Please enter the term length in months as a number.")
    initial_investment = get_float_input("Enter the initial investment amount: ", 
                                         "Error: Please enter the initial investment as a number.")

    # Calculate RATE and INTEREST EARNED
    rate = apy / 12
    interest_earned = rate * term_length_months * initial_investment

    # Round the result
    interest_earned_rounded = round(interest_earned, 2)

    # Print the rounded interest earned
    print(f"Interest Earned: ${interest_earned_rounded}")

# Call the function to run the calculator
cd_calculator()

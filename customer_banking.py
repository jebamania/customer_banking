# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
# from savings_account import create_savings_account
from cd_account import cd_Account
from savings_account import savings_Account

def checkTypeDigit(in_value):
    if in_value.isdigit():
        return in_value
    else:
        raise Exception('Unable to process based on inputs. Please make sure it is a number.')
        

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    in_balance = checkTypeDigit(input('Enter your savings Balance:\n'))
    savings_balance = float(in_balance)
    
    in_interest = checkTypeDigit(input('Enter your Interest Rate:\n'))
    savings_interest = float(in_interest)
    
    in_maturity = checkTypeDigit(input('Enter your savings Maturity in months:\n'))
    savings_maturity = int(in_maturity)

    my_savings_acct = savings_Account(savings_balance, 0)

    # Call the create_savings_account function and pass the variables from the user.
    # updated_savings_balance, interest_earned = create_savings_account(savings_interest, savings_maturity)
    my_savings_acct.create_savings_account(savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Congratulations! You earned ${my_savings_acct.interest:,.2f} in interest for a new balance of: ${my_savings_acct.balance:,.2f}!!!')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    in_balance = checkTypeDigit(input( 'What is your cd Balance:\n'))
    cd_balance = float(in_balance)
    
    in_interest = checkTypeDigit(input( 'What is your cd Interest:\n'))
    cd_interest = float(in_interest)
    
    in_maturity = checkTypeDigit(input( 'What is your cd Maturity in months:\n'))
    cd_maturity = int(in_maturity)
    
    my_cd_acct = cd_Account(cd_balance, 0)

    # Call the create_cd_account function and pass the variables from the user.
    # updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    my_cd_acct.create_cd_account(cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Congratulations! You earned ${my_cd_acct.interest:,.2f} in interest for a new balance of: ${my_cd_acct.balance:,.2f}!!!')

if __name__ == "__main__":
    # Call the main function.
    main()
from Account import Account
class savings_Account(Account):
        
    """Import the Account class from the Account.py file."""
    # ADD YOUR CODE HERE

    # Define a function for the Savings Account
    def create_savings_account(self, interest_rate, months):
        """Creates a savings account, calculates interest earned, and updates the account balance.

        Args:
            balance (float): The initial savings account balance.
            interest_rate (float): The APR interest rate for the savings account.
            months (int): The length of months to determine the amount of interest.

        Returns:
            float: The updated savings account balance after adding the interest earned.
            And returns the interest earned.
        """

        new_balance = 0

        # Create an instance of the `Account` class and pass in the balance and interest parameters.
        #  Hint: You need to add the interest as a value, i.e, 0.
        # ADD YOUR CODE HERE

        # new_acct = Account(balance, 0)

        # # Calculate interest earned
        
        total_interest_earned = 0

        # # Update the savings account balance by adding the interest earned
        # # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.

        for _ in range(int(months)):
            interest_earned = ((self.balance * interest_rate)/12)
            total_interest_earned += interest_earned
            self.set_balance( self.balance + interest_earned )


        # # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
        # new_acct.set_interest(interest_earned)

        # # Return the updated balance and interest earned.
        # return [new_acct.balance, total_interest_earned]

        # Return the updated balance and interest earned. No longer necessary with inheritance!
        #return [self.balance, total_interest_earned]
    

        #
        ## Trying again with inheritance & list comprehension:
        ## The below formula does not calculate correctly, but I tried!
        #


        # amount of interest earned for each period
        #dec_interest = interest_rate/100
        #int_func = lambda n: self.balance * ( (1+( dec_interest / 12))**n-1)
        
        # specific formula example
        # 100 * ( (1+(.12 / 12))**2-1)
        # formula: P x (1 + r/n)**nt

        # int_over_time = [int_func(x) for x in range(1, 1+months)]
        # print(int_over_time)
        # total_interest_earned = sum(int_over_time)  
            
        # self.set_balance( self.balance + total_interest_earned )
        
        
        # self.set_interest(total_interest_earned)

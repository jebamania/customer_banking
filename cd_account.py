from Account import Account
class cd_Account(Account):

    def __init__(self, balance, interest):
        Account.__init__(self, balance, interest)

    """Import the Account class from the Account.py file."""
    # ADD YOUR CODE HERE
    from Account import Account

    def create_cd_account(self, interest_rate, months):
        """Creates a CD account, calculates interest earned, and updates the account balance.

        Args:
            balance (float): The initial CD account balance.
            interest_rate (float): The APR interest rate for the CD account.
            months (int): The length of months for the CD.

        Returns:
            float: The updated CD account balance after adding the interest earned.
            And returns the interest earned.
        """
        # Create an instance of the `Account` class and pass in the balance and interest parameters.
        #  Hint: You need to add the interest as a value, i.e, 0.
        # ADD YOUR CODE HERE

        # Calculate interest earned
        # ADD YOUR CODE HERE

        # Update the CD account balance by adding the interest earned
        # ADD YOUR CODE HERE

        # Pass the updated_balance to the set balance method using the instance of the CD Account class.
        # ADD YOUR CODE HERE

        # Pass the interest_earned to the set interest method using the instance of the CD Account class.
        # ADD YOUR CODE HERE

        # new_acct = Account(balance, 0)

        # total_interest_earned = 0

        # for _ in range(months):
        #     interest_earned = ((new_acct.balance * interest_rate)/12)
        #     total_interest_earned += interest_earned
        #     new_acct.set_balance( new_acct.balance + interest_earned )

        #new_acct.set_interest(interest_earned)

        # Return the updated balance and interest earned.
        #return [new_acct.balance, total_interest_earned]
    

        ### Try again with class inheritance
        total_interest_earned = 0

        for _ in range(months):
            interest_earned = ((self.balance * (interest_rate/100))/12)
            print(interest_earned)
            total_interest_earned += interest_earned
            self.set_balance( self.balance + interest_earned )

        self.set_interest(total_interest_earned)

        # Return the updated balance and interest earned.
        # return [self.balance, total_interest_earned]

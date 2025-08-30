import sys
import os

os.system('cls')

try:
    print(f'Welcome to Tip calculator')
    bill_amount = float(input('What is the total bill? $ '))
    tip = int(input('How much tip you would like to give? 10, 12 or 15? '))
    num_of_people = int(input('How many peoples splitting the bill? '))

    # calculating the tip
    tip_percent = tip/100
    split_amount = (bill_amount + (bill_amount *tip_percent))/num_of_people
    
    #final amount
    final_amt = round(split_amount,2)
    # final_amt = "{:.2f}".format(split_amount)

    #final print
    print(f'Each person shouuld pay: $ {final_amt}')
    sys.exit(0)

#hanlding exceptions
except Exception as e:
    print(f'An error occurred: {str(e)}')
    sys.exit(1)


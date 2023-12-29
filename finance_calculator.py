#Finance Calculator
'''
Start off by asking the user which calculation they want to do,Investment or bond. 
While neither has been entered, keep on asking until the correct word is entered.
Selected Investment. User input - amount depositing/ interest rate/ number of years/ simple or compound interest.
Output - how much they would make after interest and years for either simple or compound.
'''
'''
Selected bond. User input - present house value/ interest rate/ number of months to repay.
Output - How much the user will have to pay back each month.
'''
import math

#Opening selector screen.
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

#Allows user input.
option = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")

#Check to see if input is valid otherwise repeat until correct.
while option.lower() != "investment" and option.lower() != "bond":
    option = input("Please select either 'investment' or 'bond' from the menu above to proceed: ")
    
                                        #Directing to either investment or bond. 
                                           
if option.lower() == "investment":  #Checks too see if the user selected investment.

    amount = input("Amount Depositing: ")
    while amount.isdigit() != True:                         #Checks to see if the user inputed a number.
        amount = input("Please enter a valid number: ")

    rate = input("Enter interest rate: ")
    while rate.isdigit() != True:
        rate = input("Please enter a valid number: ")

    years = input("How many Years: ")
    while years.isdigit() != True:
        years = input("Please enter a valid number: ")


    interest = input("Would you like simple or compound interest: ")

                                                        #Check to see if input is correct, if not then repeat.
    while interest.lower() != "simple" and interest.lower() != "compound":
        interest = input("Please select simple or compound: ") 

    amount = int(amount)
    rate = int(rate)                                    #Converts the strings to int.
    years = int(years) 
                                                        #Directs to either simple or compound.   
    if interest.lower() == "simple":
        r = rate /100           
        a = amount*(1 + r*years)    
        total = (a - amount) /years     #Equation to work out the simple interest.
        print("\nyour total will be £",int(a), "you will earn £",int(total), "per year")    #Prints the solution for the user to see.

    elif interest.lower() == "compound":
        r = rate /100
        a = amount*math.pow((1 + r),years)
        total = (a - amount) /years     #Equation to work out the compound interest.
        print("\nYour total will be £",int(a) ," and you will earn", int(total), "per year")    #Prints the solution for the user to see.  

# Checks to see if user selected bond
elif option.lower() == "bond": 

    value = input("Current house value: ")
    while value.isdigit() != True:          
        value = input("Please enter a valid number: ")

    rate = input("Interest rate: ")
    while rate.isdigit() != True:
        rate = input("Please enter a valid number: ")

    months = input("How many months to fully repay: ")
    while months.isdigit() != True:
        months = input("Please enter a valid number: ")

    # Converts the strings to int.
    value = int(value)
    rate = int(rate)                               
    months = int(months) 

    i = (rate /100) /12
     # Place the solution to the equation into variable.
    repayment = (i * value)/(1 -(1 + i)**(-months))

     # Prints the solution for the user to see.
    print("\nYou will have to pay £", int(repayment), " per month")    
    
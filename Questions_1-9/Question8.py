'''
Created on Apr 23, 2021

@author: Karthik
'''
def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    #Start writing your code here
    if(account_number//1000!=1):
        print("Invalid account number")
    elif(account_balance<100000):
        print("Insufficient account balance")
    elif(salary<=25000):
        print("Invalid loan type or salary")
    elif(loan_type=="Car"):
        if(salary<25000 or loan_amount_expected>500000 or customer_emi_expected > 36):
            print("The customer is not eligible for the loan")
        else:
            eligible_loan_amount=500000
            bank_emi_expected=36
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)
    elif(loan_type=="House"):
        if(salary<=50000): 
            print("Invalid loan type or salary")
        elif(loan_amount_expected>6000000 or customer_emi_expected > 60):
            print("The customer is not eligible for the loan")
        else:
            eligible_loan_amount=6000000
            bank_emi_expected=60
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)
    elif(loan_type=="Business"):
        if(salary<=75000):
            print("Invalid loan type or salary")
        elif(loan_amount_expected>7500000 or customer_emi_expected > 84):
            print("The customer is not eligible for the loan")
        else:
            eligible_loan_amount=7500000
            bank_emi_expected=84
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)
    else:
        print("Invalid loan type or salary")

#Test your code for different values and observe the results
calculate_loan(1005,20000,255000,"Car",300000,30)
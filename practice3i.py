print("Kindly provide the necessary informationon a rating of 1-10. ")

loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment"))

give_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        give_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            give_loan = True
        else:
            give_loan = False
    else:
        give_loan = False
else:
    if credit_history < 4:
        give_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            give_loan = True
        elif income >= 4 and down_payment >= 4:
            give_loan = True
        else:
            give_loan = False
if give_loan:
    print("The decision is Yes.")
else:
    print("The decision is No")
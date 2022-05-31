def Calculate_Monthly_Payment(amount, annual_rate, number_years):
    '''Take in loan amount, interest rate and loan length and returns the monthly payment.'''
    MIR = annual_rate / 1200
    NP = number_years * 12
    MonthlyPmt = (amount * MIR) / (1 - (1 + MIR) ** -NP)
    return MonthlyPmt

def Calculate_TotalInterest(loan_amount, monthly_payment, number_years):
    '''Take in the loan amount, monthly payment and the loan length and returns the total interest rate'''
    TotalInterest = (monthly_payment * number_years) - loan_amount
    return TotalInterest

def Display_Results(monthly_payment, total_interest, num_years):
    '''prints the result of the monthly payment and the total interest rate'''
    print('Monthly payment: ${:.2f}'.format(monthly_payment)) 
    print('You will pay ${:.2f} in interest over {} years.'.format(total_interest, num_years))

a = int(input('Enter loan amount: '))
r = float(input('Enter annual interest rate (ex. 7.625): '))
y = int(input('Enter loan length (in years): '))

monthly_payment = Calculate_Monthly_Payment(a, r, y)
interest = Calculate_TotalInterest(a, monthly_payment, y)

Display_Results(monthly_payment, interest, y)

import math

loanamount = int(input("Enter loan amount: "))
interest = float(input("Enter annual interest rate (ex. 7.625): "))
loanlength = int(input("Enter loan length (in years): "))

MIR = interest / 1200
NP = loanlength * 12

monthly = (loanamount * MIR) / (1 - (1 + MIR) ** -NP)
TotalInterest = (monthly * NP) - loanamount

print("Monthly payment:", "{:.2f}".format(monthly))
print("You will pay", "{:.2f}".format(TotalInterest), "in interest over", loanlength, "years.")
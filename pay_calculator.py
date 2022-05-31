import math

name = input('Enter Employee Name: ')
worked_hours = int(input('Enter Number of Hours Worked: '))
pay_rate = float(input('Enter Hourly Pay Rate (ex. 20.00): '))
overtime_eligiblitiy = input('Eligible for Overtime Pay (yes or no): ')

gross_pay = 0
net_pay = 0
tax_amount = 0
ot_pay = 0

if overtime_eligiblitiy == 'yes':
    if worked_hours > 40:
        excess_hours = worked_hours - 40
        ot_pay = excess_hours * (pay_rate * 1.5)
        standard_pay = worked_hours - excess_hours
        gross_pay = standard_pay * pay_rate + ot_pay
else:
    gross_pay = worked_hours * pay_rate

if gross_pay < 250:
    tax_amount = gross_pay * 0.15
elif gross_pay < 480:
    tax_amount = gross_pay * 0.18
elif gross_pay < 720:
    tax_amount = gross_pay * 0.21
elif gross_pay >= 720:
    tax_amount = gross_pay * 0.25

net_pay = gross_pay - tax_amount

print('Pay Information for', name)
print('Hours Worked:', worked_hours)
print('Hourly Rate: {:.2f}'.format(pay_rate))
print('Eligible for OT Pay:', overtime_eligiblitiy)
print('Gross Pay: {:.2f}'.format(gross_pay))
print('Tax Amount: {:.2f}'.format(tax_amount))
print('Net Pay: {:.2f}'.format(net_pay))
import math

celcius_input = int(input("Enter a temperature in celcius: "))
fconversion = 9 / 5 * celcius_input + 32

print(celcius_input, 'converted to fahrenheit is', "{:.2f}".format(fconversion))
print()

f_input = int(input("Enter a temperature in fahrenheit: "))
cconversion = 5 / 9 * (f_input - 32)

print(f_input, 'converted to celcius is', "{:.2f}".format(cconversion))
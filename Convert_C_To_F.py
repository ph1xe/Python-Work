def Convert_C_To_F(celcius):
    fah_temp = (celcius * 9/5) + 32
    return fah_temp

c_input = float(input('Input temperature in celcius to convert to fahrenheit: '))

fah =  Convert_C_To_F(c_input)

print(str(fah), 'degrees fahrenheit.')
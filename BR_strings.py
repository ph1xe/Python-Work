first_name = 'Benjamin'
middle_initial = "L"
last_name = "Reese"

print(first_name + '\n' + last_name)
print(first_name.casefold())
print(last_name.upper())
print(first_name[:1])
print(first_name.count("a"))

full_name = str(first_name) + ' ' + str(middle_initial) + '. ' + str(last_name)

print(full_name)
print(len(full_name))

secure_name = ''
for letter in full_name:
    if letter in 'aeiou':
        secure_name += letter.upper() 
    elif letter == 's':

        secure_name += "$"
    elif letter == "o":
        secure_name += '0'
    else:
        secure_name += letter.lower()
print(secure_name)


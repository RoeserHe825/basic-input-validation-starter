# basic-input-validation-starter
# Henry, PJ
# 12/10/24
# Level 2: Checking for a Numeric Input with Length Validation
stop = True
while stop:
    digit = input('Please enter a number: ')
    len_character = len(digit)
    if len_character > 4 and digit.isdigit():
        print(f'Valid numeric input with enough length: {digit}')
        stop = False
    else:
        print('Input must be a number')
        print('Input must be at least 5 characters long.')
def roman_to_decimal(roman_number):
    decimal_number = 0
    for letter in roman_number :
        if letter == 'I' :
           decimal_number += 1
        if letter == 'V' :
           decimal_number += 5
        if letter == 'X' :
           decimal_number += 10
    return decimal_number
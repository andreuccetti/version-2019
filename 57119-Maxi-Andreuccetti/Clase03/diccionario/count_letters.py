def count_letters(n):
    dict_mio = {}

    for letter in n :
        if  letter in dict_mio :
            dict_mio[letter] += 1
        else :
            dict_mio[letter] = 1

    return dict_mio  
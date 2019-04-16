def pipe_fix(lista):
    mayor = max(lista)
    menor = min(lista)
    new_value = []
    new_value.append(menor)
    while menor < mayor:
        menor += 1
        new_value.append(menor)
    return new_value 
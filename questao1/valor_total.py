def calcular_total(compras):
    total = 0
    for item in compras:
        total += item[2]
    return total


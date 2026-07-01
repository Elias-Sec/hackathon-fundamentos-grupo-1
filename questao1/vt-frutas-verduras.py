def calcular_frutas_verduras(compras):
    total = 0
    for item in compras:
        if item[1] == 'fruta'or item[1] == 'verdura':
            total += item[2]
    return total
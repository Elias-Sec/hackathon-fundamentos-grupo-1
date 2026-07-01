def calcular_desconto(total_bruto, valor_pago):
    if total_bruto == 0:
        return 0.0
    percentual = ((total_bruto - valor_pago) / total_bruto) * 100
    return percentual
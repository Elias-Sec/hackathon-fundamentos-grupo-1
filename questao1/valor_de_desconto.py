def calcular_desconto(cliente_fidelidade, idade_cliente, total_frutas_verduras):
    desconto = 0
    if idade_cliente > 60:
        desconto += 10
    if cliente_fidelidade:
        desconto += 5
    if total_frutas_verduras > 30.00:
        desconto += 5
    if desconto > 20:
        desconto = 20
    
    return desconto
if __name__ == "__main__":
    # Exemplo de uso da função
    cliente_fidelidade = True  # ou False
    idade_cliente = 65
    total_frutas_verduras = 35.00

    desconto_calculado = calcular_desconto(cliente_fidelidade, idade_cliente, total_frutas_verduras)
    print(f"Desconto calculado: {desconto_calculado}%")
    
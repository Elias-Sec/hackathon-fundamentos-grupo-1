def exibir_resumo(compras, cliente_fidelidade, idade_cliente):
    if not compras:
        print("Nenhuma compra foi registrada.")
        return
    
    valor_original = calcular_total(compras)
    valor_hortifruti = calcular_frutas_verduras(compras)
    percentual_desconto = calcular_desconto(cliente_fidelidade, idade_cliente, valor_hortifruti)

    valor_desconto = valor_original * (percentual_desconto / 100)
    valor_final = valor_original - valor_desconto

    print("======= Resumo da Compra =======")
    print(f"Valor Original: R$ {valor_original:.2f}")
    print(f"Valor Hortifruti: R$ {valor_hortifruti:.2f}")
    print(f"Percentual de Desconto: {percentual_desconto:.2f}%")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor Final: R$ {valor_final:.2f}")

if __name__ == "__main__":
    # Exemplo de uso da função
    compras = [
        ("Maçã", "fruta", 5.00),
        ("Alface", "verdura", 3.50),
        ("Arroz", "mercado", 10.00)
    ]
    cliente_fidelidade = True
    idade_cliente = 65

    exibir_resumo(compras, cliente_fidelidade, idade_cliente)
def calcular_total(compras):
    total = 0
    for item in compras:
        total += item[2]
    return total
if __name__ == "__main__":
    # Exemplo de uso da função
    compras = [
        ("Maçã", "fruta", 5.00),
        ("Alface", "verdura", 3.50),
        ("Arroz", "mercado", 10.00)
    ]
    total_calculado = calcular_total(compras)
    print(f"Total calculado: R$ {total_calculado:.2f}")

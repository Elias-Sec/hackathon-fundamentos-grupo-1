def calcular_frutas_verduras(compras):
    total = 0
    for item in compras:
        if item[1] == 'fruta'or item[1] == 'verdura':
            total += item[2]
    return total
if __name__ == "__main__":
    # Exemplo de uso da função
    compras = [
        ("Maçã", "fruta", 5.00),
        ("Alface", "verdura", 3.50),
        ("Arroz", "mercado", 10.00)
    ]
    total_frutas_verduras = calcular_frutas_verduras(compras)
    print(f"Total de frutas e verduras: R$ {total_frutas_verduras:.2f}")    
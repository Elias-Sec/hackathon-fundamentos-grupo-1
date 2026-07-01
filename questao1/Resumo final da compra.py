def exibir_resumo(carrinho, total_bruto, total_descontado, percentual_desc):
    print("\n" + "="*40)
    print("RESUMO FINAL DA COMPRA")
    print("="*40)
    print(f"{'Item':<15} | {'Preço':<8} | {'Qtd':<4}")
    print("-" * 40)
    for item in carrinho:
        nome, preco, quantidade, categoria = item
        print(f"{nome:<15} | R$ {preco:<6.2f} | {quantidade:<4}")
    
    print("="*40)
    print(f"Total Bruto:R$ {total_bruto:.2f}")
    print(f"Total com Desconto:R$ {total_descontado:.2f}")
    print(f"Desconto Aplicado:{percentual_desc:.1f}%")
    print("="*40)

import resumo_final_da_compra as resumo
import valor_total as total
import vt_frutas_verduras as frutas_verduras
import valor_de_desconto as desconto


print("=== CADASTRO DO CLIENTE ===")
idade_cliente = int(input("Digite a idade do cliente: "))

fidelidade_input = input("O cliente é participante do programa de fidelidade? (s/n): ").strip().lower()
cliente_fidelidade = True if fidelidade_input == 's' else False

compras = []
print("\n=== REGISTRO DE PRODUTOS ===")
print("Instruções: Cadastre os produtos um a um. Digite 'sair' no nome do produto para encerrar.\n")

while True:
    nome_produto = input("Nome do produto (digite 'sair' para encerrar ): ").strip()
    
    
    if nome_produto.lower() == 'sair':
        break
        
    categoria = input("Categoria (fruta / verdura / mercado / limpeza): ").strip().lower()
    valor = float(input("Valor do produto: R$ "))
    
    
    compras.append((nome_produto, categoria, valor))
    print(f"-> {nome_produto} adicionado com sucesso!\n")


print(resumo.exibir_resumo(compras, cliente_fidelidade, idade_cliente))
print(total.calcular_total(compras))
print(frutas_verduras.calcular_frutas_verduras(compras))
print(desconto.calcular_desconto(cliente_fidelidade, idade_cliente, frutas_verduras.calcular_frutas_verduras(compras))) 
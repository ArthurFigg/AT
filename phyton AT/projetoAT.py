estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"



produtos = []
for prod in estoque_inicial.split("#"):
    a = prod.split(";")
    produto_dict = {
        "nome": a[0],
        "codigo": int(a[1]),
        "quantidade": int(a[2]),
        "custo": float(a[3]),
        "precoVenda": float(a[4])
    }
    produtos.append(produto_dict)





def mostraItens(estoque): 
    print("\nNome".ljust(30), "Código".rjust(10), "Quant.".rjust(10), "Custo".rjust(10), "Preço Venda".rjust(15))
    for p in estoque:
        print(p["nome"].ljust(30), str(p["codigo"]).rjust(10), str(p["quantidade"]).rjust(10), 
              f'{p["custo"]:.2f}'.rjust(10), f'{p["precoVenda"]:.2f}'.rjust(15))
        






def adicionaProduto(estoque):
    codigo = int(input("Código do produto: "))
    

    for p in estoque:
        if p['codigo'] == codigo:
            print("Produto com esse código já existe.")
            return

 
    novo_produto = {
        "nome": input("Nome: "),
        "codigo": codigo,
        "quantidade": int(input("Quant.: ")),
        "custo": float(input("Custo: ")),
        "precoVenda": float(input("Preço Venda: "))
    }

    estoque.append(novo_produto)
    print(f'Produto "{novo_produto["nome"]}" adicionado com sucesso!')






def achaProduto(estoque): 
    achei = input("Nome ou Código: ").lower()
    encontrados = [p for p in estoque if achei in p['nome'].lower() or str(p['codigo']) == achei]
    if encontrados:
        mostraItens(encontrados)
    else:
        print("Nenhum produto encontrado.")






def excluirP(estoque):
    byebye = input("Digite o nome ou código do produto que deseja remover: ").lower()
    produtos_a_remover = [p for p in estoque if byebye in p['nome'].lower() or str(p['codigo']) == byebye]

    if produtos_a_remover:
        for produto in produtos_a_remover:
            estoque.remove(produto)
            print(f'Produto "{produto["nome"]}" (Código {produto["codigo"]}) removido com sucesso!')
    else:
        print(f"Nenhum produto encontrado com o termo '{termo}'.")






def ordenaProduto(estoque, ordemCrescente=True): 
    estoque.sort(key=lambda p: p['quantidade'], reverse=not ordemCrescente)
    mostraItens(estoque)






def editarProduto(estoque, campo):
    codigo = int(input("Código do produto a ser editado: "))
    for p in estoque:
        if p['codigo'] == codigo:
            if campo == "precoVenda":
                p[campo] = float(input(f"Novo {campo}: "))
            elif campo == "quantidade":
                p[campo] = int(input(f"Nova quantidade: "))
            print(f"Produto {p['nome']} atualizado com sucesso!")
            return
    print("Produto não encontrado.")






def valorTotal(estoque): 
    valor_total = sum(p['quantidade'] * p['precoVenda'] for p in estoque)
    lucro_total = sum((p['precoVenda'] - p['custo']) * p['quantidade'] for p in estoque)
    print("Valor total do estoque:", valor_total)
    print("Lucro presumido:", lucro_total)






def relatorio(estoque):
    print("\nRelatório do Estoque:")
    mostraItens(estoque)  
    valorTotal(estoque)   






def menu():
    while True:
        print("\n1.Listar")
        print("2.Cadastrar")
        print("3.Buscar")
        print("4.Remover")
        print("5.Ordenar")
        print("6.Esgotados")
        print("7.Baixa Quantidade")
        print("8.Atualizar Quantidade")
        print("9.Atualizar Preço")
        print("10.Valor Total")
        print("11.Relatório")
        print("12.Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            mostraItens(produtos)
        elif opcao == "2":
            adicionaProduto(produtos)
        elif opcao == "3":
            achaProduto(produtos)
        elif opcao == "4":
            excluirP(produtos)
        elif opcao == "5":
            ordenaProduto(produtos)
        elif opcao == "6":
            mostraItens([p for p in produtos if p['quantidade'] == 0])
        elif opcao == "7":
            limite = int(input("Limite: "))
            mostraItens([p for p in produtos if p['quantidade'] < limite])
        elif opcao == "8":
            editarProduto(produtos, "quantidade")
        elif opcao == "9":
            editarProduto(produtos, "precoVenda")
        elif opcao == "10":
            valorTotal(produtos)
        elif opcao == "11":
            relatorio(produtos)
        elif opcao == "12":
            break
        else:
            print("Opção inválida.")

# Inicia o menu
menu()

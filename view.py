import os.path
import controller


def criar_arquivo(*nomes):
    for nome in nomes:
      if not os.path.exists(f'arquivos/{nome}'):
        with open(f'arquivos/{nome}', 'w') as arq:
          arq.write('')

criar_arquivo('categoria.txt', 'cliente.txt', 'estoque.txt', 'fornecedor.txt', 'funcionarios.txt', 'vendas.txt')

os.system('cls')
while True:
  # os.system('cls')
  opcao = input('---------------------------\n'
                'ESCOLHA A OPÇÃO QUE DESEJA:\n'
                '---------------------------\n'
                '1- VENDAS\n'
                '2- CATEGORIAS\n'
                '3- PRODUTOS\n'
                '4- FORNECEDORES\n'
                '5- CLIENTES\n'
                '6- FUNCIONÁRIOS\n'
                '7- ESTOQUE\n'
                '8- RELATÓRIOS\n'
                '0- SAIR\n'
                '---------------------------\n'
                'OPÇÃO: ')
  os.system('cls')

  # SAIR:
  if opcao == '0':
    os.system('cls')
    print('PROGRAMA FINALIZADO!\n\n')
    break

  # CAIXA
  elif opcao == '1':
    pass

  # CATEGORIA:
  elif opcao == '2':
    while True:
      opcao = input('CATEGORIAS\n'
                    '------------------------------\n'
                    '1- CADASTRAR CATEGORIA\n'
                    '2- ALTERAR CATEGORIA\n'
                    '3- EXCLUIR CATEGORIA\n'
                    '4- VER CATEGORIAS\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      ctrl_cat = controller.ControllerCategoria()
      # voltar
      if opcao == '0':
        os.system('cls')
        break
      # cadastrar
      elif opcao == '1':
        ctrl_cat.cadastrar_categoria()
      # alterar
      elif opcao == '2':
        ctrl_cat.alterar_categoria()
      # excluir
      elif opcao == '3':
        ctrl_cat.excluir_categoria()
      # exibir
      elif opcao == '4':
        ctrl_cat.ver_categorias()
      # opção inválida
      else:
        os.system('cls')
        print('→ OPÇÃO INVÁLIDA:\n')



  # PRODUTO:
  elif opcao == '3':
    while True:
      opcao = input('PRODUTO:\n'
                    '------------------------------\n'
                    '1- CADASTRAR PRODUTO\n'
                    '2- ALTERAR PRODUTO\n'
                    '3- EXCLUIR PRODUTO\n'
                    '4- ADICIONAR AO ESTOQUE\n'
                    '5- VER ESTOQUE\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      ctrl_prod = controller.ControllerProduto()
      # voltar
      if opcao == '0':
        os.system('cls')
        break
      # cadastrar
      elif opcao == '1':
        ctrl_prod.cadastrar_produto()
      # alterar
      elif opcao == '2':
        ctrl_prod.alterar_produto()
        pass
      # excluir
      elif opcao == '3':
        #ctrl_prod.excluir_produto()
        pass
      # adicionar no estoque
      elif opcao == '4':
        ctrl_prod.add_estoque()
      # exibir
      elif opcao == '5':
        ctrl_prod.ver_estoque()
      # opção inválida
      else:
        os.system('cls')
        print('→ OPÇÃO INVÁLIDA:\n')


  # FORNECEDOR:
  elif opcao == '4':
    pass

  # CLIENTE:
  elif opcao == '5':
    pass

  # FUNCIONARIO:
  elif opcao == '6':
    pass

  # ESTOQUE:
  elif opcao == '7':
    pass

  # RELATÓRIOS:
  elif opcao == '8':
    pass

  # OPÇÃO INVÁLIDA:
  else:
    os.system('cls')
    print('→ OPÇÃO INVÁLIDA:\n')
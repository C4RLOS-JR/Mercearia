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
                'Escolha a opção que deseja:\n'
                '---------------------------\n'
                '1- Caixa\n'
                '2- Categoria\n'
                '3- Produto\n'
                '4- Fornecedor\n'
                '5- Cliente\n'
                '6- Funcionário\n'
                '7- Estoque\n'
                '8- Relatórios\n'
                '0- Sair\n'
                '---------------------------\n'
                'Opção: ')
  os.system('cls')

  # SAIR:
  if opcao == '0':
    os.system('cls')
    print('Programa finalizado!\n\n')
    break

  # CAIXA
  elif opcao == '1':
    pass

  # CATEGORIA:
  elif opcao == '2':
    while True:
      opcao = input('CATEGORIA:\n'
                    '------------------------------\n'
                    '1- Cadastrar Categoria\n'
                    '2- Alterar Categoria\n'
                    '3- Excluir Categoria\n'
                    '4- Mostrar Categoria\n'
                    '0- Voltar\n'
                    '------------------------------\n'
                    'Opção: ')
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
        print('→ Opção Inválida:\n')



  # PRODUTO:
  elif opcao == '3':
    while True:
      opcao = input('PRODUTO:\n'
                    '------------------------------\n'
                    '1- Cadastrar Produto\n'
                    '2- Alterar Produto\n'
                    '3- Excluir Produto\n'
                    '4- Mostrar Estoque\n'
                    '0- Voltar\n'
                    '------------------------------\n'
                    'Opção: ')
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
        #ctrl_prod.alterar_produto()
        pass
      # excluir
      elif opcao == '3':
        #ctrl_prod.excluir_produto()
        pass
      # exibir
      elif opcao == '4':
        #ctrl_prod.ver_estoque()
        pass
      # opção inválida
      else:
        os.system('cls')
        print('→ Opção Inválida:\n')


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
    print('→ Opção Inválida:\n')
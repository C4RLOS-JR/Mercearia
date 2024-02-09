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
    print('Programa finalizado!\n')
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
                    '3- Remover Categoria\n'
                    '4- Mostrar Categoria\n'
                    '0- Voltar\n'
                    '---------------------------\n'
                    'Opção: ')
      ctrl_cat = controller.ControllerCategoria()

      if opcao == '0':  # voltar
        os.system('cls')
        break
      elif opcao == '1':  # cadastrar
        os.system('cls')
        categoria = input('Digite o nome da categoria: ')
        ctrl_cat.cadastrar_categoria(categoria)
      elif opcao == '2':  # alterar
        os.system('cls')
        categoria_excluir = input('Qual categoria você deseja alterar?\n\nCategoria: ')
        os.system('cls')
        categoria_add = input('Insira uma nova categoria:\n\nCategoria: ')
        ctrl_cat.alterar_categoria(categoria_excluir, categoria_add)  
      elif opcao == '3':  # remover
        os.system('cls')
        categoria = input('Qual categoria você deseja remover?\n\nCategoria: ')
        ctrl_cat.excluir_categoria(categoria)
      elif opcao == '4':  # exibir
        os.system('cls')
        print('Lista de categorias:\n')
        ctrl_cat.ver()
        input('\nPressione "enter" para voltar para o menu...')
        os.system('cls')
      else:
        os.system('cls')
        print('→ Opção Inválida:\n')

  # PRODUTO:
  elif opcao == '3':
    pass

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
import os.path
import controller, dao


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
                '9- Sair\n\n'
                'Opção: ')

  if opcao == '9':
    os.system('cls')
    print('Programa finalizado!\n')
    break

  elif opcao == '1':
    pass
  
  elif opcao == '2':
    os.system('cls')
    opcao = input('CATEGORIA:\n'
                  '------------------------------\n'
                  '1- Cadastrar Categoria\n'
                  '2- Alterar Categoria\n'
                  '3- Remover Categoria\n'
                  '4- Mostrar Categoria\n'
                  '5- Voltar\n\n'
                  'Opção: ')
    cat = controller.ControllerCategoria()

    if opcao == '1':
      os.system('cls')
      categoria = input('Digite o nome da categoria: ')
      cat.cadastrar(categoria)
    elif opcao == '2':
      os.system('cls')
      pass
    elif opcao == '3':
      os.system('cls')
      pass
    elif opcao == '4':
      os.system('cls')
      print('Lista de categorias:\n')
      cat.ver()
      input('\nPressione "enter" para voltar para o menu...')
      os.system('cls')
    elif opcao == '5':
      os.system('cls')
      pass
    else:
      os.system('cls')
      print('Opção Inválida:\n')
      input('Pressione "enter" para voltar para o menu...')

  elif opcao == '3':
    pass
  elif opcao == '4':
    pass
  elif opcao == '5':
    pass
  elif opcao == '6':
    pass
  elif opcao == '7':
    pass
  elif opcao == '8':
    pass
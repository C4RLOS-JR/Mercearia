import os.path
import controller
from termcolor import cprint


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

  # CAIXA Fazer 
  elif opcao == '1':
    pass

  # CATEGORIA:
  elif opcao == '2':
    while True:
      opcao = input('------------------------------\n'
                    'CATEGORIAS\n'
                    '------------------------------\n'
                    '1- CADASTRAR CATEGORIA\n'
                    '2- ALTERAR CATEGORIA\n'
                    '3- EXCLUIR CATEGORIA\n'
                    '4- VER CATEGORIAS\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      os.system('cls')
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
        cprint('→ OPÇÃO INVÁLIDA...', color='red')

  # PRODUTO:
  elif opcao == '3':
    while True:
      opcao = input('------------------------------\n'
                    'PRODUTO:\n'
                    '------------------------------\n'
                    '1- CADASTRAR PRODUTO\n'
                    '2- ALTERAR PRODUTO\n'
                    '3- EXCLUIR PRODUTO\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      os.system('cls')
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
        while True:
          opcao = input('------------------------------\n'
                        'ALTERAR PRODUTO:\n'
                        '------------------------------\n'
                        '1- ALTERAR NOME DO PRODUTO\n'
                        '2- ALTERAR PREÇO DO PRODUTO\n'
                        '3- ALTERAR CATEGORIA DO PRODUTO\n'
                        '0- VOLTAR\n'
                        '------------------------------\n'
                        'OPÇÃO: ')
          os.system('cls')
          # voltar
          if opcao == '0':
            os.system('cls')
            break
          # alterar o produto
          elif opcao == '1' or opcao == '2' or opcao == '3':
            ctrl_prod.alterar_produto(opcao)
          # opção inválida
          else:
            os.system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='red')
      # excluir
      elif opcao == '3':
        ctrl_prod.excluir_produto()
      # opção inválida
      else:
        os.system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='red')

  # FORNECEDOR:
  elif opcao == '4':
    while True:
          opcao = input('------------------------------\n'
                        'FORNECEDOR:\n'
                        '------------------------------\n'
                        '1- CADASTRAR FORNECEDOR\n'
                        '2- ALTERAR FORNECEDOR\n'
                        '3- EXCLUIR FORNECEDOR\n'
                        '4- VER FORNECEDORES\n'
                        '0- VOLTAR\n'
                        '------------------------------\n'
                        'OPÇÃO: ')
          os.system('cls')
          ctrl_fornec = controller.ControllerFornecedor()
          # voltar
          if opcao == '0':
            os.system('cls')
            break
          # cadastrar fornecedor
          elif opcao == '1':
            ctrl_fornec.cadastrar_fornecedor()
          # alterar fornecedor
          elif opcao == '2':
            while True:
              opcao = input('------------------------------\n'
                          'ALTERAR FORNECEDOR:\n'
                          '------------------------------\n'
                          '1- ALTERAR NOME\n'
                          '2- ALTERAR CNPJ\n'
                          '3- ALTERAR TELEFONE\n'
                          '0- VOLTAR\n'
                          '------------------------------\n'
                          'OPÇÃO: ')
              os.system('cls')
               # voltar
              if opcao == '0':
                os.system('cls')
                break
              # alterar o fornecedor
              elif opcao == '1' or opcao == '2' or opcao == '3':
                ctrl_fornec.alterar_fornecedor(opcao)
              # opção inválida
              else:
                os.system('cls')
                cprint('→ OPÇÃO INVÁLIDA...', color='red')
          # excluir fornecedor
          elif opcao == '3':
            ctrl_fornec.excluir_fornecedor()
          # ver fornecedor
          elif opcao == '4':
            ctrl_fornec.ver_fornecedores()
          # opção inválida
          else:
            os.system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='red')

  # CLIENTE:
  elif opcao == '5':
    while True:
      opcao = input('------------------------------\n'
                    'CLIENTE:\n'
                    '------------------------------\n'
                    '1- CADASTRAR CLIENTE\n'
                    '2- ALTERAR CLIENTE\n'
                    '3- EXCLUIR CLIENTE\n'
                    '4- VER CLIENTE\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      os.system('cls')
      ctrl_cliente = controller.ControllerCliente()
      # voltar
      if opcao == '0':
        os.system('cls')
        break
      # cadastrar cliente
      elif opcao == '1':
        ctrl_cliente.cadastrar_cliente()
      # alterar cliente
      elif opcao == '2':
        while True:
          opcao = input('------------------------------\n'
                      'ALTERAR CLIENTE:\n'
                      '------------------------------\n'
                      '1- ALTERAR NOME\n'
                      '2- ALTERAR TELEFONE\n'
                      '3- ALTERAR CPF\n'
                      '4- ALTERAR EMAIL\n'
                      '5- ALTERAR ENDEREÇO\n'
                      '0- VOLTAR\n'
                      '------------------------------\n'
                      'OPÇÃO: ')
          os.system('cls')
            # voltar
          if opcao == '0':
            os.system('cls')
            break
          # alterar o cliente
          elif opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5':
            ctrl_cliente.alterar_cliente(opcao)
          # opção inválida
          else:
            os.system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='red')
      # excluir cliente
      elif opcao == '3':
        ctrl_cliente.excluir_cliente()
        pass
      # ver clientes
      elif opcao == '4':
        ctrl_cliente.ver_clientes()
      # opção inválida
      else:
        os.system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='red')




  # FUNCIONARIO: Fazer 
  elif opcao == '6':
    while True:
      opcao = input('------------------------------\n'
                    'CLIENTE:\n'
                    '------------------------------\n'
                    '1- CADASTRAR FUNCIONÁRIO\n'
                    '2- ALTERAR FUNCIONÁRIO\n'
                    '3- EXCLUIR FUNCIONÁRIO\n'
                    '4- VER FUNCIONÁRIOS\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      os.system('cls')
      ctrl_func = controller.ControllerFuncionario()
      # voltar
      if opcao == '0':
        os.system('cls')
        break
      # cadastrar funcinario
      elif opcao == '1':
        ctrl_func.cadastrar_funcionario()
      # alterar funcinario
      elif opcao == '2':
        while True:
          opcao = input('------------------------------\n'
                      'ALTERAR FUNCIONÁRIO:\n'
                      '------------------------------\n'
                      '1- ALTERAR NOME\n'
                      '2- ALTERAR ID'
                      '3- ALTERAR TELEFONE\n'
                      '4- ALTERAR CPF\n'
                      '5- ALTERAR EMAIL\n'
                      '6- ALTERAR ENDEREÇO\n'
                      '0- VOLTAR\n'
                      '------------------------------\n'
                      'OPÇÃO: ')
          os.system('cls')
            # voltar
          if opcao == '0':
            os.system('cls')
            break
          # alterar o funcinario
          elif opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5' or opcao == '6':
            ctrl_func.alterar_funcinario(opcao)
            pass
          # opção inválida
          else:
            os.system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='red')
      # excluir funcinario
      elif opcao == '3':
        ctrl_func.excluir_funcinario()
        pass
      # ver funcinario
      elif opcao == '4':
        ctrl_func.ver_funcionarios()
      # opção inválida
      else:
        os.system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='red')






  # ESTOQUE:
  elif opcao == '7':
    while True:
      opcao = input('------------------------------\n'
                    'ESTOQUE\n'
                    '------------------------------\n'
                    '1- ADICIONAR AO ESTOQUE\n'
                    '2- VER ESTOQUE\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      os.system('cls')
      ctrl_prod = controller.ControllerEstoque()
      # voltar
      if opcao == '0':
        os.system('cls')
        break
      # adicionar no estoque
      elif opcao == '1':
        ctrl_prod.add_estoque()
      # exibir
      elif opcao == '2':
        ctrl_prod.ver_estoque()
      # opção inválida
      else:
        os.system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='red')

  # RELATÓRIOS: Fazer 
  elif opcao == '8':
    pass

  # OPÇÃO INVÁLIDA:
  else:
    os.system('cls')
    cprint('→ OPÇÃO INVÁLIDA...', color='red')
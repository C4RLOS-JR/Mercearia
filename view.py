import os
import controller
from os import system
from termcolor import cprint


slogan = lambda: cprint(f'{"MERCEARIA PYTHONFULL":^30}', color='light_blue')
def criar_arquivo(*nomes):
    for nome in nomes:
      if not os.path.exists(f'arquivos/{nome}'):
        with open(f'arquivos/{nome}', 'w') as arq:
          arq.write('')

criar_arquivo('categoria.txt', 'cliente.txt', 'estoque.txt', 'fornecedor.txt', 'funcionarios.txt', 'vendas.txt')

system('cls')
while True:
  slogan()
  opcao = input('------------------------------\n'
                'ESCOLHA A OPÇÃO QUE DESEJA:\n'
                '------------------------------\n'
                '1- VENDAS\n'
                '2- CATEGORIAS\n'
                '3- PRODUTOS\n'
                '4- FORNECEDORES\n'
                '5- CLIENTES\n'
                '6- FUNCIONÁRIOS\n'
                '7- ESTOQUE\n'
                '8- RELATÓRIOS\n'
                '0- SAIR\n'
                '------------------------------\n'
                'OPÇÃO: ')
  system('cls')

  # VENDAS
  if opcao == '1':
    vnds_cat = controller.ControllerVendas()
    vnds_cat.vender()

  # CATEGORIA:
  elif opcao == '2':
    while True:
      slogan()
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
      system('cls')
      ctrl_cat = controller.ControllerCategoria()
      if opcao == '1':
        ctrl_cat.cadastrar_categoria()
      elif opcao == '2':
        ctrl_cat.alterar_categoria()
      elif opcao == '3':
        ctrl_cat.excluir_categoria()
      elif opcao == '4':
        ctrl_cat.ver_categorias()
      elif opcao == '0':
        system('cls')
        break
      else:
        system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

  # PRODUTO:
  elif opcao == '3':
    while True:
      slogan()
      opcao = input('------------------------------\n'
                    'PRODUTO:\n'
                    '------------------------------\n'
                    '1- CADASTRAR PRODUTO\n'
                    '2- ALTERAR PRODUTO\n'
                    '3- EXCLUIR PRODUTO\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      system('cls')
      ctrl_prod = controller.ControllerProduto()
      if opcao == '1':
        ctrl_prod.cadastrar_produto()
      elif opcao == '2':
        while True:
          slogan()
          opcao = input('------------------------------\n'
                        'ALTERAR PRODUTO:\n'
                        '------------------------------\n'
                        '1- ALTERAR NOME DO PRODUTO\n'
                        '2- ALTERAR PREÇO DO PRODUTO\n'
                        '3- ALTERAR CATEGORIA DO PRODUTO\n'
                        '0- VOLTAR\n'
                        '------------------------------\n'
                        'OPÇÃO: ')
          system('cls')
          if opcao == '1' or opcao == '2' or opcao == '3':
            ctrl_prod.alterar_produto(opcao)
          elif opcao == '0':
            system('cls')
            break
          else:
            system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='light_red')
      elif opcao == '3':
        ctrl_prod.excluir_produto()
      elif opcao == '0':
        system('cls')
        break
      else:
        system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

  # FORNECEDOR:
  elif opcao == '4':
    while True:
          slogan()
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
          system('cls')
          ctrl_fornec = controller.ControllerFornecedor()
          if opcao == '1':
            ctrl_fornec.cadastrar_fornecedor()
          elif opcao == '2':
            while True:
              slogan()
              opcao = input('------------------------------\n'
                            'ALTERAR FORNECEDOR:\n'
                            '------------------------------\n'
                            '1- ALTERAR NOME\n'
                            '2- ALTERAR CNPJ\n'
                            '3- ALTERAR TELEFONE\n'
                            '0- VOLTAR\n'
                            '------------------------------\n'
                            'OPÇÃO: ')
              system('cls')
              if opcao == '1' or opcao == '2' or opcao == '3':
                ctrl_fornec.alterar_fornecedor(opcao)
              elif opcao == '0':
                system('cls')
                break
              else:
                system('cls')
                cprint('→ OPÇÃO INVÁLIDA...', color='light_red')
          elif opcao == '3':
            ctrl_fornec.excluir_fornecedor()
          elif opcao == '4':
            ctrl_fornec.ver_fornecedores()
          elif opcao == '0':
            system('cls')
            break
          else:
            system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

  # CLIENTE:
  elif opcao == '5':
    while True:
      slogan()
      opcao = input('------------------------------\n'
                    'CLIENTE:\n'
                    '------------------------------\n'
                    '1- CADASTRAR CLIENTE\n'
                    '2- ALTERAR CLIENTE\n'
                    '3- EXCLUIR CLIENTE\n'
                    '4- VER CLIENTES\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      system('cls')
      ctrl_cliente = controller.ControllerCliente()
      if opcao == '1':
        ctrl_cliente.cadastrar_cliente()
      elif opcao == '2':
        while True:
          slogan()
          opcao = input('------------------------------\n'
                        'ALTERAR CLIENTE:\n'
                        '------------------------------\n'
                        '1- ALTERAR NOME\n'
                        '2- ALTERAR CPF\n'
                        '3- ALTERAR TELEFONE\n'
                        '4- ALTERAR EMAIL\n'
                        '5- ALTERAR ENDEREÇO\n'
                        '0- VOLTAR\n'
                        '------------------------------\n'
                        'OPÇÃO: ')
          system('cls')
          if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5':
            ctrl_cliente.alterar_cliente(opcao)
          elif opcao == '0':
            system('cls')
            break
          else:
            system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='light_red')
      elif opcao == '3':
        ctrl_cliente.excluir_cliente()
      elif opcao == '4':
        ctrl_cliente.ver_clientes()
      elif opcao == '0':
        system('cls')
        break
      else:
        system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

  # FUNCIONARIO:
  elif opcao == '6':
    while True:
      slogan()
      opcao = input('------------------------------\n'
                    'FUNCIONÁRIOS:\n'
                    '------------------------------\n'
                    '1- CADASTRAR FUNCIONÁRIO\n'
                    '2- ALTERAR FUNCIONÁRIO\n'
                    '3- EXCLUIR FUNCIONÁRIO\n'
                    '4- VER FUNCIONÁRIOS\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      system('cls')
      ctrl_func = controller.ControllerFuncionario()
      if opcao == '1':
        ctrl_func.cadastrar_funcionario()
      elif opcao == '2':
        while True:
          slogan()
          opcao = input('------------------------------\n'
                        'ALTERAR FUNCIONÁRIO:\n'
                        '------------------------------\n'
                        '1- ALTERAR ID\n'
                        '2- ALTERAR NOME\n'
                        '3- ALTERAR CPF\n'
                        '4- ALTERAR TELEFONE\n'
                        '5- ALTERAR EMAIL\n'
                        '6- ALTERAR ENDEREÇO\n'
                        '0- VOLTAR\n'
                        '------------------------------\n'
                        'OPÇÃO: ')
          system('cls')
          if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5' or opcao == '6':
            ctrl_func.alterar_funcionario(opcao)
          elif opcao == '0':
            system('cls')
            break
          else:
            system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='light_red')
      elif opcao == '3':
        ctrl_func.excluir_funcionario()
      elif opcao == '4':
        ctrl_func.ver_funcionarios()
      elif opcao == '0':
        system('cls')
        break
      else:
        system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

  # ESTOQUE:
  elif opcao == '7':
    while True:
      slogan()
      opcao = input('------------------------------\n'
                    'ESTOQUE\n'
                    '------------------------------\n'
                    '1- ADICIONAR AO ESTOQUE\n'
                    '2- VER ESTOQUE\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      system('cls')
      ctrl_prod = controller.ControllerEstoque()
      if opcao == '1':
        ctrl_prod.add_estoque()
      elif opcao == '2':
        ctrl_prod.ver_estoque()
      elif opcao == '0':
        system('cls')
        break
      else:
        system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

  # RELATÓRIOS:
  elif opcao == '8':
    while True:
      slogan()
      opcao = input('------------------------------\n'
                    'RELATÓRIOS\n'
                    '------------------------------\n'
                    '1- POR VENDA\n'
                    '2- POR DIA\n'
                    '3- POR DATA\n'
                    '4- POR MÊS\n'
                    '5- GERAL\n'
                    '6- MAIS VENDIDOS\n'
                    '7- MELHORES CLIENTES\n'
                    '0- VOLTAR\n'
                    '------------------------------\n'
                    'OPÇÃO: ')
      system('cls')
      ctrl_relat = controller.ControllerRelatorios()
      if opcao == '1':
        while True:
          slogan()
          opcao = input('------------------------------\n'
                        'RELATÓRIO VENDA\n'
                        '------------------------------\n'
                        '1- ID DA VENDA\n'
                        '2- ÚLTIMA VENDA\n'
                        '0- VOLTAR\n'
                        '------------------------------\n'
                        'OPÇÃO: ')
          system('cls')
          ctrl_relat = controller.ControllerRelatorios()
          if opcao == '1':
            ctrl_relat.venda(opcao)
          elif opcao == '2':
            ctrl_relat.venda(opcao)
          elif opcao == '0':
            system('cls')
            break
          else:
            system('cls')
            cprint('→ OPÇÃO INVÁLIDA...', color='light_red')
      elif opcao == '2':
        ctrl_relat.diario()
      elif opcao == '3':
        ctrl_relat.data()
      elif opcao == '4':
        ctrl_relat.mensal()
      elif opcao == '5':
        ctrl_relat.geral()
      elif opcao == '6':
        ctrl_relat.mais_vendidos()
      elif opcao == '7':
        ctrl_relat.melhores_clientes()
      elif opcao == '0':
        system('cls')
        break
      else:
        system('cls')
        cprint('→ OPÇÃO INVÁLIDA...', color='light_red')

   # SAIR:
  elif opcao == '0':
    system('cls')
    print('PROGRAMA FINALIZADO!\n\n')
    break

  # OPÇÃO INVÁLIDA:
  else:
    system('cls')
    cprint('→ OPÇÃO INVÁLIDA...', color='light_red')
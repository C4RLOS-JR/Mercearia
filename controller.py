import os
from termcolor import cprint
from dao import DaoCategoria, DaoCliente, DaoFornecedor, DaoFuncionario, DaoProduto
from model import Categoria, Cliente, Fornecedor, Funcionario, Produto


class ControllerCategoria:

  @classmethod
  def cadastrar_categoria(cls,):
    existe = False
    ver_categorias = DaoCategoria.categorias()
    nova_categoria = input('DIGITE O NOME DA CATEGORIA: ').upper()
    os.system('cls')
    if nova_categoria:
      for categoria in ver_categorias:
        if categoria == nova_categoria:
          existe = True
      if not existe:
        opcao = input(f'DESEJA CADASTRAR A CATEGORIA "{nova_categoria}"?\n'
                      '-------------------------------------------------\n'
                      'DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if opcao == 'S':
          DaoCategoria.adicionar(nova_categoria)
          cprint(f'→ CATEGORIA "{nova_categoria}" CADASTRADA COM SUCESSO...', color='green')
      else:
        cprint('→ ESSA CATEGORIA JÁ EXISTE...', color='yellow')          

  @classmethod
  def alterar_categoria(cls):
    existe = False
    categorias = DaoCategoria.categorias()
    categoria_alterar = input('QUAL CATEGORIA VOCÊ DESEJA ALTERAR?\n'
                              '-----------------------------------\n'
                              'CATEGORIA: ').upper()
    os.system('cls')
    if categoria_alterar:
      for categoria in categorias: 
        if categoria == categoria_alterar:
          existe = True
          categoria_add = input(f'ALTERAR "{categoria_alterar}" POR QUAL CATEGORIA?\n'
                        '-----------------------------------\n'
                        'NOVA CATEGORIA: ').upper()
          os.system('cls')
          if categoria_add:
            if categoria_add not in categorias:
              opcao = input(f'ALTERAR A CATEGORIA: "{categoria_alterar}"\nPARA A CATEGORIA: "{categoria_add}"\n'
                      '-----------------------------------\n'
                      'DIGITE "s" PARA CONFIRMAR: ').upper()
              os.system('cls')
              if opcao == 'S':
                categorias.remove(categoria)
                DaoCategoria.alterar(categorias)
                DaoCategoria.adicionar(categoria_add)
                cprint(f'→ CATEGORIA "{categoria_alterar}" ALTERADA PARA "{categoria_add}"...', color='green')
            else:
              cprint(f'→ JÁ EXISTE A CATEGORIA "{categoria_add}"...', color='yellow')
      if not existe:
        cprint(f'→ NÃO EXISTE A CATEGORIA "{categoria_alterar}"...', color='yellow')

  @classmethod
  def excluir_categoria(cls):
    existe = False
    categorias = DaoCategoria.categorias()
    categoria_excluir = input('QUAL CATEGORIA VOCÊ DESEJA EXCLUIR?\n'
                              '-----------------------------------\n'
                              'CATEGORIA: ').upper()
    os.system('cls')
    if categoria_excluir:
      for categoria in categorias:
        if categoria == categoria_excluir:
          existe = True
          categorias.remove(categoria) 
          confirmar = input(f'DESEJA EXCLUIR A CATEGORIA "{categoria_excluir}"?\n'
                          '-----------------------------------------------\n'
                          'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            DaoCategoria.alterar(categorias)
            cprint('→ CATEGORIA REMOVIDA COM SUCESSO...', color='green')
          break
      if not existe:
        cprint(f'→ NÃO EXISTE A CATEGORIA "{categoria_excluir}"...', color='red')  

  @classmethod
  def ver_categorias(cls):
    ver_categorias = DaoCategoria.categorias()
    ver_categorias.sort()
    print('-------------------')
    cprint('LISTA DE CATEGORIAS', color='yellow')
    print('-------------------')
    for categoria in ver_categorias:
      print(categoria)
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')


class ControllerProduto():

  @classmethod
  def cadastrar_produto(cls):
    existe_prod = False
    existe_cat = False
    categorias = DaoCategoria.categorias()
    estoque = DaoProduto.estoque()
    produto = input('DIGITE O PRODUTO: ').upper()
    if produto:
      for i in estoque:
        produto_estoque = i.split(' | ')
        if produto == produto_estoque[0]:
          existe_prod = True
          os.system('cls')
          cprint(f'→ JÁ EXISTE "{produto}" NO ESTOQUE...', color='yellow')
          break
      if not existe_prod:
        try:
          preco = float(input(f'DIGITE O PREÇO DO(A) "{produto}": ').replace(',', '.'))
          qtd = int(input(f'DIGITE A QUANTIDADE DE "{produto}": '))
          categoria = input(f'DIGITE A CATEGORIA DO(A) "{produto}": ').upper()
          os.system('cls')
        except:
          os.system('cls')
          cprint('DADOS INVÁLIDOS...', color='red')
          return
        if categoria in categorias:
          existe_cat = True
        if not existe_cat:
          cprint(f'A CATEGORIA "{categoria}" NÃO EXISTE, DESEJA CRIA-LA?', color='yellow')
          criar = input('-------------------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if criar == 'S':
            DaoCategoria.adicionar(categoria)
            existe_cat = True
            cprint(f'→ CATEGORIA "{categoria}" CRIADA COM SUCESSO...\n', color='green') 
        if existe_cat:
          confirmar = input(f'DESEJA CADASTRAR O PRODUTO "{produto}"?\n'
                      '-----------------------------------------------\n'
                      'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            DaoProduto.adicionar(categoria, Produto(produto, qtd, preco))
            cprint(f'→ "{produto}" CADASTRADO COM SUCESSO...', color='green') 
          
  @classmethod
  def alterar_produto(cls, opcao):
    cls.opcao = opcao
    existe = False
    estoque = DaoProduto.estoque()
    alterar_produto = input('QUAL PRODUTO VOCÊ DESEJA ALTERAR?\n'
                            '---------------------------------\n'
                            'PRODUTO: ').upper()
    os.system('cls')
    if alterar_produto:
      for i in estoque:
        produto = i.split(' | ')
        if alterar_produto == produto[0]:
          existe = True
          confirmar = input(f'DESEJA ALTERAR O PRODUTO "{alterar_produto}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            estoque.remove(i)
            estoque.pop()
            DaoProduto.alterar(estoque)
            if opcao == '1':
              nome = input('DIGITE O NOVO NOME: ').upper()
              DaoProduto.adicionar(produto[3], Produto(nome, produto[1], produto[2]))
            elif opcao == '2':
              preco = float(input(f'DIGITE O PREÇO DO(A) "{produto[0]}": ').replace(',', '.'))
              DaoProduto.adicionar(produto[3], Produto(produto[0], produto[1], preco))
            elif opcao == '3':
              categoria = input(f'DIGITE A NOVA CATEGORIA DE "{produto[0]}": ').upper()
              DaoProduto.adicionar(categoria, Produto(produto[0], produto[1], produto[2]))
            os.system('cls')
            cprint('→ PRODUTO ALTERADO COM SUCESSO...', color='green')
          break
      if not existe:
        cprint(f'→ NÃO EXISTE "{alterar_produto}" NO ESTOQUE...', color='yellow')

  @classmethod
  def excluir_produto(cls):
    existe = False
    estoque = DaoProduto.estoque()
    excluir_produto = input('QUAL PRODUTO VOCÊ DESEJA EXCLUIR?\n'
                            '---------------------------------\n'
                            'PRODUTO: ').upper()
    os.system('cls')
    if excluir_produto:
      for i in estoque:
        produto = i.split(' | ')
        if excluir_produto == produto[0]:
          existe = True
          opcao = input(f'DESEJA EXCLUIR O PRODUTO "{excluir_produto}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if opcao == 'S':
            estoque.remove(i)
            estoque.pop()
            DaoProduto.alterar(estoque)
            cprint(f'→ "{excluir_produto}" REMOVIDO COM SUCESSO...', color='green')
          break
      if not existe:
        cprint(f'→ NÃO TEM "{excluir_produto}" NO ESTOQUE...', color='yellow')


class ControllerFornecedor:

  @classmethod
  def cadastrar_fornecedor(cls):
    existe = False
    fornecedores = DaoFornecedor.fornecedores()
    fornecedor = input('DIGITE O NOME DO FORNECEDOR: ').upper()
    if fornecedor:
      for i in fornecedores:
        dados = i.split(' | ')
        if fornecedor == dados[0]:
          existe = True
          break
      if not existe:
        try:
          cnpj = input('DIGITE O CNPJ DO FORNECEDOR: ')
          telefone = input('DIGITE O TELEFONE DO FORNECEDOR: ')
        except:
          os.system('cls')
          cprint('DADOS INVÁLIDOS...', color='red')
          return
        DaoFornecedor.adicionar(Fornecedor(fornecedor, cnpj, telefone))
        os.system('cls')
        cprint('→ FORNECEDOR CADASTRADO COM SUCESSO...', color='green')
      else:
        cprint(f'→ FORNECEDOR "{fornecedor}" JÁ EXISTE NO SISTEMA...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def alterar_fornecedor(cls, opcao):
    cls.opcao = opcao
    existe = False
    fornecedor = DaoFornecedor.fornecedores()
    alterar_fornecedor = input('QUAL FORNECEDOR VOCÊ DESEJA ALTERAR?\n'
                            '---------------------------------\n'
                            'FORNECEDOR: ').upper()
    os.system('cls')
    if alterar_fornecedor:
      for i in fornecedor:
        dados = i.split(' | ')
        if alterar_fornecedor == dados[0]:
          existe = True
          confirmar = input(f'DESEJA ALTERAR OS DADOS DO FORNECEDOR "{alterar_fornecedor}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            fornecedor.remove(i)
            fornecedor.pop()
            DaoFornecedor.alterar(fornecedor)
            if opcao == '1':
              nome = input('DIGITE O NOVO NOME: ').upper()
              DaoFornecedor.adicionar(Fornecedor(nome, dados[1], dados[2]))
            elif opcao == '2':
              cnpj = input(f'DIGITE O CNPJ DE "{alterar_fornecedor}": ')
              DaoFornecedor.adicionar(Fornecedor(dados[0], cnpj, dados[2]))
            elif opcao == '3':
              telefone = input(f'DIGITE O TELEFONE DE "{alterar_fornecedor}": ')
              DaoFornecedor.adicionar(Fornecedor(dados[0], dados[1], telefone))
            os.system('cls')
            cprint('→ FORNECEDOR ALTERADO COM SUCESSO...', color='green')
          break    
      if not existe:
        cprint(f'→ O FORNECEDOR "{alterar_fornecedor}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def excluir_fornecedor(cls):
    existe = False
    fornecedor = DaoFornecedor.fornecedores()
    excluir_fornecedor = input('QUAL FORNECEDOR VOCÊ DESEJA EXCLUIR?\n'
                            '---------------------------------\n'
                            'FORNECEDOR: ').upper()
    os.system('cls')
    if excluir_fornecedor:
      for i in fornecedor:
        dados = i.split(' | ')
        if excluir_fornecedor == dados[0]:
          existe = True
          confirmar = input(f'DESEJA EXCLUIR O FORNECEDOR "{excluir_fornecedor}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            fornecedor.remove(i)
            fornecedor.pop()
            DaoFornecedor.alterar(fornecedor)
            os.system('cls')
            cprint(f'→ FORNECEDOR "{excluir_fornecedor}" EXCLUIDO COM SUCESSO...', color='green')
          break
      if not existe:
        os.system('cls')
        cprint(f'→ O FORNECEDOR "{excluir_fornecedor}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def ver_fornecedores(cls):
    fornecedores = DaoFornecedor.fornecedores()
    fornecedores.pop()
    fornecedores.sort()
    print('-------------------------------------------------------------------')
    cprint(f'{"FORNECEDOR":30} {"CNPJ":25} TELEFONE', color='yellow')
    print('-------------------------------------------------------------------')
    for i in fornecedores:
      fornecedor = i.split(' | ')
      print(f'{fornecedor[0]:30} {fornecedor[1]:25} {fornecedor[2]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')


class ControllerCliente:

  @classmethod
  def cadastrar_cliente(cls):
    existe = False
    clientes = DaoCliente.clientes()
    nome = input('DIGITE O NOME DO CLIENTE: ').upper()
    if nome:
      for i in clientes:
        dados = i.split(' | ')
        if nome == dados[0]:
          existe = True
          break
      if not existe:
        try:
          cpf = input('DIGITE O CPF DO CLIENTE: ')
          telefone = input('DIGITE O TELEFONE DO CLIENTE: ')
          email = input('DIGITE O EMAIL DO CLIENTE: ')
          endereco = input('DIGITE O ENDEREÇO DO CLIENTE: ').upper()
          os.system('cls')
        except:
          os.system('cls')
          cprint('DADOS INVÁLIDOS...', color='red')
          return 
        confirmar = input(f'DESEJA CADASTRAR O CLIENTE "{nome}"?\n'
                      '-----------------------------------------------\n'
                      'DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          DaoCliente.cadastrar(Cliente(nome, cpf, telefone, email, endereco))
          cprint('→ CLIENTE CADASTRADO COM SUCESSO...', color='green')
      else:
        cprint('→ CLIENTE JÁ EXISTE NO SISTEMA...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def alterar_cliente(cls, opcao):
    existe = False
    cls.opcao = opcao
    clientes = DaoCliente.clientes()
    alterar_cliente = input('QUAL CLIENTE VOCÊ DESEJA ALTERAR?\n'
                            '---------------------------------\n'
                            'CLIENTE: ').upper()
    os.system('cls')
    if alterar_cliente:
      for i in clientes:
        dados = i.split(' | ')
        if alterar_cliente == dados[0]:
          existe = True
          confirmar = input(f'DESEJA ALTERAR OS DADOS DO CLIENTE "{alterar_cliente}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            clientes.remove(i)
            clientes.pop()
            DaoCliente.alterar(clientes)
            if opcao == '1':
              nome = input('DIGITE O NOVO NOME: ').upper()
              DaoCliente.cadastrar(Cliente(nome, dados[1], dados[2], dados[3], dados[4]))
            elif opcao == '2':
              cpf = input(f'DIGITE O CPF DE "{alterar_cliente}": ')
              DaoCliente.cadastrar(Cliente(dados[0], cpf, dados[2], dados[3], dados[4]))
            elif opcao == '3':
              telefone = input(f'DIGITE O TELEFONE DE "{alterar_cliente}": ')
              DaoCliente.cadastrar(Cliente(dados[0], dados[1], telefone, dados[3], dados[4]))
            elif opcao == '4':
              email = input(f'DIGITE O EMAIL DE "{alterar_cliente}": ')
              DaoCliente.cadastrar(Cliente(dados[0], dados[1], dados[2], email, dados[4]))
            elif opcao == '5':
              endereco = input(f'DIGITE O ENDEREÇO DE "{alterar_cliente}": ').upper()
              DaoCliente.cadastrar(Cliente(dados[0], dados[1], dados[2], dados[3], endereco))
            os.system('cls')
            cprint('→ CLIENTE ALTERADO COM SUCESSO...', color='green')
          break
      if not existe:
        cprint(f'→ O CLIENTE "{alterar_cliente}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def excluir_cliente(cls):
    existe = False
    clientes = DaoCliente.clientes()
    excluir_cliente = input('QUAL CLIENTE VOCÊ DESEJA EXCLUIR?\n'
                            '---------------------------------\n'
                            'CLIENTE: ').upper()
    os.system('cls')
    if excluir_cliente:
      for i in clientes:
        dados = i.split(' | ')
        if excluir_cliente == dados[0]:
          existe = True
          confirmar = input(f'DESEJA EXCLUIR O CLIENTE "{excluir_cliente}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            clientes.remove(i)
            clientes.pop()
            DaoFornecedor.alterar(clientes)
            cprint('→ CLIENTE EXCLUIDO COM SUCESSO...', color='green')
          break
      if not existe:
        cprint(f'→ O CLIENTE "{excluir_cliente}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def ver_clientes(cls):
    clientes = DaoCliente.clientes()
    clientes.pop()
    clientes.sort()
    print('------------------------------------------------------------------------------------------------------------')
    cprint(f'{"CLIENTE":25} {"CPF":15} {"TELEFONE":15} {"EMAIL":20} ENDEREÇO', color='yellow')
    print('------------------------------------------------------------------------------------------------------------')
    for i in clientes:
      cliente = i.split(' | ')
      print(f'{cliente[0]:25} {cliente[1]:15} {cliente[2]:15} {cliente[3]:20} {cliente[4]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')

class ControllerFuncionario:
  
  @classmethod
  def cadastrar_funcionario(cls):
    existe = False
    funcionarios = DaoFuncionario.funcionarios()
    nome = input('DIGITE O NOME DO FUNCIONÁRIO: ').upper()
    if nome:
      for i in funcionarios:
        dados = i.split(' | ')
        if nome == dados[0]:
          existe = True
          break
      if not existe:
        try:
          id = input('DIGITE O ID DO FUNCIONÁRIO: ')
          telefone = input('DIGITE O TELEFONE DO FUNCIONÁRIO: ')
          cpf = input('DIGITE O CPF DO FUNCIONÁRIO: ')
          email = input('DIGITE O EMAIL DO FUNCIONÁRIO: ')
          endereco = input('DIGITE O ENDEREÇO DO FUNCIONÁRIO: ').upper()
          os.system('cls')
        except:
          os.system('cls')
          cprint('DADOS INVÁLIDOS...', color='red')
          return
        confirmar = input(f'DESEJA CADASTRAR O FUNCIONÁRIO "{nome}"?\n'
                      '-----------------------------------------------\n'
                      'DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          DaoFuncionario.cadastrar(Funcionario(nome, id, cpf, telefone, email, endereco))
          cprint('→ FUNCIONÁRIO CADASTRADO COM SUCESSO...', color='green')
      else:
        cprint('→ FUNCIONÁRIO JÁ EXISTE NO SISTEMA...', color='yellow') 
    else:
      os.system('cls')

  @classmethod
  def alterar_funcionario(cls, opcao):
    cls.opcao = opcao
    existe = False
    funcionarios = DaoFuncionario.funcionarios()
    alterar_funcionario = input('QUAL FUNCIONÁRIO VOCÊ DESEJA ALTERAR?\n'
                            '---------------------------------\n'
                            'FUNCIONÁRIO: ').upper()
    os.system('cls')
    if alterar_funcionario:
      for i in funcionarios:
        dados = i.split(' | ')
        if alterar_funcionario == dados[0]:
          existe = True
          confirmar = input(f'DESEJA ALTERAR OS DADOS DO FUNCIONÁRIO "{alterar_funcionario}"?\n'
                        '-----------------------------------------------\n'
                        'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            funcionarios.remove(i)
            funcionarios.pop()
            DaoCliente.alterar(funcionarios)
            if opcao == '1':
              nome = input('DIGITE O NOVO NOME: ').upper()
              DaoCliente.cadastrar(Cliente(nome, dados[1], dados[2], dados[3], dados[4]))
            elif opcao == '2':
              cpf = input(f'DIGITE O CPF DE "{alterar_funcionario}": ')
              DaoCliente.cadastrar(Cliente(dados[0], cpf, dados[2], dados[3], dados[4]))
            elif opcao == '3':
              telefone = input(f'DIGITE O TELEFONE DE "{alterar_funcionario}": ')
              DaoCliente.cadastrar(Cliente(dados[0], dados[1], telefone, dados[3], dados[4]))
            elif opcao == '4':
              email = input(f'DIGITE O EMAIL DE "{alterar_funcionario}": ')
              DaoCliente.cadastrar(Cliente(dados[0], dados[1], dados[2], email, dados[4]))
            elif opcao == '5':
              endereco = input(f'DIGITE O ENDEREÇO DE "{alterar_funcionario}": ').upper()
              DaoCliente.cadastrar(Cliente(dados[0], dados[1], dados[2], dados[3], endereco))

            os.system('cls')
            cprint('→ FUNCIONÁRIO ALTERADO COM SUCESSO...', color='green')
          break
      if not existe:
        cprint(f'→ O FUNCIONÁRIO "{alterar_funcionario}" NÃO EXISTE NO SISTEMA...', color='yellow')







class ControllerEstoque:

  @classmethod
  def add_estoque(cls):
    existe = False
    estoque = DaoProduto.estoque()
    produto = input('DIGITE O PRODUTO: ').upper()
    if produto:
      for i in estoque:
        prod_existente = i.split(' | ')
        if produto == prod_existente[0]:
          existe = True
          break
      if existe:
        prod_existente = i.split(' | ')
        try:
          qtd = int(input(f'DIGITE A QUANTIDADE DE "{produto}": '))
          os.system('cls')
        except:
          os.system('cls')
          cprint('DADOS INVÁLIDOS...', color='red')
          return
        confirmar = input(f'DESEJA ACRESCENTAR {qtd} UNIDADE(S) AO PRODUTO "{produto}"?\n'
                      '------------------------------------------------------------\n'
                      'DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          qtd += int(prod_existente[1])
          estoque.remove(i)
          estoque.pop()
          DaoProduto.alterar(estoque)
          DaoProduto.adicionar(prod_existente[3], Produto(produto, qtd, prod_existente[2]))
          cprint(f'→ "{produto}" ACRESCENTADO COM SUCESSO...', color='green')
      else:
        add = input(f'NÃO TEM "{produto}" NO ESTOQUE, DESEJA ADICIONA-LO?\n'
                    '----------------------------------------------------\n'
                    'DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if add == 'S':
          ControllerProduto.cadastrar_produto()
    else:
      os.system('cls')

  @classmethod
  def ver_estoque(cls):
    estoque = DaoProduto.estoque()
    estoque.pop()
    estoque.sort()

    os.system('cls')
    print('---------------------------------------------------------------')
    cprint(f'{"PRODUTO":25} {"QTD":10}  {"PREÇO":10}   CATEGORIA', color='yellow')
    print('---------------------------------------------------------------')
    for i in estoque:
      produto = i.split(' | ')
      print(f'{produto[0]:25} {produto[1]:10} R$ {produto[2].replace('.', ','):10} {produto[3]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')
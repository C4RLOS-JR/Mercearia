import os
from termcolor import cprint
from dao import DaoCategoria, DaoCliente, DaoFornecedor, DaoFuncionario, DaoProduto, DaoVendas
from model import Cliente, Fornecedor, Funcionario, Produto, Venda
from datetime import datetime

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
        cprint(f'DESEJA CADASTRAR A CATEGORIA "{nova_categoria}"?', color='yellow')
        print('-' * 30)
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          DaoCategoria.cadastrar(nova_categoria)
          cprint(f'→ CATEGORIA "{nova_categoria}" CADASTRADA COM SUCESSO...', color='green')
        else:
          cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
      else:
        cprint('→ ESSA CATEGORIA JÁ EXISTE...', color='yellow')          

  @classmethod
  def alterar_categoria(cls):
    existe = False
    categorias = DaoCategoria.categorias()
    cprint('QUAL CATEGORIA VOCÊ DESEJA ALTERAR?', color='yellow')
    categoria_alterar = input('CATEGORIA: ').upper()
    if categoria_alterar:
      for categoria in categorias: 
        if categoria == categoria_alterar:
          existe = True
          cprint(f'ALTERAR "{categoria_alterar}" POR QUAL CATEGORIA?', color='yellow')
          categoria_add = input('NOVA CATEGORIA: ').upper()
          os.system('cls')
          if categoria_add:
            if categoria_add not in categorias:
              cprint(f'\nALTERAR A CATEGORIA: "{categoria_alterar}"\nPARA: "{categoria_add}"', color='yellow')
              print('-' * 30)
              confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
              os.system('cls')
              if confirmar == 'S':
                categorias.remove(categoria)
                categorias.append(categoria_add)
                DaoCategoria.alterar(categorias)
                cprint(f'→ CATEGORIA "{categoria_alterar}" ALTERADA PARA "{categoria_add}"...', color='green')
              else:
                cprint('→ ALTERAÇÃO NÃO CONFIRMADA...', color='red')
            else:
              cprint(f'→ JÁ EXISTE A CATEGORIA "{categoria_add}"...', color='yellow')
      if not existe:
        os.system('cls')
        cprint(f'→ NÃO EXISTE A CATEGORIA "{categoria_alterar}"...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def excluir_categoria(cls):
    existe = False
    categorias = DaoCategoria.categorias()
    cprint('QUAL CATEGORIA VOCÊ DESEJA EXCLUIR?', color='yellow')
    print('-' * 30)
    categoria_excluir = input('CATEGORIA: ').upper()
    os.system('cls')
    if categoria_excluir:
      for categoria in categorias:
        if categoria == categoria_excluir:
          existe = True
          categorias.remove(categoria) 
          cprint(f'DESEJA EXCLUIR A CATEGORIA "{categoria_excluir}"?', color='yellow')
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            DaoCategoria.alterar(categorias)
            cprint('→ CATEGORIA REMOVIDA COM SUCESSO...', color='green')
          else:
            cprint('→ EXCLUSÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        cprint(f'→ NÃO EXISTE A CATEGORIA "{categoria_excluir}"...', color='red')  

  @classmethod
  def ver_categorias(cls):
    ver_categorias = DaoCategoria.categorias()
    ver_categorias.sort()
    print('-' * 20)
    cprint('LISTA DE CATEGORIAS', color='yellow')
    print('-' * 20)
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
    cadastrar_produto = input('DIGITE O PRODUTO: ').upper()
    if cadastrar_produto:
      for produto in estoque:
        dados = produto.split(' | ')
        if cadastrar_produto == dados[0]:
          existe_prod = True
          os.system('cls')
          cprint(f'→ JÁ EXISTE "{cadastrar_produto}" NO ESTOQUE...', color='yellow')
          break
      if not existe_prod:
        try:
          qtd = int(input(f'DIGITE A QUANTIDADE DE "{cadastrar_produto}": '))
          preco = float(input(f'DIGITE O PREÇO PARA "{cadastrar_produto}": ').replace(',', '.'))
          categoria = input(f'DIGITE A CATEGORIA DE "{cadastrar_produto}": ').upper()
        except:
          os.system('cls')
          cprint('→ DADOS INVÁLIDOS...', color='red')
          return
        if categoria in categorias:
          existe_cat = True
        if not existe_cat:
          cprint(f'A CATEGORIA "{categoria}" NÃO EXISTE, DESEJA CRIA-LA?', color='yellow')
          print('-' * 30)
          criar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if criar == 'S':
            DaoCategoria.cadastrar(categoria)
            existe_cat = True
            os.system('cls')
            cprint(f'→ CATEGORIA "{categoria}" CRIADA COM SUCESSO...', color='green')
          else:
            cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
        if existe_cat:
          cprint(f'\nDESEJA CADASTRAR O PRODUTO "{cadastrar_produto}"?', color='yellow')
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            DaoProduto.cadastrar(Produto(cadastrar_produto, qtd, f'{preco:.2f}', categoria))
            cprint(f'→ "{cadastrar_produto}" CADASTRADO COM SUCESSO...', color='green') 
          else:
            cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
    else:
      os.system('cls')
          
  @classmethod
  def alterar_produto(cls, opcao):
    cls.opcao = opcao
    existe = False
    estoque = DaoProduto.estoque()
    estoque.pop()
    cprint('QUAL PRODUTO VOCÊ DESEJA ALTERAR?', color='yellow')
    alterar_produto = input('PRODUTO: ').upper()
    if alterar_produto:
      for produto in estoque:
        dados = produto.split(' | ')
        if alterar_produto == dados[0]:
          existe = True  
          try:
            if opcao == '1':
              nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_produto}": ').upper()
              cprint(f'\nALTERAR O NOME: "{dados[0]}"\nPARA: "{nome}"', color='yellow')
              dados[0] = nome
            elif opcao == '2':
              preco = float(input(f'DIGITE UM NOVO PREÇO PARA "{alterar_produto}": ').replace(',', '.'))
              cprint(f'\nALTERAR O PREÇO: R${dados[2]}\nPARA: R${preco:.2f}'.replace('.', ','), color='yellow')
              dados[2] = f'{preco:.2f}'.replace('.', ',')



            elif opcao == '3':
              categoria = input(f'DIGITE UMA NOVA CATEGORIA PARA "{alterar_produto}": ').upper()
              cprint(f'\nALTERAR A CATEGORIA: "{dados[3]}"\nPARA: "{categoria}"', color='yellow')
              dados[3] = categoria
          except:
            os.system('cls')
            cprint('→ DADOS INVÁLIDOS...', color='red')
            return
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            estoque.remove(produto)
            DaoProduto.alterar(estoque)
            DaoProduto.cadastrar(Produto(dados[0], dados[1], dados[2], dados[3]))
            cprint('→ PRODUTO ALTERADO COM SUCESSO...', color='green')
          else:
            cprint('→ ALTERAÇÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        os.system('cls')
        cprint(f'→ NÃO EXISTE "{alterar_produto}" NO ESTOQUE...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def excluir_produto(cls):
    existe = False
    estoque = DaoProduto.estoque()
    estoque.pop()
    cprint('QUAL PRODUTO VOCÊ DESEJA EXCLUIR?', color='yellow')
    print('-' * 30)
    excluir_produto = input('PRODUTO: ').upper()
    os.system('cls')
    if excluir_produto:
      for produto in estoque:
        dados = produto.split(' | ')
        if excluir_produto == dados[0]:
          existe = True
          cprint(f'DESEJA EXCLUIR O PRODUTO "{excluir_produto}"?', color='yellow')
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            estoque.remove(produto)
            DaoProduto.alterar(estoque)
            cprint(f'→ "{excluir_produto}" REMOVIDO COM SUCESSO...', color='green')
          else:
            cprint('→ EXCLUSÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        cprint(f'→ NÃO TEM "{excluir_produto}" NO ESTOQUE...', color='yellow')


class ControllerFornecedor:

  @classmethod
  def cadastrar_fornecedor(cls):
    existe = False
    fornecedores = DaoFornecedor.fornecedores()
    nome = input('DIGITE O NOME DO(A) FORNECEDOR(A): ').upper()
    if nome:
      for fornecedor in fornecedores:
        dados = fornecedor.split(' | ')
        if nome == dados[0]:
          existe = True
          break
      if not existe:
        try:
          cnpj = input(f'DIGITE O CNPJ DE {nome}: ')
          telefone = input(f'DIGITE O TELEFONE DE {nome}: ')
        except:
          os.system('cls')
          cprint('→ DADOS INVÁLIDOS...', color='red')
          return
        cprint(f'\nDESEJA CADASTRAR O(A) FORNECEDOR(A) "{dados[0]}"?', color='yellow')
        print('-' * 30)
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          DaoFornecedor.cadastrar(Fornecedor(nome, cnpj, telefone))
          cprint('→ FORNECEDOR(A) CADASTRADO(A) COM SUCESSO...', color='green')
        else:
          cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
      else:
        os.system('cls')
        cprint(f'→ FORNECEDOR(A) "{nome}" JÁ EXISTE NO SISTEMA...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def alterar_fornecedor(cls, opcao):
    cls.opcao = opcao
    existe = False
    fornecedores = DaoFornecedor.fornecedores()
    fornecedores.pop()
    alterar_fornecedor = input('QUAL FORNECEDOR(A) VOCÊ DESEJA ALTERAR?: ').upper()
    if alterar_fornecedor:
      for fornecedor in fornecedores:
        dados = fornecedor.split(' | ')
        if alterar_fornecedor == dados[0]:
          existe = True
          try:
            if opcao == '1':
              nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_fornecedor}": ').upper()
              cprint(f'\nALTERAR O NOME: "{dados[0]}"\nPARA: "{nome}"?', color='yellow')
              dados[0] = nome
            if opcao == '2':
              cnpj = input(f'DIGITE UM NOVO CNPJ PARA "{alterar_fornecedor}": ')
              cprint(f'\nALTERAR O CNPJ: "{dados[1]}"\nPARA: "{cnpj}"?', color='yellow')
              dados[1] = cnpj
            if opcao == '3':
              telefone = input(f'DIGITE UM NOVO TELEFONE PARA "{alterar_fornecedor}": ')
              cprint(f'\nALTERAR O TELEFONE: "{dados[2]}"\nPARA: "{telefone}"?', color='yellow')
              dados[2] = telefone
          except:
            os.system('cls')
            cprint('→ DADOS INVÁLIDOS...', color='red')
            return
          print('-' * 30)
          confirmar = input(f'DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            fornecedores.remove(fornecedor)
            DaoFornecedor.alterar(fornecedores)
            DaoFornecedor.cadastrar(Fornecedor(dados[0], dados[1], dados[2]))
            cprint('→ FORNECEDOR(A) ALTERADO(A) COM SUCESSO...', color='green')
          else:
            cprint('→ ALTERAÇÃO NÃO CONFIRMADA...', color='red')
          break    
      if not existe:
        os.system('cls')
        cprint(f'→ O(A) FORNECEDOR(A) "{alterar_fornecedor}" NÃO EXISTE NO SISTEMA...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def excluir_fornecedor(cls):
    existe = False
    fornecedores = DaoFornecedor.fornecedores()
    fornecedores.pop()
    cprint('QUAL FORNECEDOR(A) VOCÊ DESEJA EXCLUIR?', color='yellow')
    print('-' * 30)
    excluir_fornecedor = input('FORNECEDOR(A): ').upper()
    os.system('cls')
    if excluir_fornecedor:
      for fornecedor in fornecedores:
        dados = fornecedor.split(' | ')
        if excluir_fornecedor == dados[0]:
          existe = True
          cprint(f'DESEJA EXCLUIR O(A) FORNECEDOR(A) "{excluir_fornecedor}"?', color='yellow')
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            fornecedores.remove(fornecedor)
            DaoFornecedor.alterar(fornecedores)
            os.system('cls')
            cprint(f'→ FORNECEDOR(A) "{excluir_fornecedor}" EXCLUIDO(A) COM SUCESSO...', color='green')
          else:
            cprint('→ EXCLUSÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        cprint(f'→ O(A) FORNECEDOR(A) "{excluir_fornecedor}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def ver_fornecedores(cls):
    fornecedores = DaoFornecedor.fornecedores()
    fornecedores.pop()
    fornecedores.sort()
    print('-' * 67)
    cprint(f'{"FORNECEDOR(A)":30} {"CNPJ":25} TELEFONE', color='yellow')
    print('-' * 67)
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
    nome = input('NOME DO(A) CLIENTE: ').upper()
    if nome:
      for cliente in clientes:
        dados = cliente.split(' | ')
        if nome == dados[0]:
          existe = True
          break
      if not existe:
        try:
          cpf = input(f'CPF DE {nome}: ')
          telefone = input(f'TELEFONE DE {nome}: ')
          email = input(f'EMAIL DE {nome}: ')
          endereco = input(f'ENDEREÇO DE {nome}: ').upper()
        except:
          os.system('cls')
          cprint('→ DADOS INVÁLIDOS...', color='red')
          return 
        cprint(f'\nDESEJA CADASTRAR O(A) CLIENTE "{nome}"?', color='yellow')
        print('-' * 30)
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          DaoCliente.cadastrar(Cliente(nome, cpf, telefone, email, endereco))
          cprint('→ CLIENTE CADASTRADO COM SUCESSO...', color='green')
        else:
          cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
      else:
        os.system('cls')
        cprint('→ CLIENTE JÁ EXISTE NO SISTEMA...', color='yellow')      
    else:
      os.system('cls')

  @classmethod
  def alterar_cliente(cls, opcao):
    existe = False
    cls.opcao = opcao
    clientes = DaoCliente.clientes()
    clientes.pop()
    cprint('QUAL CLIENTE VOCÊ DESEJA ALTERAR?', color='yellow')
    alterar_cliente = input('CLIENTE: ').upper()
    if alterar_cliente:
      for cliente in clientes:
        dados = cliente.split(' | ')
        if alterar_cliente == dados[0]:
          existe = True
          try:
            if opcao == '1':
              nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_cliente}": ').upper()
              cprint(f'\nALTERAR O NOME: "{dados[0]}"\nPARA: "{nome}"?', color='yellow')
              dados[0] = nome
            elif opcao == '2':
              cpf = input(f'DIGITE UM NOVO CPF PARA "{alterar_cliente}": ')
              cprint(f'\nALTERAR O CPF: "{dados[1]}"\nPARA: "{cpf}"?', color='yellow')
              dados[1] = cpf
            elif opcao == '3':
              telefone = input(f'DIGITE UM NOVO TELEFONE PARA "{alterar_cliente}": ')
              cprint(f'\nALTERAR O TELEFONE: "{dados[2]}"\nPARA: "{telefone}"?', color='yellow')
              dados[2] = telefone
            elif opcao == '4':
              email = input(f'DIGITE UM NOVO EMAIL PARA "{alterar_cliente}": ')
              cprint(f'\nALTERAR O EMAIL: "{dados[3]}"\nPARA: "{email}"?', color='yellow')
              dados[3] = email
            elif opcao == '5':
              endereco = input(f'DIGITE UM NOVO ENDEREÇO PARA "{alterar_cliente}": ').upper()
              cprint(f'\nALTERAR O ENDEREÇO: "{dados[4]}"\nPARA: "{endereco}"?', color='yellow')
              dados[4] = endereco
          except:
            os.system('cls')
            cprint('→ DADOS INVÁLIDOS...', color='red')
            return
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            clientes.remove(cliente)
            DaoCliente.alterar(clientes)
            DaoCliente.cadastrar(Cliente(dados[0], dados[1], dados[2], dados[3], dados[4]))
            cprint('→ CLIENTE ALTERADO COM SUCESSO...', color='green')
          else:
            cprint('→ ALTERAÇÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        os.system('cls')
        cprint(f'→ O(A) CLIENTE "{alterar_cliente}" NÃO EXISTE NO SISTEMA...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def excluir_cliente(cls):
    existe = False
    clientes = DaoCliente.clientes()
    clientes.pop()
    cprint('QUAL CLIENTE VOCÊ DESEJA EXCLUIR?', color='yellow')
    print('-' * 30)
    excluir_cliente = input('CLIENTE: ').upper()
    os.system('cls')
    if excluir_cliente:
      for cliente in clientes:
        dados = cliente.split(' | ')
        if excluir_cliente == dados[0]:
          existe = True
          cprint(f'DESEJA EXCLUIR O(A) CLIENTE "{excluir_cliente}"?', color='yellow')
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            clientes.remove(cliente)
            DaoCliente.alterar(clientes)
            cprint('→ CLIENTE EXCLUIDO COM SUCESSO...', color='green')
          else:
            cprint('→ EXCLUSÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        cprint(f'→ O(A) CLIENTE "{excluir_cliente}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def ver_clientes(cls):
    clientes = DaoCliente.clientes()
    clientes.pop()
    clientes.sort()
    print('-' * 110)
    cprint(f'{"CLIENTE":25} {"CPF":15} {"TELEFONE":15} {"EMAIL":20} ENDEREÇO', color='yellow')
    print('-' * 110)
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
    nome = input('DIGITE O NOME DO(A) FUNCIONÁRIO(A): ').upper()
    if nome:
      for funcionario in funcionarios:
        dados = funcionario.split(' | ')
        if nome == dados[0]:
          existe = True
          break
      if not existe:
        try:
          id = input(f'DIGITE UM ID PARA {nome}: ')
          cpf = input(f'DIGITE O CPF DE {nome}: ')
          telefone = input(f'DIGITE O TELEFONE DE {nome}: ')
          email = input(f'DIGITE O EMAIL De {nome} ')
          endereco = input(f'DIGITE O ENDEREÇO DE {nome}: ').upper()
        except:
          os.system('cls')
          cprint('→ DADOS INVÁLIDOS...', color='red')
          return
        cprint(f'\nDESEJA CADASTRAR O(A) FUNCIONÁRIO(A) "{nome}"?', color='yellow')
        print('-' * 30)
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          DaoFuncionario.cadastrar(Funcionario(id, nome, cpf, telefone, email, endereco))
          cprint('→ FUNCIONÁRIO(A) CADASTRADO(A) COM SUCESSO...', color='green')
        else:
          cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
      else:
        os.system('cls')
        cprint('→ FUNCIONÁRIO(A) JÁ EXISTE NO SISTEMA...', color='yellow') 
    else:
      os.system('cls')

  @classmethod
  def alterar_funcionario(cls, opcao):
    cls.opcao = opcao
    existe = False
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    cprint('QUAL FUNCIONÁRIO(A) VOCÊ DESEJA ALTERAR?', color='yellow')
    alterar_funcionario = input('FUNCIONÁRIO(A): ').upper()
    if alterar_funcionario:
      for funcionario in funcionarios:
        dados = funcionario.split(' | ')
        if alterar_funcionario == dados[1]:
          existe = True
          try:
            if opcao == '1':
              id = input(f'DIGITE UM NOVO ID PARA "{alterar_funcionario}": ').upper()
              cprint(f'\nALTERAR O ID: "{dados[0]}"\nPARA: "{id}"?', color='yellow')
              dados[0] = id
            if opcao == '2':
              nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_funcionario}": ').upper()
              cprint(f'\nALTERAR O NOME: "{dados[1]}"\nPARA: "{nome}"?', color='yellow')
              dados[1] = nome
            elif opcao == '3':
              cpf = input(f'DIGITE UM NOVO CPF PARA "{alterar_funcionario}": ')
              cprint(f'\nALTERAR O CPF: "{dados[2]}"\nPARA: "{cpf}"?', color='yellow')
              dados[2] = cpf
            elif opcao == '4':
              telefone = input(f'DIGITE UM NOVO TELEFONE PARA "{alterar_funcionario}": ')
              cprint(f'\nALTERAR O TELEFONE: "{dados[3]}"\nPARA: "{telefone}"?', color='yellow')
              dados[3] = telefone
            elif opcao == '5':
              email = input(f'DIGITE UM NOVO EMAIL PARA "{alterar_funcionario}": ')
              cprint(f'\nALTERAR O EMAIL: "{dados[4]}"\nPARA: "{email}"?', color='yellow')
              dados[4] = email
            elif opcao == '6':
              endereco = input(f'DIGITE UM NOVO ENDEREÇO PARA "{alterar_funcionario}": ').upper()
              cprint(f'\nALTERAR O ENDEREÇO: "{dados[5]}"\nPARA: "{endereco}"?', color='yellow')
              dados[5] = endereco
          except:
            os.system('cls')
            cprint('→ DADOS INVÁLIDOS...', color='red')
            return
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            funcionarios.remove(funcionario)
            DaoFuncionario.alterar(funcionarios)
            DaoFuncionario.cadastrar(Funcionario(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]))
            cprint('→ FUNCIONÁRIO(A) ALTERADO(A) COM SUCESSO...', color='green')
          else:
            cprint('→ ALTERAÇÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        os.system('cls')
        cprint(f'→ O(A) FUNCIONÁRIO(A) "{alterar_funcionario}" NÃO EXISTE NO SISTEMA...', color='yellow')
    else:
      os.system('cls')

  @classmethod
  def excluir_funcionario(cls):
    existe = False
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    cprint('QUAL FUNCIONÁRIO(A) VOCÊ DESEJA EXCLUIR?', color='yellow')
    print('-' * 30)
    excluir_funcionario = input('FUNCIONÁRIO(A): ').upper()
    os.system('cls')
    if excluir_funcionario:
      for funcionario in funcionarios:
        dados = funcionario.split(' | ')
        if excluir_funcionario == dados[1]:
          existe = True
          cprint(f'DESEJA EXCLUIR O(A) FUNCIONÁRIO(A) "{excluir_funcionario}"?', color='yellow')
          print('-'*30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            funcionarios.remove(funcionario)
            DaoFuncionario.alterar(funcionarios)
            cprint('→ FUNCIONÁRIO(A) EXCLUIDO(A) COM SUCESSO...', color='green')
          else:
            cprint('→ EXCLUSÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        cprint(f'→ O(A) FUNCIONÁRIO(A) "{excluir_funcionario}" NÃO EXISTE NO SISTEMA...', color='yellow')

  @classmethod
  def ver_funcionarios(cls):
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    funcionarios.sort()
    os.system('cls')
    print('-'*130)
    cprint(f'{"ID":6} {"fUNCIONÁRIO(A)":20} {"CPF":20} {"TELEFONE":15} {"EMAIL":25} ENDEREÇO', color='yellow')
    print('-'*130)
    for funcionario in funcionarios:
      dados = funcionario.split(' | ')
      print(f'{dados[0]:6} {dados[1]:20} {dados[2]:20} {dados[3]:15} {dados[4]:25} {dados[5]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')


class ControllerEstoque:

  @classmethod
  def add_estoque(cls):
    existe = False
    estoque = DaoProduto.estoque()
    estoque.pop()
    add_produto = input('DIGITE O PRODUTO: ').upper()
    if add_produto:
      for produto in estoque:
        prod_existente = produto.split(' | ')
        if add_produto == prod_existente[0]:
          existe = True
          try:
            qtd = int(input(f'DIGITE A QUANTIDADE DE "{add_produto}": '))
            os.system('cls')
          except:
            os.system('cls')
            cprint('→ DADOS INVÁLIDOS...', color='red')
            return
          cprint(f'DESEJA ACRESCENTAR {qtd} UNIDADE(S) AO PRODUTO "{add_produto}"?', color='yellow')
          print('-' * 30)
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          os.system('cls')
          if confirmar == 'S':
            qtd += int(prod_existente[1])
            estoque.remove(produto)
            DaoProduto.alterar(estoque)
            DaoProduto.cadastrar(Produto(add_produto, qtd, prod_existente[2], prod_existente[3]))
            cprint(f'→ "{add_produto}" ACRESCENTADO COM SUCESSO...', color='green')
          else:
            cprint('→ ADIÇÃO NÃO CONFIRMADA...', color='red')
          break
      if not existe:
        cprint(f'NÃO TEM "{add_produto}" NO ESTOQUE, DESEJA CADASTRA-LO?', color='yellow')
        print('-' * 30)
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          ControllerProduto.cadastrar_produto()
        else:
            cprint('→ CADASTRO NÃO CONFIRMADO...', color='red')
    else:
      os.system('cls')

  @classmethod
  def ver_estoque(cls):
    estoque = DaoProduto.estoque()
    estoque.pop()
    estoque.sort()
    os.system('cls')
    print('-' * 65)
    cprint(f'{"PRODUTO":25} {"QTD":10}  {"PREÇO":10}   CATEGORIA', color='yellow')
    print('-' * 65)
    for produto in estoque:
      dados = produto.split(' | ')
      print(f'{dados[0]:25} {dados[1]:10} R${dados[2].replace('.', ','):10} {dados[3]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')


class ControllerVendas:
  
  @classmethod
  def vender(cls):
    estoque = DaoProduto.estoque()
    estoque.pop()
    clientes = DaoCliente.clientes()
    clientes.pop()
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    horario = datetime.now()
    msg = 0
    total_itens = 0
    total_pagar = 0
    total_volumes = 0
    lista_compras = []
    slogan = lambda: cprint(f'{"MERCEARIA PYTHONFULL":^65}\n', color='light_blue')
    
    def lista():
      slogan()
      cprint(f'{"QTD":^5}{"PRODUTO":^32}{"VALOR":^14}{"V.TOTAL":^14}', color='yellow')
      print('-' * 65)
      for i in lista_compras:
        print(f'|{i[0]:>3}| {i[1]:30}| R${i[2]:10}| R${i[3]:10}|')
      print('-' * 65)
      cprint(f'{total_itens:>5} {"ITEM(S)":<8}{total_volumes:>5} {"VOLUME(S)":<12}{"TOTAL À PAGAR:":>19} R${total_pagar:<10.2f}', color='yellow')

    while True:
      existe = False
      os.system('cls')
      lista()
      # mensagens:
      if msg == 0:
        cprint(f'\n→ INICIANDO O REGISTRO DE COMPRAS...\n', color='light_blue')
      elif msg == 1:
        cprint(f'\n→ "{item}" ADICIONADO(A) A COMPRA...\n', color='green')
      elif msg == 2:
        cprint('\n→ DADOS INVÁLIDOS...\n', color='red')
      elif msg == 3:
        cprint(f'\n→ "{item}" NÃO EXISTENTE NO ESTOQUE...\n', color='red')

      print('DIGITE "0" EM PRODUTO PARA ENCERRAR!\n')
      item = input('PRODUTO: ').upper()
      if item == '0':
        break
      for produto in estoque:
        dados = produto.split(' | ')
        if item == dados[0]:
          existe = True
          try:
            qtd = int(input(f'QUANTIDADE DE {item}(S): '))
            total = f'{float(dados[2].replace(',', '.')) * qtd:.2f}'.replace('.', ',')
            total_itens += 1
            total_volumes += qtd
            total_pagar += float(total.replace(',', '.'))
            lista_compras.append([qtd, item, dados[2], total])
            msg = 1
            break      
          except ValueError:
            msg = 2  
      if not existe:
          msg = 3
    while True:
      cliente_existe = False
      funcionario_existe = False
      os.system('cls')
      lista()
      print('\n')
      cpf_cliente = input('INFORME O CPF DO CLIENTE: ')
      if cpf_cliente:
        for cliente in clientes:
          dados_cliente = cliente.split(' | ')
          if cpf_cliente == dados_cliente[1]:
            cliente_existe = True
            break
        if cliente_existe:
          id_funcionario = input('INFORME O ID DO VENDEDOR: ')
          for funcionario in funcionarios:
            dados_funcionario = funcionario.split(' | ')
            if id_funcionario == dados_funcionario[0]:
              funcionario_existe = True
              break
          if not funcionario_existe:
            cprint('FUNCIONÁRIO NÃO CADASTRADO!...')
        else:
          input('CLIENTE NÃO CADASTRADO!...DESEJA CADASTRAR CLIENTE?...')
      else:
        os.system('cls')
      if cliente_existe and funcionario_existe:
        os.system('cls')
        slogan()
        cprint(f'COMPRA ENCERRADA NO VALOR DE R${total_pagar:.2f}', color='green')
        print('-' * 50)
        print(f'CLIENTE: {dados_cliente[0]}\n'
              f'CPF: {dados_cliente[1]}\n'
              f'ENDEREÇO: {dados_cliente[4]}\n')
        print(f'VENDEDOR: {dados_funcionario[1]}\n'
              f'CPF: {dados_funcionario[2]}\n'
              f'ID: {dados_funcionario[0]}\n')
        print(f'DATA: {horario}\n')
        cprint(f'CONFIRMAR O PAGAMENTO NO VALOR DE R${total_pagar:.2f}', color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        os.system('cls')
        if confirmar == 'S':
          slogan()
          cprint('PAGAMENTO CONFIRMADO!...VOLTE SEMPRE...:)\n', color='light_green')
          print('-' * 50)
          input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
          os.system('cls')
          break
  #DaoVendas.venda(Venda(qtd, item, dados[2], dados[3], total, total_itens, total_pagar))

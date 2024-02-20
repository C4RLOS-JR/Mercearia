import os
from os import system
from termcolor import cprint
from dao import DaoCategoria, DaoCliente, DaoFornecedor, DaoFuncionario, DaoProduto, DaoRelatorios, DaoVendas
from model import Cliente, Fornecedor, Funcionario, Produto, Venda
from datetime import datetime


class ControllerCategoria:

  @classmethod
  def cadastrar_categoria(cls,):
    existe = False
    ver_categorias = DaoCategoria.categorias()
    nova_categoria = input('DIGITE O NOME DA CATEGORIA: ').upper()
    if nova_categoria:
      for categoria in ver_categorias:
        if categoria == nova_categoria:
          existe = True
      if not existe:
        info = f'DESEJA CADASTRAR A CATEGORIA "{nova_categoria}"?'
        print('-' * len(info))
        cprint(info, color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        system('cls')
        if confirmar == 'S':
          DaoCategoria.cadastrar(nova_categoria)
          cprint(f'>> CATEGORIA CADASTRADA COM SUCESSO\n', color='green')
        else:
          cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
      else:
        cprint('>> ESSA CATEGORIA JÁ EXISTE\n', color='yellow')
    else:
      system('cls')         

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
          info = f'ALTERAR "{categoria_alterar}" POR QUAL CATEGORIA?'
          print('-' * len(info))
          cprint(info, color='yellow')
          categoria_add = input('NOVA CATEGORIA: ').upper()
          if categoria_add:
            if categoria_add not in categorias:
              info = f'ALTERAR A CATEGORIA "{categoria_alterar}" PARA "{categoria_add}"?'
              print('-' * len(info))
              cprint(info, color='yellow')
              confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
              system('cls')
              if confirmar == 'S':
                categorias.remove(categoria)
                categorias.append(categoria_add)
                DaoCategoria.alterar(categorias)
                cprint(f'>> CATEGORIA ALTERADA COM SUCESSO\n', color='green')
              else:
                cprint('>> ALTERAÇÃO NÃO CONFIRMADA\n', color='light_red')
            else:
              cprint(f'>> JÁ EXISTE A CATEGORIA "{categoria_add}"\n', color='yellow')
      if not existe:
        system('cls')
        cprint(f'>> NÃO EXISTE A CATEGORIA "{categoria_alterar}"\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def excluir_categoria(cls):
    existe = False
    categorias = DaoCategoria.categorias()
    cprint('QUAL CATEGORIA VOCÊ DESEJA EXCLUIR?', color='yellow')
    categoria_excluir = input('CATEGORIA: ').upper()
    if categoria_excluir:
      for categoria in categorias:
        if categoria == categoria_excluir:
          existe = True
          categorias.remove(categoria)
          info = f'DESEJA EXCLUIR A CATEGORIA "{categoria_excluir}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            DaoCategoria.alterar(categorias)
            cprint('>> CATEGORIA REMOVIDA COM SUCESSO\n', color='green')
          else:
            cprint('>> EXCLUSÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        system('cls')
        cprint(f'>> NÃO EXISTE A CATEGORIA "{categoria_excluir}"\n', color='light_red')
    else:
      system('cls')

  @classmethod
  def ver_categorias(cls):
    ver_categorias = DaoCategoria.categorias()
    ver_categorias.sort()
    print('-' * 20)
    cprint('LISTA DE CATEGORIAS!', color='yellow')
    print('-' * 20)
    for categoria in ver_categorias:
      print(categoria)
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    system('cls')


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
          system('cls')
          cprint(f'>> JÁ EXISTE "{cadastrar_produto}" NO ESTOQUE\n', color='yellow')
          break
      if not existe_prod:
        try:
          qtd = int(input(f'DIGITE A QUANTIDADE DE "{cadastrar_produto}": '))
          preco = float(input(f'DIGITE O PREÇO PARA "{cadastrar_produto}": ').replace(',', '.'))
          categoria = input(f'DIGITE A CATEGORIA DE "{cadastrar_produto}": ').upper()
        except:
          system('cls')
          cprint('>> DADOS INVÁLIDOS\n', color='light_red')
          return
        if categoria in categorias:
          existe_cat = True
        if not existe_cat:
          info = f'A CATEGORIA "{categoria}" NÃO EXISTE, DESEJA CRIA-LA?'
          print('-' * len(info))
          cprint(info, color='yellow')
          criar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          if criar == 'S':
            DaoCategoria.cadastrar(categoria)
            existe_cat = True
            system('cls')
            cprint(f'>> CATEGORIA CRIADA COM SUCESSO\n', color='green')
          else:
            system('cls')
            cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
        if existe_cat:
          info = f'DESEJA CADASTRAR O PRODUTO "{cadastrar_produto}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            DaoProduto.cadastrar(Produto(cadastrar_produto, qtd, f'{preco:.2f}', categoria))
            cprint(f'>> PRODUTO CADASTRADO COM SUCESSO\n', color='green') 
          else:
            cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
    else:
      system('cls')
          
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
          if opcao == '1':
            nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_produto}": ').upper()
            info = f'ALTERAR O NOME "{dados[0]}" PARA "{nome}"'
            dados[0] = nome
          elif opcao == '2':
            preco = float(input(f'DIGITE UM NOVO PREÇO PARA "{alterar_produto}": ').replace(',', '.'))
            info = f'ALTERAR O PREÇO R${dados[2]} PARA R${preco:.2f}'.replace('.', ',')
            dados[2] = f'{preco:.2f}'.replace('.', ',')
          elif opcao == '3':
            categoria = input(f'DIGITE UMA NOVA CATEGORIA PARA "{alterar_produto}": ').upper()
            info = f'ALTERAR A CATEGORIA "{dados[3]}" PARA "{categoria}"'
            dados[3] = categoria
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            estoque.remove(produto)
            DaoProduto.alterar(estoque)
            DaoProduto.cadastrar(Produto(dados[0], dados[1], dados[2], dados[3]))
            cprint('>> PRODUTO ALTERADO COM SUCESSO\n', color='green')
          else:
            cprint('>> ALTERAÇÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        system('cls')
        cprint(f'>> NÃO EXISTE "{alterar_produto}" NO ESTOQUE\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def excluir_produto(cls):
    existe = False
    estoque = DaoProduto.estoque()
    estoque.pop()
    cprint('QUAL PRODUTO VOCÊ DESEJA EXCLUIR?', color='yellow')
    excluir_produto = input('PRODUTO: ').upper()
    if excluir_produto:
      for produto in estoque:
        dados = produto.split(' | ')
        if excluir_produto == dados[0]:
          existe = True
          info = f'DESEJA EXCLUIR O PRODUTO "{excluir_produto}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            estoque.remove(produto)
            DaoProduto.alterar(estoque)
            cprint(f'>> PRODUTO REMOVIDO COM SUCESSO\n', color='green')
          else:
            cprint('>> EXCLUSÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        system('cls')
        cprint(f'>> NÃO EXISTE "{excluir_produto}" NO ESTOQUE\n', color='yellow')
    else:
      system('cls')


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
          system('cls')
          cprint('>> DADOS INVÁLIDOS\n', color='light_red')
          return
        info = f'DESEJA CADASTRAR "{nome}"?'
        print('-' * len(info))
        cprint(info, color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        system('cls')
        if confirmar == 'S':
          DaoFornecedor.cadastrar(Fornecedor(nome, cnpj, telefone))
          cprint('>> FORNECEDOR(A) CADASTRADO(A) COM SUCESSO\n', color='green')
        else:
          cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
      else:
        system('cls')
        cprint(f'>> FORNECEDOR(A) "{nome}" JÁ EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def alterar_fornecedor(cls, opcao):
    cls.opcao = opcao
    existe = False
    fornecedores = DaoFornecedor.fornecedores()
    fornecedores.pop()
    cprint('QUAL FORNECEDOR(A) VOCÊ DESEJA ALTERAR?', color='yellow')
    alterar_fornecedor = input('FORNECEDOR: ').upper()
    if alterar_fornecedor:
      for fornecedor in fornecedores:
        dados = fornecedor.split(' | ')
        if alterar_fornecedor == dados[0]:
          existe = True
          if opcao == '1':
            nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_fornecedor}": ').upper()
            info = f'ALTERAR O NOME "{dados[0]}" PARA "{nome}"?'
            dados[0] = nome
          if opcao == '2':
            cnpj = input(f'DIGITE UM NOVO CNPJ PARA "{alterar_fornecedor}": ')
            info = f'ALTERAR O CNPJ "{dados[1]}" PARA "{cnpj}"?'
            dados[1] = cnpj
          if opcao == '3':
            telefone = input(f'DIGITE UM NOVO TELEFONE PARA "{alterar_fornecedor}": ')
            info = f'ALTERAR O TELEFONE "{dados[2]}" PARA "{telefone}"?'
            dados[2] = telefone
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input(f'DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            fornecedores.remove(fornecedor)
            DaoFornecedor.alterar(fornecedores)
            DaoFornecedor.cadastrar(Fornecedor(dados[0], dados[1], dados[2]))
            cprint('>> FORNECEDOR(A) ALTERADO(A) COM SUCESSO\n', color='green')
          else:
            cprint('>> ALTERAÇÃO NÃO CONFIRMADA\n', color='light_red')
          break    
      if not existe:
        system('cls')
        cprint(f'>> O(A) FORNECEDOR(A) "{alterar_fornecedor}" NÃO EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def excluir_fornecedor(cls):
    existe = False
    fornecedores = DaoFornecedor.fornecedores()
    fornecedores.pop()
    cprint('QUAL FORNECEDOR(A) VOCÊ DESEJA EXCLUIR?', color='yellow')
    excluir_fornecedor = input('FORNECEDOR(A): ').upper()
    if excluir_fornecedor:
      for fornecedor in fornecedores:
        dados = fornecedor.split(' | ')
        if excluir_fornecedor == dados[0]:
          existe = True
          info = f'DESEJA EXCLUIR O(A) FORNECEDOR(A) "{excluir_fornecedor}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            fornecedores.remove(fornecedor)
            DaoFornecedor.alterar(fornecedores)
            system('cls')
            cprint(f'>> FORNECEDOR(A) "{excluir_fornecedor}" EXCLUIDO(A) COM SUCESSO\n', color='green')
          else:
            cprint('>> EXCLUSÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        cprint(f'>> O(A) FORNECEDOR(A) "{excluir_fornecedor}" NÃO EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

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
    system('cls')


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
          system('cls')
          cprint('>> DADOS INVÁLIDOS\n', color='light_red')
        info = f'DESEJA CADASTRAR O(A) CLIENTE "{nome}"?'
        print('-' * len(info))
        cprint(info, color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        system('cls')
        if confirmar == 'S':
          DaoCliente.cadastrar(Cliente(nome, cpf, telefone, email, endereco))
          cprint('>> CLIENTE CADASTRADO COM SUCESSO\n', color='green')
        else:
          cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
      else:
        system('cls')
        cprint('>> CLIENTE JÁ EXISTE NO SISTEMA\n', color='yellow')      
    else:
      system('cls')

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
          if opcao == '1':
            nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_cliente}": ').upper()
            info = f'ALTERAR O NOME "{dados[0]}" PARA "{nome}"?'
            dados[0] = nome
          elif opcao == '2':
            cpf = input(f'DIGITE UM NOVO CPF PARA "{alterar_cliente}": ')
            info = f'ALTERAR O CPF "{dados[1]}" PARA "{cpf}"?'
            dados[1] = cpf
          elif opcao == '3':
            telefone = input(f'DIGITE UM NOVO TELEFONE PARA "{alterar_cliente}": ')
            info = f'ALTERAR O TELEFONE "{dados[2]}" PARA "{telefone}"?'
          elif opcao == '4':
            email = input(f'DIGITE UM NOVO EMAIL PARA "{alterar_cliente}": ')
            info = f'ALTERAR O EMAIL "{dados[3]}" PARA "{email}"?'
            dados[3] = email
          elif opcao == '5':
            endereco = input(f'DIGITE UM NOVO ENDEREÇO PARA "{alterar_cliente}": ').upper()
            info = f'ALTERAR O ENDEREÇO "{dados[4]}" PARA "{endereco}"?'
            dados[4] = endereco
        print('-' * len(info))
        cprint(info, color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        system('cls')
        if confirmar == 'S':
          clientes.remove(cliente)
          DaoCliente.alterar(clientes)
          DaoCliente.cadastrar(Cliente(dados[0], dados[1], dados[2], dados[3], dados[4]))
          cprint('>> CLIENTE ALTERADO COM SUCESSO\n', color='green')
        else:
          cprint('>> ALTERAÇÃO NÃO CONFIRMADA\n', color='light_red')
        break
      if not existe:
        system('cls')
        cprint(f'>> O(A) CLIENTE "{alterar_cliente}" NÃO EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def excluir_cliente(cls):
    existe = False
    clientes = DaoCliente.clientes()
    clientes.pop()
    cprint('QUAL CLIENTE VOCÊ DESEJA EXCLUIR?', color='yellow')
    excluir_cliente = input('CLIENTE: ').upper()
    if excluir_cliente:
      for cliente in clientes:
        dados = cliente.split(' | ')
        if excluir_cliente == dados[0]:
          existe = True
          info = f'DESEJA EXCLUIR O(A) CLIENTE "{excluir_cliente}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            clientes.remove(cliente)
            DaoCliente.alterar(clientes)
            cprint('>> CLIENTE EXCLUIDO COM SUCESSO\n', color='green')
          else:
            cprint('>> EXCLUSÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        cprint(f'>> O(A) CLIENTE "{excluir_cliente}" NÃO EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

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
    system('cls')


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
        id = input(f'DIGITE UM ID PARA {nome}: ')
        cpf = input(f'DIGITE O CPF DE {nome}: ')
        telefone = input(f'DIGITE O TELEFONE DE {nome}: ')
        email = input(f'DIGITE O EMAIL De {nome} ')
        endereco = input(f'DIGITE O ENDEREÇO DE {nome}: ').upper()
        info = f'DESEJA CADASTRAR O(A) FUNCIONÁRIO(A) "{nome}"?'
        print('-' * len(info))
        cprint(info, color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        system('cls')
        if confirmar == 'S':
          DaoFuncionario.cadastrar(Funcionario(id, nome, cpf, telefone, email, endereco))
          cprint('>> FUNCIONÁRIO(A) CADASTRADO(A) COM SUCESSO\n', color='green')
        else:
          cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
      else:
        system('cls')
        cprint('>> FUNCIONÁRIO(A) JÁ EXISTE NO SISTEMA\n', color='yellow') 
    else:
      system('cls')

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
          if opcao == '1':
            id = input(f'DIGITE UM NOVO ID PARA "{alterar_funcionario}": ').upper()
            info = f'ALTERAR O ID "{dados[0]}" PARA "{id}"?'
            dados[0] = id
          if opcao == '2':
            nome = input(f'DIGITE UM NOVO NOME PARA "{alterar_funcionario}": ').upper()
            info = f'ALTERAR O NOME "{dados[1]}" PARA "{nome}"?'
            dados[1] = nome
          elif opcao == '3':
            cpf = input(f'DIGITE UM NOVO CPF PARA "{alterar_funcionario}": ')
            info = f'ALTERAR O CPF "{dados[2]}" PARA "{cpf}"?'
            dados[2] = cpf
          elif opcao == '4':
            telefone = input(f'DIGITE UM NOVO TELEFONE PARA "{alterar_funcionario}": ')
            info = f'ALTERAR O TELEFONE "{dados[3]}" PARA "{telefone}"?'
            dados[3] = telefone
          elif opcao == '5':
            email = input(f'DIGITE UM NOVO EMAIL PARA "{alterar_funcionario}": ')
            info = f'ALTERAR O EMAIL "{dados[4]}" PARA "{email}"?'
            dados[4] = email
          elif opcao == '6':
            endereco = input(f'DIGITE UM NOVO ENDEREÇO PARA "{alterar_funcionario}": ').upper()
            info = f'ALTERAR O ENDEREÇO "{dados[5]}" PARA "{endereco}"?'
            dados[5] = endereco
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            funcionarios.remove(funcionario)
            DaoFuncionario.alterar(funcionarios)
            DaoFuncionario.cadastrar(Funcionario(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]))
            cprint('>> FUNCIONÁRIO(A) ALTERADO(A) COM SUCESSO\n', color='green')
          else:
            system('cls')
            cprint('>> ALTERAÇÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        system('cls')
        cprint(f'>> O(A) FUNCIONÁRIO(A) "{alterar_funcionario}" NÃO EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def excluir_funcionario(cls):
    existe = False
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    cprint('QUAL FUNCIONÁRIO(A) VOCÊ DESEJA EXCLUIR?', color='yellow')
    excluir_funcionario = input('FUNCIONÁRIO(A): ').upper()
    
    if excluir_funcionario:
      for funcionario in funcionarios:
        dados = funcionario.split(' | ')
        if excluir_funcionario == dados[1]:
          existe = True
          info = f'DESEJA EXCLUIR O(A) FUNCIONÁRIO(A) "{excluir_funcionario}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            funcionarios.remove(funcionario)
            DaoFuncionario.alterar(funcionarios)
            cprint('>> FUNCIONÁRIO(A) EXCLUIDO(A) COM SUCESSO\n', color='green')
          else:
            cprint('>> EXCLUSÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        cprint(f'>> O(A) FUNCIONÁRIO(A) "{excluir_funcionario}" NÃO EXISTE NO SISTEMA\n', color='yellow')
    else:
      system('cls')

  @classmethod
  def ver_funcionarios(cls):
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    funcionarios.sort()
    system('cls')
    print('-'*130)
    cprint(f'{"ID":6} {"fUNCIONÁRIO(A)":20} {"CPF":20} {"TELEFONE":15} {"EMAIL":25} ENDEREÇO', color='yellow')
    print('-'*130)
    for funcionario in funcionarios:
      dados = funcionario.split(' | ')
      print(f'{dados[0]:6} {dados[1]:20} {dados[2]:20} {dados[3]:15} {dados[4]:25} {dados[5]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    system('cls')


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
          except:
            system('cls')
            cprint('>> DADOS INVÁLIDOS\n', color='light_red')
            break
          info = f'DESEJA ACRESCENTAR {qtd} UNIDADE(S) AO PRODUTO "{add_produto}"?'
          print('-' * len(info))
          cprint(info, color='yellow')
          confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
          system('cls')
          if confirmar == 'S':
            qtd += int(prod_existente[1])
            estoque.remove(produto)
            DaoProduto.alterar(estoque)
            DaoProduto.cadastrar(Produto(add_produto, qtd, prod_existente[2], prod_existente[3]))
            cprint(f'>> "{add_produto}" ACRESCENTADO COM SUCESSO\n', color='green')
          else:
            cprint('>> ADIÇÃO NÃO CONFIRMADA\n', color='light_red')
          break
      if not existe:
        info = f'NÃO TEM "{add_produto}" NO ESTOQUE, DESEJA CADASTRA-LO?'
        print('-' * len(info))
        cprint(info, color='yellow')
        confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
        system('cls')
        if confirmar == 'S':
          ControllerProduto.cadastrar_produto()
        else:
            cprint('>> CADASTRO NÃO CONFIRMADO\n', color='light_red')
    else:
      system('cls')

  @classmethod
  def ver_estoque(cls):
    estoque = DaoProduto.estoque()
    estoque.pop()
    estoque.sort()
    system('cls')
    print('-' * 65)
    cprint(f'{"PRODUTO":25} {"QTD":10}  {"PREÇO":10}   CATEGORIA', color='yellow')
    print('-' * 65)
    for produto in estoque:
      dados = produto.split(' | ')
      print(f'{dados[0]:25} {dados[1]:10} R${dados[2].replace('.', ','):10} {dados[3]}')
    input('\n\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    system('cls')


class ControllerVendas:
  
  @classmethod
  def vender(cls):
    estoque = DaoProduto.estoque()
    estoque.pop()
    clientes = DaoCliente.clientes()
    clientes.pop()
    funcionarios = DaoFuncionario.funcionarios()
    funcionarios.pop()
    relatorio = DaoRelatorios.relatorio()
    data_hora = datetime.now()
    data = data_hora.strftime('%d/%m/%Y')
    hora = data_hora.strftime('%H:%M')
    msg = 0
    id_venda = 0
    total_itens = 0
    total_pagar = 0
    total_volumes = 0
    lista_compras = []
    relatorio_venda = []
    estoque_baixo = 2
    slogan = lambda: cprint(f'{"MERCEARIA PYTHONFULL":^65}\n', color='light_blue')
    
    def lista():
      slogan()
      cprint(f'{"QTD":^5}{"PRODUTO":^32}{"VALOR":^14}{"V.TOTAL":^14}', color='yellow')
      print('-' * 65)
      for produto in lista_compras:
        print(f'|{produto[0]:>3}| {produto[1]:30}| R${produto[2]:10}| R${produto[3]:10}|')
      print('-' * 65)
      cprint(f'{total_itens:>5} {"ITEM(S)":<8}{total_volumes:>5} {"VOLUME(S)":<12}{"TOTAL À PAGAR:":>19} R${total_pagar:<10.2f}', color='yellow')

    while True:
      atualizar_qtd = 0
      existe = False
      system('cls')
      lista()
      # mensagens:
      if msg == 0:
        cprint(f'\n>> INICIANDO O REGISTRO DE COMPRAS\n\n', color='light_blue')
      elif msg == 1:
        cprint(f'\n>> "{item}" ADICIONADO(A) A COMPRA\n\n', color='green')
      elif msg == 2:
        cprint('\n>> DADOS INVÁLIDOS\n\n', color='light_red')
      elif msg == 3:
        cprint(f'\n>> "{item}" NÃO EXISTENTE NO ESTOQUE!\n\n', color='light_red')
      elif msg == 4:
        cprint(f'\n>> SÓ TEM {dados[1]} UNIDADES DE {dados[0]} NO ESTOQUE!\n\n', color='light_red')
      elif msg == 5:
        cprint(f'\n>> O ESTOQUE DE {dados[0]} ESTÁ ZERADO!\n\n', color='light_red')
      if estoque_baixo == 1:
        cprint(f'>> {dados[0]} VAI FICAR ABAIXO DE 10 UNIDADES NO ESTOQUE!\n\n', color='light_red')
      if estoque_baixo == 0:
        cprint(f'>> {dados[0]} VAI FICAR ZERADO NO ESTOQUE!\n\n', color='light_red')

      print('DIGITE "0" EM PRODUTO PARA ENCERRAR!\n')
      item = input('PRODUTO: ').upper()
      if item == '0':
        break
      for produto in estoque:
        dados = produto.split(' | ')
        if item == dados[0]:
          existe = True
          if int(dados[1]) == 0:
            msg = 5
            break
          try:
            qtd = int(input(f'QUANTIDADE DE {item}(S): '))
            atualizar_qtd = int(dados[1]) - qtd
            
            if atualizar_qtd < 0:
              msg = 4
              break
            elif atualizar_qtd == 0:
              estoque_baixo = 0
            elif atualizar_qtd < 10:
              estoque_baixo = 1
            total = f'{float(dados[2].replace(',', '.')) * qtd:.2f}'.replace('.', ',')
            total_itens += 1
            total_volumes += qtd
            total_pagar += float(total.replace(',', '.'))
            lista_compras.append([qtd, item, dados[2], total])
            relatorio_venda.append([qtd, item, dados[2], dados[3]])
            estoque.remove(produto)
            estoque.append(f'{dados[0]} | {atualizar_qtd} | {dados[2]} | {dados[3]}')
            msg = 1
            break      
          except ValueError:
            msg = 2
      if not existe:
          msg = 3
    if lista_compras:
      while True:
        cliente_existe = False
        funcionario_existe = False
        system('cls')
        lista()
        print('\n')
        cpf_cliente = input('INFORME O CPF DO CLIENTE OU DIGITE "0" PARA CONSUMIDOR: ')
        if cpf_cliente:
          if cpf_cliente == '0':
            consumidor = 'CONSUMIDOR'
            cliente_existe = True
          else:
            for cliente in clientes:
              dados_cliente = cliente.split(' | ')
              if cpf_cliente == dados_cliente[1]:
                cliente_existe = True
                consumidor = dados_cliente[0]
                break
          if cliente_existe:
            id_funcionario = input('INFORME O ID DO VENDEDOR: ')
            for funcionario in funcionarios:
              dados_funcionario = funcionario.split(' | ')
              if id_funcionario == dados_funcionario[0]:
                funcionario_existe = True
                break
            if not funcionario_existe:
              cprint('FUNCIONÁRIO NÃO CADASTRADO!\n')
          else:
            info = (f'CLIENTE NÃO CADASTRADO!...DESEJA CADASTRAR CLIENTE?')
            print('-' * len(info))
            cprint(info, color='yellow')
            confirmar = input('DIGITE "s" PARA CONFIRMAR: ').upper()
            system('cls')
            if confirmar == 'S':
              ControllerCliente.cadastrar_cliente()
        else:
          system('cls')
        if cliente_existe and funcionario_existe:
          system('cls')
          slogan()
          cprint(f'COMPRA ENCERRADA NO VALOR DE R${total_pagar:.2f}'.replace('.', ','), color='green')
          print('-' * 45)
          if cpf_cliente == '0':
            print(f'CLIENTE: {consumidor}\n')
          else:
            print(f'CLIENTE: {dados_cliente[0]}\n'
                  f'CPF: {dados_cliente[1]}\n'
                  f'ENDEREÇO: {dados_cliente[4]}\n')
          print(f'VENDEDOR: {dados_funcionario[1]}\n'
                f'CPF: {dados_funcionario[2]}\n'
                f'ID: {dados_funcionario[0]}\n')
          print(f'Número da venda: {len(relatorio)}\n')
          print(f'DATA: {data}    HORA: {hora}\n')
          print('-' * 45)
          cprint(f'CONFIRMAR O PAGAMENTO NO VALOR DE R${total_pagar:.2f}'.replace('.', ','), color='yellow')
          confirmar = input('\nDIGITE "s" PARA CONFIRMAR OU "n" PARA SAIR: ').upper()
          system('cls')
          if confirmar == 'S':
            slogan()
            cprint('PAGAMENTO CONFIRMADO!...\nAGRADECEMOS A PREFERÊNCIA...\nVOLTE SEMPRE...:)', color='light_green')
            id_venda = len(relatorio)
            DaoVendas.venda(relatorio_venda, id_venda, consumidor, dados_funcionario[1], total_pagar, data, hora)
            DaoProduto.alterar(estoque)
            input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
            system('cls')
            break
          elif confirmar == 'N':
            cprint('COMPRA CANCELADA!', color='light_red')
            input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
            system('cls')
            break
    else:
      system('cls')

  @classmethod
  def cancelar_venda(cls, opcao):
    relatorio = DaoRelatorios.relatorio()
    relatorio.pop()

    if opcao == '1':
      cprint('DIGITE O NÚMERO DA VENDA!', color='yellow')
      try:
        id_venda = int(input('NÚMERO DA VENDA: '))
        system('cls')
        for venda in relatorio:
          venda = eval(venda)
          if id_venda == venda['id_venda']:
            cprint(f'DESEJA REALMENTE EXCLUIR ESSA VENDA?\nESSA OPERAÇÃO NÃO PODE SER DESFEITA!', color='yellow')
            confirmar = input('\nDIGITE "s" ').upper()
            system('cls')
            if confirmar == 'S':
              pass
              # decidir se vai voltar os itens para o estoque:

              # relatorio.remove(venda)
              # DaoVendas.cancelar_venda(relatorio)

      except:
        pass

        


      




class ControllerRelatorios:
  
  def imprimir(venda):
    print('-' * 60)
    cprint(f'{"QTD":^5}{"PRODUTO":<32}{"VALOR":<14}{"V.TOTAL":<14}', color='yellow')
    print('-' * 60)
    for produto in venda['vendas']:
      total_venda = float(str(produto[2]).replace(',', '.'))*int(produto[0])
      print(f'{produto[0]:^5}{produto[1]:<32}R${produto[2]:<12}R${total_venda:.2f}'.replace('.', ','))
    print('-' * 60)
    cprint(f'{"TOTAL PAGO:":>50} R${venda['valor_pago']:.2f}'.replace('.', ','), color='yellow')
    print(f'CLIENTE: {venda['cliente']}')
    print(f'VENDEDOR: {venda['vendedor']}\n')
    cprint('*' * 60, color='light_blue')
    return float(f'{venda['valor_pago']}'.replace(',', '.'))

  @classmethod
  def venda(cls, opcao):
    relatorio = DaoRelatorios.relatorio()
    relatorio.pop()
    total_vendido = 0
    existe = False
    
    if opcao == '1':
      cprint('DIGITE O NÚMERO DA VENDA!', color='yellow')
      try:
        id_venda = int(input('NÚMERO DA VENDA: '))
        system('cls')
        for venda in relatorio:
          venda = eval(venda)
          if id_venda == venda['id_venda']:
            existe = True
            total_vendido = ControllerRelatorios.imprimir(venda)
            cprint(f'DATA DA VENDA: {venda['data']}', color='light_green')
            cprint(f'NÚMERO DA VENDA: {venda['id_venda']}', color='light_green')
            cprint(f'TOTAL VENDIDO: R${total_vendido:.2f}'.replace('.', ','), color='light_green')
            input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
            system('cls')
            break
        if not existe:
          system('cls')
          cprint(f'>> A VENDA NÚMERO {id_venda} NÃO CONSTA NO RELATÓRIO\n\n', color='light_red')
      except:
        system('cls')
        cprint('>> ID INVÁLIDO\n', color='light_red')
      
    elif opcao == '2':
      ultima_venda = relatorio[len(relatorio)-1]
      venda = eval(ultima_venda)
      total_vendido = ControllerRelatorios.imprimir(venda)
      cprint(f'DATA DA VENDA: {venda['data']}', color='light_green')
      cprint(f'NÚMERO DA VENDA: {venda['id_venda']}', color='light_green')
      cprint(f'TOTAL VENDIDO: R${total_vendido:.2f}'.replace('.', ','), color='light_green')
      input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
      system('cls')

  @classmethod
  def diario(cls):
    relatorio = DaoRelatorios.relatorio()
    relatorio.pop()
    existe = False
    num = 0
    total_vendido = 0

    try:
      cprint('DIGITE A DATA PARA BUSCAR O RELATÓRIO!', color='yellow')
      dia = input('DIA(dd): ')
      mes = input('MÊS(mm): ')
      ano = input('ANO(aaaa): ')
      data = f'{dia}/{mes}/{ano}'
      system('cls')

      for venda in relatorio:
        venda = eval(venda)
        if data == venda['data']:
          existe = True
          num += 1
          cprint(f'ID DA VENDA: {venda['id_venda']}', color='yellow')
          total_vendido += ControllerRelatorios.imprimir(venda)
      if existe:
        cprint(f'DATA DAS VENDAS: {data}', color='light_green')
        cprint(f'NÚMERO DE VENDAS: {num}', color='light_green')
        cprint(f'TOTAL VENDIDO NO DIA: R${total_vendido:.2f}'.replace('.', ','), color='light_green')
        print('RELATÓRIO DIÁRIO')
        input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
        system('cls')
      else:
        system('cls')
        cprint(f'>> NÃO CONSTA VENDAS NO DIA {data}\n\n', color='light_red')
    except:
      system('cls')
      cprint('>> DADOS INVÁLIDOS\n', color='light_red')
    
  @classmethod
  def mensal(cls):
    relatorio = DaoRelatorios.relatorio()
    relatorio.pop()
    existe = False
    num = 0
    total_vendido = 0

    try:
      cprint('DIGITE O MÊS PARA BUSCAR O RELATÓRIO!', color='yellow')
      mes = input('MÊS(mm): ')
      ano = input('ANO(aaaa): ')
      data = f'{mes}/{ano}'
      system('cls')

      for venda in relatorio:
        venda = eval(venda)
        i = venda['data'].split('/')
        if i[1] == mes and i[2] == ano:
          existe = True
          num += 1
          cprint(f'ID DA VENDA: {venda['id_venda']}', color='yellow')
          total_vendido += ControllerRelatorios.imprimir(venda)
      if existe:
        cprint(f'MÊS DAS VENDAS: {data}', color='light_green')
        cprint(f'NÚMERO DE VENDAS: {num}', color='light_green')
        cprint(f'TOTAL VENDIDO NO MÊS: R${total_vendido:.2f}'.replace('.', ','), color='light_green')
        print('RELATÓRIO MENSAL')
        input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
        system('cls')
      else:
        system('cls')
        cprint(f'>> NÃO CONSTA VENDAS NO DIA {data}\n\n', color='light_red')
    except:
      system('cls')
      cprint('>> DADOS INVÁLIDOS\n', color='light_red')

  @classmethod
  def geral(cls):
    relatorio = DaoRelatorios.relatorio()
    relatorio.pop()
    existe = False
    num = 0
    total_vendido = 0

    for venda in relatorio:
      venda = eval(venda)
      num += 1
      cprint(f'ID DA VENDA: {venda['id_venda']}', color='yellow')
      total_vendido += ControllerRelatorios.imprimir(venda)
    cprint(f'NÚMERO DE VENDAS: {num}', color='light_green')
    cprint(f'TOTAL VENDIDO: R${total_vendido:.2f}'.replace('.', ','), color='light_green')
    print('RELATÓRIO GERAL')
    input('\nPRESSIONE "ENTER" PARA CONTINUAR...')
    system('cls')
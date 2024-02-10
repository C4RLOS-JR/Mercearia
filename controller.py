import os
from dao import DaoCategoria, DaoProduto
from model import Categoria, Fornecedor, Produto


class ControllerCategoria:

  @classmethod
  def cadastrar_categoria(cls,):
    existe = False
    ver_categorias = DaoCategoria.ver()

    os.system('cls')
    nova_categoria = input('DIGITE O NOME DA CATEGORIA: ').upper()
    for categoria in ver_categorias:
      if categoria == nova_categoria:
        existe = True

    if not existe:
      DaoCategoria.adicionar(nova_categoria)
      os.system('cls')
      print(f'→ CATEGORIA "{nova_categoria}" CADASTRADA COM SUCESSO... \n')
    else:
      os.system('cls')
      print('→ ESSA CATEGORIA JÁ EXISTE... ←\n')

  @classmethod
  def excluir_categoria(cls):
    existe = False
    lista_categorias = DaoCategoria.ver()

    os.system('cls')
    categoria_excluir = input('QUAL CATEGORIA VOCÊ DESEJA EXCLUIR?\n\nCATEGORIA: ').upper()
    for categoria in lista_categorias:
      if categoria == categoria_excluir:
        lista_categorias.remove(categoria)
        existe = True
    if existe:
      DaoCategoria.alterar(lista_categorias)
      os.system('cls')
      print('→ CATEGORIA REMOVIDA...\n')
    else:
      os.system('cls')
      return print(f'→ NÃO EXISTE A CATEGORIA "{categoria_excluir}"...\n')
    
  @classmethod
  def alterar_categoria(cls):
    lista_categorias = DaoCategoria.ver()
    os.system('cls')
    categoria_excluir = input('QUAL CATEGORIA VOCÊ DESEJA ALTERAR?\n\nCATEGORIA: ').upper()
    if categoria_excluir in lista_categorias:
      os.system('cls')
      categoria_add = input(f'ALTERAR "{categoria_excluir}" POR QUAL CATEGORIA?\n\nCATEGORIA: ').upper()
      if categoria_add not in lista_categorias:
        for categoria in lista_categorias: 
          if categoria == categoria_excluir:
            lista_categorias.remove(categoria)
            DaoCategoria.alterar(lista_categorias)
            DaoCategoria.adicionar(categoria_add)
            os.system('cls')
            print(f'→ CATEGORIA "{categoria_excluir}" ALTERADA PARA "{categoria_add}"...\n')
      else:
        os.system('cls')
        print(f'→ JÁ EXISTE A CATEGORIA "{categoria_add}"...\n')
    else:
       os.system('cls')
       print(f'→ NÃO EXISTE A CATEGORIA "{categoria_excluir}"...\n')
  
  @classmethod
  def ver_categorias(cls):
    ver_categorias = DaoCategoria.ver()
    ver_categorias.sort()

    os.system('cls')
    print('LISTA DE CATEGORIAS:')
    print('--------------------')
    for categoria in ver_categorias:
      print(categoria)
    input('\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')


class ControllerProduto():

  @classmethod
  def cadastrar_produto(cls):
    os.system('cls')
    produto = input('DIGITE O PRODUTO: ').upper()
    preco = float(input(f'DIGITE O PREÇO DO(A) {produto}: ').replace(',', '.'))
    qtd = int(input(f'DIGITE A QUANTIDADE DE {produto}: '))
    categoria = input(f'DIGITE A CATEGORIA DO(A) {produto}: ').upper()
    os.system('cls')

    existe_cat = False
    cadastrar_cat = False
    ver_categorias = DaoCategoria.ver()
    
    for cat_existente in ver_categorias:
      if categoria == cat_existente:
        existe_cat = True
    if not existe_cat:
      criar = input(f'A CATEGORIA "{categoria}" NÃO EXISTE, DESEJA CRIA-LA?\nDIGITE "s" PARA CONFIRMAR: ')
      os.system('cls')
      if criar == 's':
        cadastrar_cat = True
        DaoCategoria.adicionar(categoria)
        os.system('cls')
        print(f'→ CATEGORIA "{categoria}" CRIADA COM SUCESSO... \n')
    if existe_cat == True or cadastrar_cat == True:
      DaoProduto.adicionar(categoria, Produto(produto, qtd, preco))
      os.system('cls')
      print(f'"{produto}" CADASTRADO COM SUCESSO...')

  @classmethod
  def add_estoque(cls):
    os.system('cls')
    produto = input('DIGITE O PRODUTO: ').upper()

    estoque = DaoProduto.estoque()
    estoque.pop()

    for i in estoque:
      prod_existente = i.split(' | ')
      if prod_existente[0] == produto:
        qtd = int(input(f'DIGITE A QUANTIDADE DE {produto}: '))
        qtd += int(prod_existente[1])
        estoque.remove(i)
        DaoProduto.alterar(estoque)
        DaoProduto.adicionar(prod_existente[3], Produto(produto, qtd, prod_existente[2]))
        os.system('cls')
        print(f'{produto} ADICIONADO(A) COM SUCESSO...')
      else:
        os.system('cls')
        add = input(f'NÃO TEM "{produto}" NO ESTOQUE, DESEJA ADICIONA-LO?\nDIGITE "s" PARA CONFIRMAR: ')
        os.system('cls')
        if add == 's':
          ControllerProduto.cadastrar_produto()
          
  @classmethod
  def alterar_produto(cls):
    estoque = DaoProduto.estoque()
    os.system('cls')
    produto_excluir = input('QUAL PRODUTO VOCÊ DESEJA ALTERAR?\nPRODUTO: ').upper()
    for i in estoque:
      produto = i.split(' | ')
      if produto_excluir == produto[0]:
        estoque.remove(i)
        estoque.pop()
        DaoProduto.alterar(estoque)
        ControllerProduto.cadastrar_produto()

  @classmethod
  def ver_estoque(cls):
    estoque = DaoProduto.estoque()
    estoque.pop()
    estoque.sort()
    os.system('cls')
    print('---------------------------------------------------------------')
    print(f'{"PRODUTO":25} {"QTD":10}  {"PREÇO":10}   CATEGORIA')
    print('---------------------------------------------------------------')
    for i in estoque:
      produto = i.split(' | ')
      print(f'{produto[0]:25} {produto[1]:10} R$ {produto[2]:10} {produto[3]}')
    input('\nPRESSIONE "ENTER" PARA VOLTAR AO MENU...')
    os.system('cls')
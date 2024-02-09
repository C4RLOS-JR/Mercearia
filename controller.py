import os
from dao import DaoCategoria, DaoProduto
from model import Categoria, Fornecedor, Produto


class ControllerCategoria:

  @classmethod
  def cadastrar_categoria(cls,):
    existe = False
    ver_categorias = DaoCategoria.ver()

    os.system('cls')
    nova_categoria = input('Digite o nome da categoria: ').upper()
    for categoria in ver_categorias:
      if categoria == nova_categoria:
        existe = True

    if not existe:
      DaoCategoria.adicionar(nova_categoria)
      os.system('cls')
      print('→ Categoria cadastrada com sucesso... \n')
    else:
      os.system('cls')
      print('→ Essa categoria já existe... ←\n')

  @classmethod
  def excluir_categoria(cls):
    existe = False
    lista_categorias = DaoCategoria.ver()

    os.system('cls')
    categoria_excluir = input('Qual categoria você deseja excluir?\n\nCategoria: ').upper()
    for categoria in lista_categorias:
      if categoria == categoria_excluir:
        lista_categorias.remove(categoria)
        existe = True
    if existe:
      DaoCategoria.alterar(lista_categorias)
      os.system('cls')
      print('→ Categoria removida...\n')
    else:
      os.system('cls')
      return print(f'→ Não existe a categoria {categoria_excluir}...\n')
    
  @classmethod
  def alterar_categoria(cls):
    lista_categorias = DaoCategoria.ver()
    os.system('cls')
    categoria_excluir = input('Qual categoria você deseja alterar?\n\nCategoria: ').upper()
    if categoria_excluir in lista_categorias:
      os.system('cls')
      categoria_add = input(f'Alterar "{categoria_excluir}" por qual categoria?\n\nCategoria: ').upper()
      if categoria_add not in lista_categorias:
        for categoria in lista_categorias: 
          if categoria == categoria_excluir:
            lista_categorias.remove(categoria)
            DaoCategoria.alterar(lista_categorias)
            DaoCategoria.adicionar(categoria_add)
            os.system('cls')
            print(f'→ Categoria "{categoria_excluir}" alterada para "{categoria_add}"...\n')
      else:
        os.system('cls')
        print(f'→ Já existe a categoria {categoria_add}...\n')
    else:
       os.system('cls')
       print(f'→ Não existe a categoria {categoria_excluir}...\n')
  
  @classmethod
  def ver_categorias(cls):
    ver_categorias = DaoCategoria.ver()
    ver_categorias.sort()
    os.system('cls')
    print('Lista de categorias:\n')
    for categoria in ver_categorias:
      print(categoria)
    input('\nPressione "enter" para voltar para o menu...')
    os.system('cls')


class ControllerProduto():

  @classmethod
  def cadastrar_produto(cls):
    os.system('cls')
    produto = input('Digite o produto: ').upper()
    preco = float(input(f'Digite o preço do(a) {produto}: '))
    qtd = int(input(f'Digite a quantidade de {produto}: '))
    categoria = input(f'Digite a categoria do(a) {produto}: ').upper()

    os.system('cls')

    DaoProduto.adicionar(categoria, Produto(produto, qtd, preco))
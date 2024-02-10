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
      print(f'→ Categoria "{nova_categoria}" cadastrada com sucesso... \n')
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

    existe_cat = False
    cadastrar_cat = False
    ver_categorias = DaoCategoria.ver()
    
    for cat_existente in ver_categorias:
      if categoria == cat_existente:
        existe_cat = True
    if not existe_cat:
      criar = input(f'A categoria "{categoria}" não existe, deseja cria-la?\nDigite "s" para confirmar: ')
      os.system('cls')
      if criar == 's':
        cadastrar_cat = True
        DaoCategoria.adicionar(categoria)
        os.system('cls')
        print(f'→ Categoria "{categoria}" cadastrada com sucesso... \n')
    if existe_cat == True or cadastrar_cat == True:
      DaoProduto.adicionar(categoria, Produto(produto, qtd, preco))
      os.system('cls')
      print(f'"{produto}" cadastrado com sucesso...')



  @classmethod
  def add_estoque(cls):
    os.system('cls')
    ControllerProduto.ver_estoque()
    produto = input('Digite o produto: ').upper()

    estoque = DaoProduto.estoque()
    estoque.pop()

    for i in estoque:
      prod_existente = i.split(' | ')
      if prod_existente[0] == produto:
        qtd = int(input(f'Digite a quantidade de {produto}: '))
        qtd += int(prod_existente[1])
        estoque.remove(i)
        DaoProduto.alterar(estoque)
        DaoProduto.adicionar(prod_existente[3], Produto(produto, qtd, prod_existente[2]))
        os.system('cls')
        print(f'{produto} adicionado(a) ao estoque...')
      else:
        os.system('cls')
        add = input(f'Não tem "{produto}" no estoque, deseja adiciona-lo?\nDigite "s" para confirmar: ')
        os.system('cls')
        if add == 's':
          ControllerProduto.cadastrar_produto()
          

    


  @classmethod
  def alterar_produto(cls):
    estoque = DaoProduto.estoque()
    os.system('cls')
    produto_excluir = input('Qual produto deseja alterar?\nProduto: ').upper()
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
    for i in estoque:
      produto = i.split(' | ')
      print(f'Produto: {produto[0]:15} Qtd: {produto[1]:10} R$ {produto[2]:10} Categoria: {produto[3]}')
    input('\nPressione "enter" para voltar para o menu...')
    os.system('cls')
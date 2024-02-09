import os
from dao import DaoCategoria
from model import Categoria, Fornecedor, Produto


class ControllerCategoria:

  @classmethod
  def cadastrar_categoria(cls,nova_categoria):
    existe = False
    ver_categorias = DaoCategoria.ver()
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
  def excluir_categoria(cls, categoria_remover):
    existe = False
    lista_categorias = DaoCategoria.ver()
    for categoria in lista_categorias:
      if categoria == categoria_remover:
        lista_categorias.remove(categoria)
        existe = True
    if existe:
      DaoCategoria.remover(lista_categorias)
      os.system('cls')
      print('→ Categoria removida...\n')
    else:
      os.system('cls')
      return print('→ Não existe essa categoria...\n')
    
  @classmethod
  def alterar_categoria(cls, categoria_excluir, cadegoria_add):
    existe = False
    lista_categorias = DaoCategoria.ver()
    for categoria in lista_categorias:
      if categoria == categoria_excluir:
        lista_categorias.remove(categoria)
        DaoCategoria.remover(lista_categorias)
        DaoCategoria.adicionar(cadegoria_add)
        existe = True
    if existe:
      os.system('cls')
      print('→ Categoria alterada...\n')
    else:
      os.system('cls')
      return print('→ Não existe essa categoria...\n')
  
  
  
  @classmethod
  def ver_categorias(cls):
    ver_categorias = DaoCategoria.ver()
    ver_categorias.sort()
    for categoria in ver_categorias:
      print(categoria)
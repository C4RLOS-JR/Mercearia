import os
from dao import DaoCategoria
from model import Categoria, Fornecedor, Produto


class ControllerCategoria:

  @classmethod
  def cadastrar(cls,nova_categoria):
    existe = False
    ver_categorias = DaoCategoria.ver()
    for categoria in ver_categorias:
      if categoria == nova_categoria:
        existe = True

    if not existe:
      DaoCategoria.adicionar(nova_categoria)
      os.system('cls')
      print('→ Categoria cadastrada com sucesso ←\n')
    else:
      os.system('cls')
      print('→ Essa categoria já existe ←\n')




  @classmethod
  def remover(cls, remover_categoria):
    lista_categorias = DaoCategoria.ver()
    for categoria in lista_categorias:
      if categoria == remover_categoria:
        lista_categorias.remove(categoria)
    DaoCategoria.remover(lista_categorias)
      

  
  
  
  
  @classmethod
  def ver(cls):
    ver_categorias = DaoCategoria.ver()
    for categoria in ver_categorias:
      print(categoria)

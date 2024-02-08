import os
from dao import DaoCategoria
from model import Categoria, Fornecedor, Produto


class ControllerCategoria:
  @classmethod
  def cadastrar(cls,nova_categoria):
    existe = False
    categorias = DaoCategoria.ver()
    for categoria in categorias:
      if nova_categoria == categoria:
        existe = True

    if not existe:
      DaoCategoria.adicionar(nova_categoria)
      os.system('cls')
      print('→ Categoria cadastrada com sucesso ←\n')
    else:
      os.system('cls')
      print('→ Essa categoria já existe ←\n')

  @classmethod
  def ver(cls):
    lista = DaoCategoria.ver()
    for i in lista:
      print(i)

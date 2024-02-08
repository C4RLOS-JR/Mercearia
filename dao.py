

from model import Categoria


class DaoCategoria:
  
  @classmethod
  def adicionar(cls, categoria):
    with open('arquivos/categoria.txt', 'a') as arq:
      arq.write(categoria + '\n')

  @classmethod
  def remover(cls, nova_lista):
    with open('arquivos/categoria.txt', 'w') as arq:
      for categoria in nova_lista:
        arq.write(categoria + '\n')

  @classmethod
  def ver(cls):
    with open('arquivos/categoria.txt', 'r') as arq:
      return list(arq.read().split())
      
from model import Categoria, Produto


class DaoCategoria:
  
  @classmethod
  def adicionar(cls, categoria: Categoria):
    with open('arquivos/categoria.txt', 'a') as arq:
      arq.write(categoria + '\n')

  @classmethod
  def alterar(cls, nova_lista):
    with open('arquivos/categoria.txt', 'w') as arq:
      for categoria in nova_lista:
        arq.write(categoria + '\n')

  @classmethod
  def ver(cls):
    with open('arquivos/categoria.txt', 'r') as arq:
      return list(arq.read().split())
      

class DaoProduto:

  @classmethod
  def adicionar(cls, produto: Produto):
    pass
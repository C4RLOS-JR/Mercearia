from math import prod
from model import Categoria, Produto


class DaoCategoria:
  
  @classmethod
  def adicionar(cls, categoria: Categoria):
    with open('arquivos/categoria.txt', 'a') as arq:
      arq.write(f'{categoria}\n')

  @classmethod
  def alterar(cls, nova_lista):
    with open('arquivos/categoria.txt', 'w') as arq:
      for categoria in nova_lista:
        arq.write(f'{categoria}\n')

  @classmethod
  def ver(cls):
    with open('arquivos/categoria.txt', 'r') as arq:
      return list(arq.read().split())
      

class DaoProduto:

  @classmethod
  def adicionar(cls, categoria, produto: Produto):
    produto.categoria = categoria
    with open('arquivos/estoque.txt', 'a') as arq:
      arq.write(f'{produto.nome} | {produto.qtd} | {produto.preco} | {produto.categoria}\n')

  @classmethod
  def estoque(cls):
    with open('arquivos/estoque.txt', 'r') as arq:
      


      produtos = arq.read().split('\n')
      produtos.pop()
      #print(produtos)
      soma = 0
      for i in produtos:
        produto = i.split(' | ')
        soma += float(produto[1])
      #print(soma)
 
DaoProduto.estoque()
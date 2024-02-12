from math import prod
from model import Categoria, Fornecedor, Produto


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
  def alterar(cls, novo_estoque):
    with open('arquivos/estoque.txt', 'w') as arq:
      for produto in novo_estoque:
        arq.write(f'{produto}\n')

  @classmethod
  def estoque(cls):
    with open('arquivos/estoque.txt', 'r') as arq:
      return list(arq.read().split('\n'))


class DaoFornecedor:

  @classmethod
  def adicionar(cls, fornecedor: Fornecedor):
    with open('arquivos/fornecedor.txt', 'a') as arq:
      arq.write(f'{fornecedor.nome} | {fornecedor.cnpj} | {fornecedor.telefone}\n')

  @classmethod
  def fornecedores(cls):
    with open('arquivos/fornecedor.txt', 'r') as arq:
      return list(arq.read().split('\n'))
    
  @classmethod
  def alterar(cls, novo_fornecedor):
    with open('arquivos/fornecedor.txt', 'w') as arq:
      for fornecedor in novo_fornecedor:
        arq.write(f'{fornecedor}\n')
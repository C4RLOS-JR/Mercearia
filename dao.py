from math import prod
from model import Categoria, Cliente, Fornecedor, Funcionario, Produto


class DaoCategoria:
  
  @classmethod
  def adicionar(cls, categoria: Categoria):
    with open('arquivos/categoria.txt', 'a') as arq:
      arq.write(f'{categoria}\n')

  @classmethod
  def alterar(cls, categorias_alterada):
    with open('arquivos/categoria.txt', 'w') as arq:
      for categoria in categorias_alterada:
        arq.write(f'{categoria}\n')

  @classmethod
  def categorias(cls):
    with open('arquivos/categoria.txt', 'r') as arq:
      return list(arq.read().split())
      

class DaoProduto:

  @classmethod
  def adicionar(cls, categoria, produto: Produto):
    produto.categoria = categoria
    with open('arquivos/estoque.txt', 'a') as arq:
      arq.write(f'{produto.nome} | {produto.qtd} | {produto.preco} | {produto.categoria}\n')

  @classmethod
  def alterar(cls, estoque_alterado):
    with open('arquivos/estoque.txt', 'w') as arq:
      for produto in estoque_alterado:
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
  def alterar(cls, fornecedores_alterado):
    with open('arquivos/fornecedor.txt', 'w') as arq:
      for fornecedor in fornecedores_alterado:
        arq.write(f'{fornecedor}\n')

  @classmethod
  def fornecedores(cls):
    with open('arquivos/fornecedor.txt', 'r') as arq:
      return list(arq.read().split('\n'))


class DaoCliente:

  @classmethod
  def cadastrar(cls, cliente: Cliente):
    with open('arquivos/cliente.txt', 'a') as arq:
      arq.write(f'{cliente.nome} | {cliente.cpf} | {cliente.telefone} | {cliente.email} | {cliente.endereco}\n')
  
  @classmethod
  def alterar(cls, clientes_alterado):
    with open('arquivos/cliente.txt', 'w') as arq:
      for cliente in clientes_alterado:
        arq.write(f'{cliente}\n')
  
  @classmethod
  def clientes(cls):
    with open('arquivos/cliente.txt', 'r') as arq:
      return list(arq.read().split('\n'))
    

class DaoFuncionario:
  @classmethod
  def cadastrar(cls, funcionario:Funcionario):
    with open('arquivos/funcionarios.txt', 'a') as arq:
      arq.write(f'{funcionario.id} | {funcionario.nome} | {funcionario.cpf} | {funcionario.telefone} | {funcionario.email} | {funcionario.endereco}\n')

  @classmethod
  def alterar(cls, funcionarios_alterado):
    with open('arquivos/funcionarios.txt', 'w') as arq:
      for funcionario in funcionarios_alterado:
        arq.write(f'{funcionario}\n')

  @classmethod
  def funcionarios(cls):
    with open('arquivos/funcionarios.txt', 'r') as arq:
      return list(arq.read().split('\n'))
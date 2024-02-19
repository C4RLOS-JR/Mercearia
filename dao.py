from model import Categoria, Cliente, Fornecedor, Funcionario, Produto, Venda


class DaoCategoria:
  
  @classmethod
  def cadastrar(cls, categoria: Categoria):
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
  def cadastrar(cls, produto: Produto):
    with open('arquivos/estoque.txt', 'a') as arq:
      arq.write(f'{produto.nome} | {produto.qtd} | {produto.preco} | {produto.categoria}\n'.replace('.', ','))

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
  def cadastrar(cls, fornecedor: Fornecedor):
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
    

class DaoVendas:
  
  @classmethod
  def venda(cls, relatorio_venda, id_venda, cliente, funcionario, total_pagar, data, hora):
    venda = {'id_venda': id_venda, 'data': data, 'hora': hora, 'vendas': relatorio_venda, 'cliente': cliente, 'vendedor': funcionario, 'valor_pago': total_pagar}
    with open('arquivos/vendas.txt', 'a') as arq:
      arq.write(f'{venda}\n')

  @classmethod
  def cancelar_venda(cls): # Fazer 
    pass


class DaoRelatorios:

  @classmethod
  def relatorio(cls):
    with open('arquivos/vendas.txt', 'r') as arq:
      return list(arq.read().split('\n'))
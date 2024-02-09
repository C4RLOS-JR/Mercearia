class Categoria:
  def __init__(self, categoria):
    self.categoria = categoria


class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco


class Fornecedor:
  def __init__(self, fornecedor, cnpj, telefone):
    self.fornecedor = fornecedor
    self.cnpj = cnpj
    self.telefone = telefone


class Pessoa:
  def __init__(self, nome, telefone, cpf, email, endereco):
    self.nome = nome
    self.telefone = telefone
    self.cpf = cpf
    self.email = email
    self.endereco = endereco


class Cliente(Pessoa):
  def __init__(self, nome, telefone, cpf, email, endereco):
    super().__init__(nome, telefone, cpf, email, endereco)


class Funcionario(Pessoa):
  def __init__(self, id, nome, telefone, cpf, email, endereco):
    self.id = id
    super().__init__(nome, telefone, cpf, email, endereco)
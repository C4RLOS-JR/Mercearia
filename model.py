class Categoria:
  def __init__(self, categoria):
    self.categoria = categoria


class Produto(Categoria):
  def __init__(self, nome, qtd, preco):
    self.nome = nome
    self.qtd = qtd
    self.preco = preco


class Fornecedor:
  def __init__(self, nome, cnpj, telefone):
    self.nome = nome
    self.cnpj = cnpj
    self.telefone = telefone


class Pessoa:
  def __init__(self, nome, cpf, telefone, email, endereco):
    self.nome = nome
    self.cpf = cpf
    self.telefone = telefone
    self.email = email
    self.endereco = endereco


class Cliente(Pessoa):
  def __init__(self, nome, cpf, telefone, email, endereco):
    super().__init__(nome, cpf, telefone, email, endereco)


class Funcionario(Pessoa):
  def __init__(self, id, nome, cpf, telefone, email, endereco):
    self.id = id
    super().__init__(nome, cpf, telefone, email, endereco)
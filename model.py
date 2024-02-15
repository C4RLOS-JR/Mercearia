class Categoria:
  def __init__(self, categoria):
    self.categoria = categoria


class Produto(Categoria):
  def __init__(self, nome, qtd, preco, categoria):
    super().__init__(categoria)
    self.nome = nome
    self.qtd = qtd
    self.preco = preco


class Venda(Produto):
  def __init__(self, qtd, nome, preco, categoria, preco_total, total_itens, total_pagar):
    super().__init__(qtd, nome, preco, categoria)
    self.preco_total = preco_total
    self.total_itens = total_itens
    self.total_pagar = total_pagar

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
    super().__init__(nome, cpf, telefone, email, endereco)
    self.id = id
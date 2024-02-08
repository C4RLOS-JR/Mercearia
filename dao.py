

class DaoCategoria:
  
  @classmethod
  def adicionar(cls, categoria):
    with open('arquivos/categoria.txt', 'a') as arq:
      arq.write(categoria + '\n')

  @classmethod
  def ver(cls):
    with open('arquivos/categoria.txt', 'r') as arq:
      return list(arq.read().split())
      
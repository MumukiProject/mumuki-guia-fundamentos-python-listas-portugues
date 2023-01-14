livros = ["Ensaio sobre a Cegueira", "Socorro", "Meu Pé de Laranja Lima"]

def pronto():
  if "Fundação" in livros:
    return "Muito bem!"
  else:
    raise RuntimeError("Não se esqueça de adicionar 'Fundamentos' à lista de livros!")
  
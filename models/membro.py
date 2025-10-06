from models.livro import Livro

class Membro:
    '''Cria um membro da biblioteca. Registro de usuário da biblioteca'''
    def __init__(self, nome: str, numero_membro: int):
        """Representa um membro da biblioteca."""
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico = []  # lista de livros emprestados

    def adicionar_ao_historico(self, livro: Livro):
        """Adiciona um livro ao histórico do membro."""
        self.historico.append(livro.titulo)

    def __repr__(self):
        return f"<Membro: {self.nome} | ID: {self.numero_membro} | Histórico: {self.historico}>"
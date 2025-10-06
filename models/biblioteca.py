from models.livro import Livro
from models.membro import Membro

class Biblioteca:
    '''Cria a biblioteca dentro do sistema, permitindo o grenciamento dos membros e livros dentro do sistema.'''
    def __init__(self, nome: str):
        """Gerencia os livros e membros."""
        self.nome = nome
        self.catalogo = []   # lista de objetos Livro
        self.membros = []    # lista de objetos Membro

    # ---------------------- MÉTODOS DE CADASTRO ----------------------

    def adicionar_livro(self, livro: Livro):
        self.catalogo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao catálogo.")

    def registrar_membro(self, membro: Membro):
        self.membros.append(membro)
        print(f"Membro '{membro.nome}' registrado com sucesso.")

    # ---------------------- MÉTODOS DE OPERAÇÃO ----------------------

    def emprestar_livro(self, id_livro: int, numero_membro: int):
        """Empresta um livro a um membro, se disponível."""
        livro = next((l for l in self.catalogo if l.id_livro == id_livro), None)
        membro = next((m for m in self.membros if m.numero_membro == numero_membro), None)

        if not livro:
            print(f"Livro com ID {id_livro} não encontrado.")
            return
        if not membro:
            print(f"Membro com número {numero_membro} não encontrado.")
            return
        if not livro.disponivel:
            print(f"O livro '{livro.titulo}' já está emprestado.")
            return

        livro.emprestar()
        membro.adicionar_ao_historico(livro)

    def devolver_livro(self, id_livro: int):
        """Devolve um livro à biblioteca."""
        livro = next((l for l in self.catalogo if l.id_livro == id_livro), None)
        if not livro:
            print(f"Livro com ID {id_livro} não encontrado.")
            return
        livro.devolver()

    # ---------------------- MÉTODOS DE PESQUISA ----------------------

    def buscar_por_titulo(self, titulo: str):
        resultados = [l for l in self.catalogo if titulo.lower() in l.titulo.lower()]
        return resultados or f"Nenhum livro encontrado com o título '{titulo}'."

    def buscar_por_autor(self, autor: str):
        resultados = [l for l in self.catalogo if autor.lower() in l.autor.lower()]
        return resultados or f"Nenhum livro encontrado do autor '{autor}'."

    def buscar_por_id(self, id_livro: int):
        livro = next((l for l in self.catalogo if l.id_livro == id_livro), None)
        return livro or f"Nenhum livro encontrado com ID {id_livro}."

    # ---------------------- VISUALIZAÇÃO ----------------------

    def listar_livros(self):
        print("\nCatálogo de Livros:")
        for livro in self.catalogo:
            print(livro)

    def listar_membros(self):
        print("\nMembros Registrados:")
        for membro in self.membros:
            print(membro)

    def __repr__(self):
        return f"<Biblioteca: {self.nome} | Livros: {len(self.catalogo)} | Membros: {len(self.membros)}>"
class Livro:
    '''Cria um livro dentro do sistema.'''
    def __init__(self, titulo: str, autor: str, id_livro: int):
        """Representa um livro na biblioteca."""
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
        self.disponivel = True  # True = disponível | False = emprestado

    def emprestar(self):
        """Marca o livro como emprestado."""
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        """Marca o livro como disponível novamente."""
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já estava disponível.")

    def __repr__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"<Livro: {self.titulo} | Autor: {self.autor} | ID: {self.id_livro} | Status: {status}>"
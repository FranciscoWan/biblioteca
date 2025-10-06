from models.biblioteca import Biblioteca
from models.livro import Livro
from models.membro import Membro

def menu():
    print("\n📚 === Sistema de Gerenciamento de Biblioteca ===")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Membro")
    print("3. Listar Livros")
    print("4. Listar Membros")
    print("5. Emprestar Livro")
    print("6. Devolver Livro")
    print("7. Buscar Livro por Título")
    print("8. Buscar Livro por Autor")
    print("9. Buscar Livro por ID")
    print("0. Sair")
    return input("\nEscolha uma opção: ")

def main():
    biblioteca = Biblioteca("Biblioteca Central")

    while True:
        opcao = menu()

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            id_livro = int(input("ID do livro: "))
            biblioteca.adicionar_livro(Livro(titulo, autor, id_livro))

        elif opcao == "2":
            nome = input("Nome do membro: ")
            numero_membro = int(input("Número do membro: "))
            biblioteca.registrar_membro(Membro(nome, numero_membro))

        elif opcao == "3":
            biblioteca.listar_livros()

        elif opcao == "4":
            biblioteca.listar_membros()

        elif opcao == "5":
            id_livro = int(input("ID do livro a emprestar: "))
            numero_membro = int(input("Número do membro: "))
            biblioteca.emprestar_livro(id_livro, numero_membro)

        elif opcao == "6":
            id_livro = int(input("ID do livro a devolver: "))
            biblioteca.devolver_livro(id_livro)

        elif opcao == "7":
            titulo = input("Digite o título do livro: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            print(resultados)

        elif opcao == "8":
            autor = input("Digite o nome do autor: ")
            resultados = biblioteca.buscar_por_autor(autor)
            print(resultados)

        elif opcao == "9":
            id_livro = int(input("Digite o ID do livro: "))
            resultado = biblioteca.buscar_por_id(id_livro)
            print(resultado)

        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
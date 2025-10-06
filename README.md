# 📚 Sistema de Gerenciamento de Biblioteca (POO em Python)

Este projeto implementa um **sistema de gerenciamento de biblioteca** utilizando os princípios de **Programação Orientada a Objetos (POO)** em Python.  
Ele permite **cadastrar livros, gerenciar membros, realizar empréstimos e devoluções**, tudo com uma estrutura modular e organizada.

---

## 🧩 Estrutura do Projeto

```
prova9_pooII/
│
├── main.py
└── models/
    ├── __init__.py
    ├── biblioteca.py
    ├── imports.py
    ├── livro.py
    ├── membro.py
    └── menu.py
```

---

## ⚙️ Funcionalidades

### 📘 Classe `Livro`
Representa um livro da biblioteca.

- **Atributos:**
  - `titulo`
  - `autor`
  - `id`
  - `disponivel`

- **Métodos:**
  - `emprestar()`: marca o livro como emprestado
  - `devolver()`: torna o livro disponível novamente

---

### 👤 Classe `Membro`
Representa um usuário da biblioteca.

- **Atributos:**
  - `nome`
  - `numero_membro`
  - `historico`

- **Métodos:**
  - `emprestar_livro()`
  - `devolver_livro()`

---

### 🏛️ Classe `Biblioteca`
Gerencia os livros e membros.

- **Atributos:**
  - `catalogo`
  - `membros`

- **Métodos:**
  - `adicionar_livro(livro)`
  - `adicionar_membro(membro)`
  - `emprestar_livro(id_livro, numero_membro)`
  - `devolver_livro(id_livro, numero_membro)`
  - `listar_livros_disponiveis()`

---

### 🧭 Menu Interativo (`menu.py`)
Um menu simples para o usuário navegar e interagir com o sistema, permitindo:
- Cadastrar livros e membros
- Emprestar e devolver livros
- Listar livros disponíveis
- Sair do programa

---

## ▶️ Execução

Para executar o projeto, rode o arquivo principal:

```bash
python main.py
```

---

## 💡 Tecnologias Utilizadas
- **Python 3.12+**
- **Programação Orientada a Objetos (POO)**
- Estrutura modular com pacotes (`models`)

---

## 🧠 Conceitos Aplicados
- Associação de objetos
- Modularização
- Tipagem e anotações
- Interação entre classes

---

## 👨‍💻 Autor
Desenvolvido por **Francisco** como parte dos estudos de **Programação Orientada a Objetos em Python**.

class AlunoClass:
    def __init__(self, nome, sobrenome, nota):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        return (
            "Aluno: " + self.nome + " " + self.sobrenome + " - Nota: " + str(self.nota)
        )

    def salvar(self, conexao, colecao):
        print("Escreva o seu método aqui...")

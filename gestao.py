class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def info(self):
        return super().info() + f", Matrícula: {self.matricula}"

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def info(self):
        return super().info() + f", Disciplina: {self.disciplina}"

class FuncionarioAdministrativo(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
    
    def info(self):
        return super().info() + f", Cargo: {self.cargo}"

# Programa principal para demonstrar a funcionalidade do sistema
if __name__ == "__main__":
    aluno1 = Aluno("João", 20, "2021001")
    professor1 = Professor("Maria", 35, "Matemática")
    funcionario1 = FuncionarioAdministrativo("Carlos", 40, "Secretário")

    print("Informações sobre os membros da comunidade educacional:")
    print(aluno1.info())
    print(professor1.info())
    print(funcionario1.info())
from models.Funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo, estado_civil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor, salario: float, crea: str):
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento, cpf, rg, matricula, setor, salario)
        self.crea = crea


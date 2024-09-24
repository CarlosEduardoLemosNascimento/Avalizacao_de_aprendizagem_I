from models.Fisica import Fisica
from models.enum.Setor import Setor

class Funcionario(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo, estado_civil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float):
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento)
        if len(cpf) != 11:
            raise ValueError("CPF inválido: deve ter 11 caracteres.")
        if salario < 0:
            raise ValueError("Salário inválido: o salário não pode ser negativo.")
        
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

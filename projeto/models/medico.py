from models.Funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo, estado_civil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor, salario: float, crm: str):
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento, cpf, rg, matricula, setor, salario)
        self.crm = crm
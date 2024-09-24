from models.Fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo, estado_civil, data_nascimento: str, protocolo_atendimento: int):
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento)
        self.protocolo_atendimento = protocolo_atendimento

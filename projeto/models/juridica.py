from abc import ABC, abstractmethod
from models.Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, cnpj: str, inscricao_estadual: str):
        super().__init__(id, nome, telefone, email, endereco)
        if len(cnpj) != 14:
            raise ValueError("CNPJ inválido: deve ter 14 caracteres.")
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

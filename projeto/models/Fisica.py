from abc import ABC, abstractmethod
import os
from models.Pessoa import Pessoa
from models.enum.Sexo import Sexo
from models.enum.EstadoCivil import EstadoCivil

class Fisica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str):
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.data_nascimento = data_nascimento

        # O formato “%Y-%m-%d” especifica que a string segue o padrão de ano-mês-dia


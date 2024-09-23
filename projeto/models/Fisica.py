from abc import ABC, abstractmethod
import os
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.EstadoCivil import EstadoCivil
from datetime import datetime

class Fisica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str):
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.data_nascimento = data_nascimento

        # Validação de data de nascimento
        try:
            data = datetime.strptime(data_nascimento, '%Y-%m-%d')
            if data > datetime.now():
                raise ValueError("Data de nascimento inválida: a data não pode ser no futuro.")
        except ValueError:
            raise ValueError("Data de nascimento inválida: formato incorreto, deve ser YYYY-MM-DD.")
        # O formato “%Y-%m-%d” especifica que a string segue o padrão de ano-mês-dia


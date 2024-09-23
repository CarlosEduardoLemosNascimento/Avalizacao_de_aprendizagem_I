import os
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from datetime import datetime

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa):
        if not logradouro or not numero or not cidade:
            raise ValueError("Endereço inválido: campos obrigatórios não podem ser vazios.")
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

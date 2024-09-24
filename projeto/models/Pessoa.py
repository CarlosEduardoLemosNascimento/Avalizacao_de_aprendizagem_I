from abc import ABC, abstractmethod
import os
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from projeto.models.Endereco import Endereco
from datetime import datetime

class Pessoa:
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco):
        if not nome:
            raise ValueError("Nome inválido: o nome não pode ser vazio.")
        if "@" not in email:
            raise ValueError("Email inválido: formato de email incorreto.")
        
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

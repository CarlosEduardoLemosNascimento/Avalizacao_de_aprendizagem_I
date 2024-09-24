import os
class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf):
        if not logradouro:
            raise ValueError("Logradouro inválido: não pode ser vazio.")
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf  # Enum UnidadeFederativa

import pytest
from projeto.models.Funcionario import Funcionario
from projeto.models.Endereco import Endereco
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.EstadoCivil import EstadoCivil
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from projeto.models.enum.Setor import Setor

def test_funcionario_cpf_invalido():
    endereco = Endereco("Rua B", "456", "Apto 101", "12345-678", "Cidade B", UnidadeFederativa.SAO_PAULO)
    with pytest.raises(ValueError, match="CPF inválido: deve ter 11 caracteres."):
        Funcionario(1, "Maria", "99999-8888", "maria@example.com", endereco, Sexo.FEMININO, EstadoCivil.SOLTEIRO, "1990-05-20", "123", "987654321", "1234", Setor.ENGENHARIA, 5000)

def test_funcionario_salario_negativo():
    endereco = Endereco("Rua C", "789", "Casa 2", "12345-678", "Cidade C", UnidadeFederativa.RIO_DE_JANEIRO)
    with pytest.raises(ValueError, match="Salário inválido: o salário não pode ser negativo."):
        Funcionario(2, "José", "99999-7777", "jose@example.com", endereco, Sexo.MASCULINO, EstadoCivil.CASADO, "1985-10-12", "12345678910", "12345678", "5678", Setor.SAUDE, -1000)

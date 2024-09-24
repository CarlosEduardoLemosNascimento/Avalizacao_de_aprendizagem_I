import pytest
from projeto.models.Pessoa import Pessoa
from projeto.models.Endereco import Endereco
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa

def test_pessoa_nome_vazio():
    endereco = Endereco("Rua A", "123", "", "12345-678", "Cidade A", UnidadeFederativa.BAHIA)
    with pytest.raises(ValueError, match="Nome inválido: o nome não pode ser vazio."):
        Pessoa(1, "", "99999-9999", "email@example.com", endereco)

def test_pessoa_email_invalido():
    endereco = Endereco("Rua A", "123", "", "12345-678", "Cidade A", UnidadeFederativa.BAHIA)
    with pytest.raises(ValueError, match="Email inválido: formato de email incorreto."):
        Pessoa(1, "João", "99999-9999", "email.com", endereco)

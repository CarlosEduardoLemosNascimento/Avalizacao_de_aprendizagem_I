import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.Endereco import Endereco
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa

def test_fornecedor_cnpj_invalido():
    endereco = Endereco("Rua E", "123", "Loja A", "65432-198", "Cidade E", UnidadeFederativa.SAO_PAULO)
    with pytest.raises(ValueError, match="CNPJ inválido: deve ter 14 caracteres."):
        Fornecedor(4, "Loja X", "88888-5555", "loja@example.com", endereco, "123456789", "123456", "Produtos X")

def test_fornecedor_produto_vazio():
    endereco = Endereco("Rua F", "789", "Sala 3", "12345-000", "Cidade F", UnidadeFederativa.RIO_DE_JANEIRO)
    with pytest.raises(ValueError, match="Produto inválido: o produto fornecido não pode ser vazio."):
        Fornecedor(5, "Loja Y", "77777-4444", "lojay@email.com", endereco, "12345678901234", "654321", "")

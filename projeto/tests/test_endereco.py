import pytest
from projeto.models.Endereco import Endereco
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def test_endereco_logradouro_vazio():
    with pytest.raises(ValueError, match="Logradouro inválido: não pode ser vazio."):
        Endereco("", "100", "Apto 4", "12345-678", "Cidade Z", UnidadeFederativa.BAHIA)

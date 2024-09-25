import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.Endereco import Endereco
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.EstadoCivil import EstadoCivil
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from projeto.models.enum.Setor import Setor

def test_engenheiro_crea_vazio():
    endereco = Endereco("Rua G", "123", "Casa 1", "56789-012", "Cidade G", UnidadeFederativa.SAO_PAULO)
    with pytest.raises(ValueError, match="CREA inválido: o CREA não pode ser vazio."):
        Engenheiro(6, "Pedro", "99999-2222", "pedro@email.com", endereco, Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "1990-11-11", "12345678910", "987654321", "ENG123", Setor.ENGENHARIA, 8000, "")

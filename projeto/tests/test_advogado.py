import pytest
from projeto.models.advogado import Advogado
from projeto.models.Endereco import Endereco
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.EstadoCivil import EstadoCivil
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from projeto.models.enum.Setor import Setor

def test_advogado_oab_vazio():
    endereco = Endereco("Rua I", "456", "Sala 201", "67890-123", "Cidade I", UnidadeFederativa.RIO_DE_JANEIRO)
    with pytest.raises(ValueError, match="OAB inválido: o OAB não pode ser vazio."):
        Advogado(8, "Carlos", "77777-2222", "carlos@email.com", endereco, Sexo.MASCULINO, EstadoCivil.VIUVO, "1980-01-01", "12345678910", "87654321", "ADV456", Setor.JURIDICO, 12000, "")

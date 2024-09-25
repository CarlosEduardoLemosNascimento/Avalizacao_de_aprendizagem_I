import pytest
from projeto.models.medico import Medico
from projeto.models.Endereco import Endereco
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.EstadoCivil import EstadoCivil
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa
from projeto.models.enum.Setor import Setor

def test_medico_crm_vazio():
    endereco = Endereco("Rua H", "321", "Apto 101", "76543-210", "Cidade H", UnidadeFederativa.BAHIA)
    with pytest.raises(ValueError, match="CRM inválido: o CRM não pode ser vazio."):
        Medico(7, "Mariana", "88888-3333", "mariana@email.com", endereco, Sexo.FEMININO, EstadoCivil.SEPARADO, "1993-03-23", "09876543210", "123456789", "MED123", Setor.SAUDE, 10000, "")

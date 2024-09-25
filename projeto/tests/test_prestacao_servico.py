import pytest
from projeto.models.prestacao_servico import PrestacaoServico

@pytest.fixture
def test_prestacao_servico_data_invalida():
    with pytest.raises(ValueError, match="Data inválida: formato incorreto, use YYYY-MM-DD."):
        PrestacaoServico("2023-15-01", "2023-12-31")

def test_prestacao_servico_data_inicio_maior():
    with pytest.raises(ValueError, match="Data inválida: a data de início deve ser anterior à data de fim."):
        PrestacaoServico("2023-12-31", "2023-01-01")

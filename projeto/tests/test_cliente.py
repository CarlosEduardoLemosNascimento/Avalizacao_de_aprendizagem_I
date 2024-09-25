from projeto.models.cliente import Cliente
from projeto.models.Endereco import Endereco
from projeto.models.enum.Sexo import Sexo
from projeto.models.enum.EstadoCivil import EstadoCivil
from projeto.models.enum.UnidadeFederativa import UnidadeFederativa

@pytest.fixture
def test_cliente_protocolo_invalido():
    endereco = Endereco("Rua D", "321", "Apto 201", "98765-432", "Cidade D", UnidadeFederativa.BAHIA)
    with pytest.raises(ValueError, match="Protocolo de atendimento inválido."):
        Cliente(3, "Ana", "99999-6666", "ana@email.com", endereco, Sexo.FEMININO, EstadoCivil.DIVORCIADO, "1992-07-15", -1)

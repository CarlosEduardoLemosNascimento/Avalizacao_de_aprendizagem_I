from models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco, cnpj: str, inscricao_estadual: str, produto: str):
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        if not produto:
            raise ValueError("Produto inválido: o produto fornecido não pode ser vazio.")
        self.produto = produto

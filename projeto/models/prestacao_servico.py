from datetime import datetime

class PrestacaoServico:
    def __init__(self, contrato_inicio: str, contrato_fim: str):
        try:
            self.contrato_inicio = datetime.strptime(contrato_inicio, '%Y-%m-%d')
            self.contrato_fim = datetime.strptime(contrato_fim, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Data inválida: formato incorreto, use YYYY-MM-DD.")
        if self.contrato_inicio > self.contrato_fim:
            raise ValueError("Data inválida: a data de início deve ser anterior à data de fim.")
 # O formato “%Y-%m-%d” especifica que a string segue o padrão de ano-mês-dia
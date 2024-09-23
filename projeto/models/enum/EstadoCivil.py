import os
from enum import Enum
from datetime import datetime
class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"
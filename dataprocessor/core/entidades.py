from dataclasses import dataclass, field


@dataclass(frozen=True)
class Cliente:
    id: int
    nome: str
    email: str
    idade: int
    cidade: str
    data_cadastro: str

    @property
    def identificacao(self):
        return f"#{self.id} - {self.nome}"


@dataclass(frozen=True)
class Transacao:
    id: int
    cliente_id: int
    valor: float
    categoria: str
    data: str
    status: str

    @property
    def esta_aprovada(self):
        return self.status == "aprovado"


@dataclass(frozen=True)
class Resultado:
    clientes: list
    transacoes: list
    clientes_invalidos: list
    transacoes_invalidas: list
    metricas: dict = field(default_factory=dict)

from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    caminho_clientes: str = "data/clientes.csv"
    caminho_transacoes: str = "data/transacoes.csv"
    caminho_config: str = "data/config.json"

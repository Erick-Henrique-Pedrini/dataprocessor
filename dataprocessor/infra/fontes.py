from abc import ABC, abstractmethod

from . import arquivos


class FonteDados(ABC):
    @abstractmethod
    def carregar_clientes(self): ...

    @abstractmethod
    def carregar_transacoes(self): ...

    @abstractmethod
    def carregar_config(self): ...


class FonteDadosArquivos(FonteDados):
    def __init__(self, caminho_clientes, caminho_transacoes, caminho_config):
        self.caminho_clientes = caminho_clientes
        self.caminho_transacoes = caminho_transacoes
        self.caminho_config = caminho_config

    def carregar_clientes(self):
        return arquivos.carregar_clientes(self.caminho_clientes)

    def carregar_transacoes(self):
        return arquivos.carregar_transacoes(self.caminho_transacoes)

    def carregar_config(self):
        return arquivos.carregar_config(self.caminho_config)


class FonteDadosMemoria(FonteDados):
    def __init__(self, clientes, transacoes, config):
        self._clientes = clientes
        self._transacoes = transacoes
        self._config = config

    def carregar_clientes(self):
        return list(self._clientes)

    def carregar_transacoes(self):
        return list(self._transacoes)

    def carregar_config(self):
        return dict(self._config)

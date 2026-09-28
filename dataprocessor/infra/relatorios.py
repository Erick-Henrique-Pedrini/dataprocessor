import csv
import io
import json
from abc import ABC, abstractmethod
from dataclasses import asdict


class GeradorRelatorio(ABC):
    extensao = "txt"

    @abstractmethod
    def render(self, resultado) -> str: ...


class RelatorioTexto(GeradorRelatorio):
    def render(self, resultado):
        m = resultado.metricas
        return "\n".join([
            "=== DataProcessor ===",
            f"Clientes válidos: {len(resultado.clientes)}",
            f"Clientes inválidos: {len(resultado.clientes_invalidos)}",
            f"Transações válidas: {len(resultado.transacoes)}",
            f"Transações inválidas: {len(resultado.transacoes_invalidas)}",
            f"Média de idade: {m['media_idade']:.1f}",
            f"Total aprovado: R$ {m['total_aprovado']:.2f}",
            f"Ticket médio aprovado: R$ {m['ticket_medio_aprovado']:.2f}",
        ])


class RelatorioJson(GeradorRelatorio):
    extensao = "json"

    def render(self, resultado):
        return json.dumps(asdict(resultado), ensure_ascii=False, indent=2)


class RelatorioCsv(GeradorRelatorio):
    extensao = "csv"

    def render(self, resultado):
        saida = io.StringIO()
        escritor = csv.writer(saida, lineterminator="\n")
        escritor.writerow(["metrica", "valor"])
        escritor.writerow(["clientes_validos", len(resultado.clientes)])
        escritor.writerow(["transacoes_validas", len(resultado.transacoes)])
        for nome, valor in resultado.metricas.items():
            escritor.writerow([nome, f"{valor:.2f}"])
        return saida.getvalue()


GERADORES = {"texto": RelatorioTexto, "json": RelatorioJson, "csv": RelatorioCsv}


def criar_gerador(formato):
    try:
        return GERADORES[formato]()
    except KeyError:
        raise ValueError(f"formato desconhecido: '{formato}'") from None

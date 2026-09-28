import csv
import json

from ..core.entidades import Cliente, Transacao


def _para_int(valor, padrao=None):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return padrao


def _para_float(valor, padrao=None):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return padrao


def carregar_clientes(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return [
            Cliente(
                id=_para_int(linha["id"]),
                nome=linha["nome"].strip(),
                email=linha["email"].strip(),
                idade=_para_int(linha["idade"]),
                cidade=linha["cidade"].strip(),
                data_cadastro=linha["data_cadastro"].strip(),
            )
            for linha in csv.DictReader(arquivo)
        ]


def carregar_transacoes(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return [
            Transacao(
                id=_para_int(linha["id"]),
                cliente_id=_para_int(linha["cliente_id"]),
                valor=_para_float(linha["valor"]),
                categoria=linha["categoria"].strip(),
                data=linha["data"].strip(),
                status=linha["status"].strip(),
            )
            for linha in csv.DictReader(arquivo)
        ]


def carregar_config(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)

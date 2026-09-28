def _idades_validas(clientes):
    return [c.idade for c in clientes if c.idade and c.idade > 0]


def _valores_aprovados(transacoes):
    return [t.valor for t in transacoes if t.esta_aprovada and t.valor and t.valor > 0]


def media_idade(clientes):
    idades = _idades_validas(clientes)
    return sum(idades) / len(idades) if idades else 0


def total_aprovado(transacoes):
    return sum(_valores_aprovados(transacoes))


def ticket_medio_aprovado(transacoes):
    valores = _valores_aprovados(transacoes)
    return sum(valores) / len(valores) if valores else 0


def extremos_idade(clientes):
    idades = _idades_validas(clientes)
    if not idades:
        return None, None
    return min(idades), max(idades)


def contar_por_cidade(clientes):
    contagem = {}
    for cliente in clientes:
        contagem[cliente.cidade] = contagem.get(cliente.cidade, 0) + 1
    return contagem

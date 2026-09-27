def media_idade(clientes):
    idades_validas = [c["idade"] for c in clientes if c.get("idade") and c["idade"] > 0]
    if not idades_validas:
        return 0
    return sum(idades_validas) / len(idades_validas)


def total_aprovado(transacoes):
    return sum(
        t["valor"]
        for t in transacoes
        if t.get("status") == "aprovado" and t.get("valor", 0) > 0
    )


def ticket_medio_aprovado(transacoes):
    valores = [
        t["valor"]
        for t in transacoes
        if t.get("status") == "aprovado" and t.get("valor", 0) > 0
    ]
    if not valores:
        return 0
    return sum(valores) / len(valores)


def extremos_idade(clientes):
    """Retorna (minimo, maximo) das idades válidas."""
    idades_validas = [c["idade"] for c in clientes if c.get("idade") and c["idade"] > 0]
    if not idades_validas:
        return None, None
    return min(idades_validas), max(idades_validas)


def contar_por_cidade(clientes):
    """Retorna dicionário com contagem de clientes por cidade."""
    contagem = {}
    for cliente in clientes:
        cidade = cliente["cidade"]
        contagem[cidade] = contagem.get(cidade, 0) + 1
    return contagem

from leitor import (
    carregar_clientes,
    carregar_transacoes,
    carregar_config,
)

from validador import (
    validar_cliente,
    validar_transacao,
    separar_registros,
)

from transformador import (
    transformar_clientes,
    transformar_transacoes,
)

from processador import (
    media_idade,
    total_aprovado,
    formatar_moeda,
)

# ----------------------------
# LEITURA
# ----------------------------

clientes_raw = carregar_clientes("data/clientes.csv")
transacoes_raw = carregar_transacoes("data/transacoes.csv")
config = carregar_config("data/config.json")

# ----------------------------
# CLIENTES
# ----------------------------

clientes_validos, clientes_invalidos = separar_registros(
    clientes_raw,
    validar_cliente
)

ids_validos = {c["id"] for c in clientes_validos}
ids_invalidos = {
    c["registro"]["id"]
    for c in clientes_invalidos
}

# ----------------------------
# TRANSAÇÕES
# ----------------------------

transacoes_validas, transacoes_invalidas = separar_registros(
    transacoes_raw,
    validar_transacao,
    ids_clientes=ids_validos,
    ids_clientes_invalidos=ids_invalidos,
    config=config
)

clientes = transformar_clientes(clientes_validos)
transacoes = transformar_transacoes(transacoes_validas)

# ==================================================
# SAÍDA
# ==================================================

print(
    f"CLIENTES PROCESSADOS ({len(clientes)} válidos de {len(clientes_raw)})"
)

for c in clientes:
    print(
        f"  ID {c['id']} | "
        f"{c['nome']} | "
        f"{c['email']} | "
        f"{c['idade']} anos | "
        f"{c['cidade']}"
    )

print()

print(f"CLIENTES REJEITADOS ({len(clientes_invalidos)})")

for erro in clientes_invalidos:
    cliente = erro["registro"]
    print(
        f"  ID {cliente['id']} — "
        f"{cliente['nome']}: "
        + ", ".join(erro["erros"])
    )

print()

print(
    f"TRANSAÇÕES PROCESSADAS ({len(transacoes)} válidas de {len(transacoes_raw)})"
)
for t in transacoes:
    print(
        f"  ID {t['id']} | "
        f"cliente {t['cliente_id']} | "
        f"{formatar_moeda(t['valor'])} | "
        f"{t['categoria']} | "
        f"{t['status']}"
    )

print()

print(f"TRANSAÇÕES REJEITADAS ({len(transacoes_invalidas)})")

for erro in transacoes_invalidas:
    t = erro["registro"]
    print(
        f"  ID {t['id']} — "
        + ", ".join(erro["erros"])
    )

print()

print("MÉTRICAS")
print(
    f"  Total aprovado: {formatar_moeda(total_aprovado(transacoes))}"
)

media = media_idade(clientes)

if media is not None:
    print(f"  Média de idade (válidos): {media:.1f}")
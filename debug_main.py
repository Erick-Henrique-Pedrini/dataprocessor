from dataprocessor.pipeline import executar_pipeline


def imprimir_invalidos(titulo, invalidos):
    print(f"\n--- {titulo} ({len(invalidos)}) ---")
    for item in invalidos:
        registro = item["registro"]
        print(f"id={registro.get('id')}: {'; '.join(item['erros'])}")


def main():
    resultado = executar_pipeline(
        "data/clientes.csv",
        "data/transacoes.csv",
        "data/config.json",
    )

    print("=== DataProcessor (debug) ===")
    print(f"Clientes válidos: {len(resultado['clientes'])}")
    print(f"Transações válidas: {len(resultado['transacoes'])}")

    imprimir_invalidos("Clientes inválidos", resultado["clientes_invalidos"])
    imprimir_invalidos("Transações inválidas", resultado["transacoes_invalidas"])


if __name__ == "__main__":
    main()

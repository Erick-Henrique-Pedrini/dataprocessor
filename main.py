from dataprocessor.pipeline import executar_pipeline


def main():
    resultado = executar_pipeline(
        "data/clientes.csv",
        "data/transacoes.csv",
        "data/config.json",
    )

    print("=== DataProcessor ===")
    print(f"Clientes válidos: {len(resultado['clientes'])}")
    print(f"Transações válidas: {len(resultado['transacoes'])}")
    print(f"Média de idade: {resultado['metricas']['media_idade']:.1f}")
    print(f"Total aprovado: R$ {resultado['metricas']['total_aprovado']:.2f}")
    print(f"Ticket médio aprovado: R$ {resultado['metricas']['ticket_medio_aprovado']:.2f}")


if __name__ == "__main__":
    main()
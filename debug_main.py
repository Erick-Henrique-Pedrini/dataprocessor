from dataprocessor.config import AppConfig
from dataprocessor.infra.fontes import FonteDadosArquivos
from dataprocessor.services.processamento import executar_processamento


def imprimir_invalidos(titulo, invalidos):
    print(f"\n--- {titulo} ({len(invalidos)}) ---")
    for item in invalidos:
        print(f"id={item['registro'].id}: {'; '.join(item['erros'])}")


def main():
    c = AppConfig()
    resultado = executar_processamento(
        FonteDadosArquivos(c.caminho_clientes, c.caminho_transacoes, c.caminho_config)
    )
    print("=== DataProcessor (debug) ===")
    print(f"Clientes válidos: {len(resultado.clientes)}")
    print(f"Transações válidas: {len(resultado.transacoes)}")
    imprimir_invalidos("Clientes inválidos", resultado.clientes_invalidos)
    imprimir_invalidos("Transações inválidas", resultado.transacoes_invalidas)


if __name__ == "__main__":
    main()

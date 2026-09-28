from ..config import AppConfig
from ..infra.fontes import FonteDadosArquivos
from ..infra.relatorios import GERADORES, criar_gerador
from ..services.processamento import executar_processamento


def processar():
    padrao = AppConfig()
    caminhos = [
        input(f"{rotulo} [{valor}]: ").strip() or valor
        for rotulo, valor in [
            ("Caminho do CSV de clientes", padrao.caminho_clientes),
            ("Caminho do CSV de transações", padrao.caminho_transacoes),
            ("Caminho do JSON de config", padrao.caminho_config),
        ]
    ]
    try:
        resultado = executar_processamento(FonteDadosArquivos(*caminhos))
    except (OSError, ValueError, KeyError) as erro:
        print(f"[ERRO] Não foi possível processar: {erro}")
        return None
    print(f"Clientes válidos: {len(resultado.clientes)}")
    print(f"Transações válidas: {len(resultado.transacoes)}")
    return resultado


def exibir_relatorio(resultado):
    formato = input("Formato (texto/json/csv) [texto]: ").strip() or "texto"
    if formato not in GERADORES:
        print(f"Formato inválido: '{formato}'.")
        return
    print(criar_gerador(formato).render(resultado))


def menu_principal():
    resultado = None
    while True:
        print("\n=== DataProcessor — Menu ===")
        print("1. Processar dados")
        print("2. Exibir relatório")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao not in {"1", "2", "3"}:
            print(f"Opção inválida: '{opcao}'. Escolha 1, 2 ou 3.")
        elif opcao == "1":
            novo = processar()
            if novo is not None:
                resultado = novo
        elif opcao == "2":
            if resultado is None:
                print("Nenhum dado processado ainda. Escolha a opção 1 primeiro.")
                continue
            exibir_relatorio(resultado)
        else:
            break


if __name__ == "__main__":
    menu_principal()

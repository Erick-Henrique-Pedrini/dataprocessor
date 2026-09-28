import argparse
import logging
import sys
from pathlib import Path

from .config import AppConfig
from .infra.fontes import FonteDadosArquivos
from .infra.relatorios import GERADORES, criar_gerador
from .services.processamento import executar_processamento

logger = logging.getLogger("dataprocessor")


def criar_parser():
    padrao = AppConfig()
    parser = argparse.ArgumentParser(prog="dataprocessor", description="Processa clientes e transações.")
    parser.add_argument("--clientes", default=padrao.caminho_clientes)
    parser.add_argument("--transacoes", default=padrao.caminho_transacoes)
    parser.add_argument("--config", default=padrao.caminho_config)
    parser.add_argument("--formato", choices=sorted(GERADORES), default="texto")
    parser.add_argument("--output", default="output", help="diretório de saída")
    return parser


def main(argv=None):
    args = criar_parser().parse_args(argv)
    saida = Path(args.output)
    saida.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=saida / "dataprocessor.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    try:
        fonte = FonteDadosArquivos(args.clientes, args.transacoes, args.config)
        resultado = executar_processamento(fonte)
        gerador = criar_gerador(args.formato)
        destino = saida / f"relatorio.{gerador.extensao}"
        destino.write_text(gerador.render(resultado), encoding="utf-8")
    except (OSError, ValueError, KeyError) as erro:
        logger.exception("falha ao processar")
        print(f"[ERRO] {erro}", file=sys.stderr)
        return 1
    logger.info("relatório salvo em %s", destino)
    print(f"Relatório salvo em {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

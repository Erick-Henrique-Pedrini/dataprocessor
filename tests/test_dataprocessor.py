import json
import unittest

from dataprocessor.core.entidades import Cliente, Transacao
from dataprocessor.infra.fontes import FonteDados, FonteDadosArquivos, FonteDadosMemoria
from dataprocessor.infra.relatorios import GeradorRelatorio, RelatorioCsv, RelatorioJson, criar_gerador
from dataprocessor.services.processamento import executar_processamento

CONFIG = {"categorias_validas": ["livros"], "status_validos": ["aprovado"], "valor_minimo": 0}
CLIENTES = [
    Cliente(1, "  ana LIMA ", "ANA@x.com", 30, "São Paulo", "2023-01-01"),
    Cliente(2, "", "invalido", -1, "X", "nope"),
]
TRANSACOES = [
    Transacao(1, 1, 100.0, "livros", "2023-01-01", "aprovado"),
    Transacao(2, 2, 50.0, "livros", "2023-01-01", "aprovado"),
]


class Testes(unittest.TestCase):
    def setUp(self):
        self.res = executar_processamento(FonteDadosMemoria(CLIENTES, TRANSACOES, CONFIG))

    def test_entidades(self):
        self.assertEqual(CLIENTES[0].identificacao, "#1 -   ana LIMA ")
        self.assertTrue(TRANSACOES[0].esta_aprovada)

    def test_processamento_memoria(self):
        self.assertEqual(len(self.res.clientes), 1)
        self.assertEqual(self.res.clientes[0].nome, "Ana Lima")
        self.assertEqual(len(self.res.clientes_invalidos), 1)
        self.assertEqual(len(self.res.transacoes), 1)  # transação do cliente 2 é inválida
        self.assertEqual(self.res.metricas["total_aprovado"], 100.0)

    def test_processamento_arquivos(self):
        res = executar_processamento(
            FonteDadosArquivos("data/clientes.csv", "data/transacoes.csv", "data/config.json")
        )
        self.assertGreater(len(res.clientes), 0)

    def test_relatorios(self):
        self.assertIsInstance(criar_gerador("json"), GeradorRelatorio)
        self.assertEqual(json.loads(RelatorioJson().render(self.res))["metricas"]["total_aprovado"], 100.0)
        self.assertIn("total_aprovado,100.00", RelatorioCsv().render(self.res))
        with self.assertRaises(ValueError):
            criar_gerador("xml")

    def test_abcs_nao_instanciaveis(self):
        with self.assertRaises(TypeError):
            FonteDados()
        with self.assertRaises(TypeError):
            GeradorRelatorio()


if __name__ == "__main__":
    unittest.main()

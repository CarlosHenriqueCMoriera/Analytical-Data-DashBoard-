import logging
import sys
sys.path.append(".")

from extract import extrair_usuarios, extrair_produtos, extrair_carrinhos
from transform import transformar_usuarios, transformar_produtos, transformar_carrinhos
from load import carregar_usuarios, carregar_produtos, carregar_carrinhos

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def executar_pipeline():
    logging.info("=== INICIANDO PIPELINE ETL ===")

    # EXTRACT
    logging.info("Etapa 1: Extraindo dados da API...")
    dados_usuarios = extrair_usuarios()
    dados_produtos = extrair_produtos()
    dados_carrinhos = extrair_carrinhos()

    # TRANSFORM
    logging.info("Etapa 2: Transformando dados...")
    df_usuarios = transformar_usuarios(dados_usuarios)
    df_produtos = transformar_produtos(dados_produtos)
    df_carrinhos = transformar_carrinhos(dados_carrinhos)

    # LOAD
    logging.info("Etapa 3: Carregando dados no banco...")
    carregar_usuarios(df_usuarios)
    carregar_produtos(df_produtos)
    carregar_carrinhos(df_carrinhos)

    logging.info("=== PIPELINE CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    executar_pipeline()
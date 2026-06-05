from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

load_dotenv(dotenv_path="../.env")

def criar_conexao():
    string_conexao = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    engine = create_engine(string_conexao)
    return engine

def carregar_usuarios(df_usuarios):
    engine = criar_conexao()
    df_usuarios.to_sql("usuarios", engine, if_exists="replace", index=False)
    logging.info(f"{len(df_usuarios)} usuários carregados no banco!")

def carregar_produtos(df_produtos):
    engine = criar_conexao()
    df_produtos.to_sql("produtos", engine, if_exists="replace", index=False)
    logging.info(f"{len(df_produtos)} produtos carregados no banco!")

def carregar_carrinhos(df_carrinhos):
    engine = criar_conexao()
    df_carrinhos.to_sql("carrinhos", engine, if_exists="replace", index=False)
    logging.info(f"{len(df_carrinhos)} carrinhos carregados no banco!")

if __name__ == "__main__":
    import pandas as pd
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    df_usuarios_teste = pd.DataFrame([{"id": 1, "nome": "Emily", "sobrenome": "Johnson", "idade": 29, "genero": "female", "email": "emily@test.com", "pais": "United States"}])
    df_produtos_teste = pd.DataFrame([{"id": 1, "titulo": "Mascara", "categoria": "beauty", "preco": 9.99, "avaliacao": 4.5, "estoque": 99, "marca": "Essence"}])
    df_carrinhos_teste = pd.DataFrame([{"id": 1, "id_usuario": 1, "total": 100.0, "total_com_desconto": 90.0, "total_produtos": 3, "total_itens": 5}])

    carregar_usuarios(df_usuarios_teste)
    carregar_produtos(df_produtos_teste)
    carregar_carrinhos(df_carrinhos_teste)
    print("Dados carregados com sucesso!")
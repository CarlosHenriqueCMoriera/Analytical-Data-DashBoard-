import requests
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "https://dummyjson.com"

def fazer_requisicao(url, tentativas=3):
    for i in range(tentativas):
        try:
            logging.info(f"Tentativa {i+1} de {tentativas} - {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            logging.warning("Timeout, tentando novamente...")
            time.sleep(2)
        except requests.exceptions.HTTPError as e:
            logging.error(f"Erro HTTP: {e}")
            break
    return None

def extrair_usuarios():
    logging.info("Extraindo usuários...")
    dados = fazer_requisicao(f"{BASE_URL}/users?limit=100")
    if dados:
        logging.info(f"{len(dados['users'])} usuários extraídos")
        return dados["users"]
    return []

def extrair_produtos():
    logging.info("Extraindo produtos...")
    dados = fazer_requisicao(f"{BASE_URL}/products?limit=100")
    if dados:
        logging.info(f"{len(dados['products'])} produtos extraídos")
        return dados["products"]
    return []

def extrair_carrinhos():
    logging.info("Extraindo carrinhos...")
    dados = fazer_requisicao(f"{BASE_URL}/carts?limit=100")
    if dados:
        logging.info(f"{len(dados['carts'])} carrinhos extraídos")
        return dados["carts"]
    return []

if __name__ == "__main__":
    usuarios = extrair_usuarios()
    produtos = extrair_produtos()
    carrinhos = extrair_carrinhos()
    print(usuarios[:2])
    print(produtos[:2])
    print(carrinhos[:2])
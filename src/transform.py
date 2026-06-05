import pandas as pd

def transformar_usuarios(dados):
    df_original = pd.DataFrame(dados)
    
    df_colunas = df_original[["id", "firstName", "lastName", "age", "gender", "email", "address"]]
    
    df_pais = df_colunas.copy()
    df_pais["country"] = df_colunas["address"].apply(lambda x: x["country"])
    
    df_sem_address = df_pais.drop(columns=["address"])
    
    df_renomeado = df_sem_address.rename(columns={
        "firstName": "nome",
        "lastName": "sobrenome",
        "age": "idade",
        "gender": "genero",
        "email": "email",
        "country": "pais"
    })
    
    df_limpo = df_renomeado.dropna()
    
    return df_limpo

def transformar_produtos(dados):
    df_original = pd.DataFrame(dados)
    
    df_colunas = df_original[["id", "title", "category", "price", "rating", "stock"]]
    
    df_renomeado = df_colunas.rename(columns={
        "title": "titulo",
        "category": "categoria",
        "price": "preco",
        "rating": "avaliacao",
        "stock": "estoque",
    })
    
    df_limpo = df_renomeado.dropna()
    
    return df_limpo

def transformar_carrinhos(dados):
    df_original = pd.DataFrame(dados)
    
    df_colunas = df_original[["id", "userId", "total", "discountedTotal", "totalProducts", "totalQuantity"]]
    
    df_renomeado = df_colunas.rename(columns={
        "userId": "id_usuario",
        "total": "total",
        "discountedTotal": "total_com_desconto",
        "totalProducts": "total_produtos",
        "totalQuantity": "total_itens"
    })
    
    df_limpo = df_renomeado.dropna()
    
    return df_limpo

if __name__ == "__main__":
    usuario_teste = [{"id": 1, "firstName": "Emily", "lastName": "Johnson", "age": 29, "gender": "female", "email": "emily@test.com", "address": {"country": "United States"}}]
    produto_teste = [{"id": 1, "title": "Mascara", "category": "beauty", "price": 9.99, "rating": 4.5, "stock": 99, "brand": "Essence"}]
    carrinho_teste = [{"id": 1, "userId": 1, "total": 100.0, "discountedTotal": 90.0, "totalProducts": 3, "totalQuantity": 5}]

    print(transformar_usuarios(usuario_teste))
    print(transformar_produtos(produto_teste))
    print(transformar_carrinhos(carrinho_teste))
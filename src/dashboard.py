import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

def criar_conexao():
    string_conexao = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return create_engine(string_conexao)

@st.cache_data
def carregar_dados():
    engine = criar_conexao()
    df_usuarios = pd.read_sql("SELECT * FROM usuarios", engine)
    df_produtos = pd.read_sql("SELECT * FROM produtos", engine)
    df_carrinhos = pd.read_sql("SELECT * FROM carrinhos", engine)
    return df_usuarios, df_produtos, df_carrinhos

# configuração da página
st.set_page_config(page_title="Analytical Dashboard", layout="wide")
st.title("📊 Analytical Data Dashboard")

# carrega os dados
df_usuarios, df_produtos, df_carrinhos = carregar_dados()

# =====================
# SEÇÃO 1 - USUÁRIOS
# =====================
st.header("👥 Usuários")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Usuários", len(df_usuarios))

with col2:
    media_idade = round(df_usuarios["idade"].mean(), 1)
    st.metric("Idade Média", media_idade)

with col3:
    paises = df_usuarios["pais"].nunique()
    st.metric("Países", paises)

col4, col5 = st.columns(2)

with col4:
    fig_genero = px.pie(df_usuarios, names="genero", title="Distribuição por Gênero")
    st.plotly_chart(fig_genero, use_container_width=True)

with col5:
    top_paises = df_usuarios["pais"].value_counts().reset_index()
    top_paises.columns = ["pais", "quantidade"]
    fig_paises = px.bar(top_paises.head(10), x="pais", y="quantidade", title="Top 10 Países")
    st.plotly_chart(fig_paises, use_container_width=True)

# =====================
# SEÇÃO 2 - PRODUTOS
# =====================
st.header("🛍️ Produtos")

col6, col7, col8 = st.columns(3)

with col6:
    st.metric("Total de Produtos", len(df_produtos))

with col7:
    preco_medio = round(df_produtos["preco"].mean(), 2)
    st.metric("Preço Médio", f"$ {preco_medio}")

with col8:
    avaliacao_media = round(df_produtos["avaliacao"].mean(), 2)
    st.metric("Avaliação Média", avaliacao_media)

col9, col10 = st.columns(2)

with col9:
    fig_categoria = px.bar(
        df_produtos.groupby("categoria").size().reset_index(name="quantidade"),
        x="categoria", y="quantidade", title="Produtos por Categoria"
    )
    st.plotly_chart(fig_categoria, use_container_width=True)

with col10:
    fig_preco = px.bar(
        df_produtos.groupby("categoria")["preco"].mean().reset_index(),
        x="categoria", y="preco", title="Preço Médio por Categoria"
    )
    st.plotly_chart(fig_preco, use_container_width=True)

# =====================
# SEÇÃO 3 - CARRINHOS
# =====================
st.header("🛒 Carrinhos")

col11, col12, col13 = st.columns(3)

with col11:
    st.metric("Total de Carrinhos", len(df_carrinhos))

with col12:
    media_itens = round(df_carrinhos["total_itens"].mean(), 1)
    st.metric("Média de Itens", media_itens)

with col13:
    total_gasto = round(df_carrinhos["total"].sum(), 2)
    st.metric("Total Gasto", f"$ {total_gasto:,.2f}")

col14, col15 = st.columns(2)

with col14:
    fig_total = px.histogram(df_carrinhos, x="total", title="Distribuição de Gastos por Carrinho")
    st.plotly_chart(fig_total, use_container_width=True)

with col15:
    top_carrinhos = df_carrinhos.nlargest(10, "total")
    fig_top = px.bar(top_carrinhos, x="id", y="total", title="Top 10 Maiores Compras")
    st.plotly_chart(fig_top, use_container_width=True)
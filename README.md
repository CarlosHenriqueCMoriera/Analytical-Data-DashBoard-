# Analytical-Data-DashBoard-

Analytical Data Dashboard
This project implements a complete ETL pipeline combined with an interactive analytical dashboard. Data is extracted from the DummyJSON public API, transformed and loaded into a PostgreSQL database, and visualized through a Streamlit dashboard deployed on Streamlit Community Cloud.
About the Project
The pipeline consumes users, products, and cart data from the DummyJSON API — a free public API that simulates realistic e-commerce data. The data goes through three stages: extraction via HTTP requests with retry logic and error handling, transformation and cleaning using Pandas, and loading into a PostgreSQL database via SQLAlchemy. The dashboard is built with Streamlit and Plotly, providing interactive charts and key metrics across three analytical sections.
Pipeline Stages
Extract — HTTP requests are made to three DummyJSON endpoints (users, products, carts) with support for multiple retry attempts on timeout. Each endpoint has its own dedicated extraction function.
Transform — raw data from each endpoint is converted into structured DataFrames with column selection, renaming to a standardized format, null record removal, and field extraction from nested JSON objects.
Load — each transformed DataFrame is persisted into its own PostgreSQL table. The connection is managed by SQLAlchemy and credentials are securely loaded through environment variables.
Dashboard — Streamlit reads data directly from PostgreSQL and renders interactive visualizations using Plotly, including pie charts, bar charts, histograms, and KPI metrics.
Dashboard Sections
Users — total users, average age, number of countries, gender distribution chart, and top 10 countries by user count.
Products — total products, average price, average rating, products by category chart, and average price per category.
Carts — total carts, average items per cart, total spent, spending distribution histogram, and top 10 largest orders.
Technologies

Python 3.14
Requests for HTTP calls
Pandas for data manipulation and transformation
SQLAlchemy for database connection and loading
PostgreSQL for data storage
python-dotenv for secure credential management
Streamlit for the interactive dashboard
Plotly for data visualizations

Data Source
DummyJSON API — a free public API that provides realistic fake data for users, products, carts, and more, with no authentication required. Documentation available at https://dummyjson.com.
Data Structure
Three tables are loaded into PostgreSQL: usuarios (id, nome, sobrenome, idade, genero, email, pais), produtos (id, titulo, categoria, preco, avaliacao, estoque), and carrinhos (id, id_usuario, total, total_com_desconto, total_produtos, total_itens).

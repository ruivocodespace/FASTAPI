from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

# URL de conexão com o banco de dados
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/banco_SA"

# Cria o objeto de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Cria a classe SessionLocal para instanciar sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declaração de modelos
Base = declarative_base()

# --- FUNÇÃO ESSENCIAL PARA O FASTAPI (get_db) ---

# Esta função é um gerador de dependência que fornece uma sessão de DB
# e garante que ela seja fechada após o uso (bloco finally)
def get_db() -> Generator:
    # 1. Cria a sessão do banco de dados
    db = SessionLocal()
    try:
        # 2. 'yield' retorna a sessão para a rota do FastAPI
        # e o código pára aqui até a rota terminar
        yield db
    finally:
        # 3. Garante que a sessão seja fechada, mesmo se ocorrer um erro
        db.close()
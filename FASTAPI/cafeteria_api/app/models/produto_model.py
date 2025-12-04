from sqlalchemy import Column, Integer, String, DECIMAL, Text, ForeignKey
from cafeteria_api.app.database.connection import Base
# Importa relationship se você for usar (boa prática para relações)
# from sqlalchemy.orm import relationship 

class Produto(Base):
    __tablename__ = "produto"
    
    # Coluna ID principal (Ajustado de idProduto para id)
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # ------------------------------------------------------------------
    # CORREÇÃO: Nomes ajustados para coincidir com o Roteador/Schema
    # (nomeProduto -> nome, precoVenda -> preco, estoqueAtual -> quantidade)
    # ------------------------------------------------------------------
    
    nome = Column(String(100), nullable=False)  # Corrigido
    descricao = Column(Text, nullable=True) # Ajustado (descricaoProduto -> descricao)
    preco = Column(DECIMAL(10, 2), nullable=False) # Corrigido (Usando precoVenda como preco principal)
    
    # Colunas de estoque/quantidade: use 'quantidade' para a rota 'estoqueAtual'
    quantidade = Column(Integer, default=0)  # Corrigido (estoqueAtual -> quantidade)
    
    # Colunas que podem ser mapeadas para schemas internos, mas não são o foco principal
    precoCompra = Column(DECIMAL(10, 2), nullable=True)
    estoqueMinimo = Column(Integer, nullable=True)
    estoqueMaximo = Column(Integer, nullable=True)
    unMedida = Column(String(10), nullable=True)

    # Chave Estrangeira: Ajustado idCategoria -> categoria_id (convenção snake_case)
    categoria_id = Column(Integer, ForeignKey("categoria.idCategoria"), nullable=True)
    
    # ------------------------------------------------------------------
    
    # Adicione este método para uma representação amigável ao debug
    def __repr__(self):
        return f"<Produto(nome='{self.nome}', preco={self.preco})>"
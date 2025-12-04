from sqlalchemy import Column, Integer, String, DECIMAL, Text, ForeignKey
# importa classes do SQLAlchemy usadas para definir colunas e tipos:
# Column -> define uma coluna de tabela
# Integer, String, DECIMAL, Text -> tipos das colunas
# ForeignKey -> cria uma chave estrangeira

from cafeteria_api.app.database.connection import Base

# importa a classe Base (declarative base) definida no seu módulo de conexão.
# Todos os models herdam de Base para serem registrados pelo SQLAlchemy.

class Produto(Base):
    # define uma classe Python que representa a tabela 'produto' no banco
    __tablename__ = "produto"
    # nome exato da tabela no banco. Deve coincidir com o nome utilizado no MySQL.

    idProduto = Column(Integer, primary_key=True, autoincrement=True)
    # coluna idProduto:
    # Integer -> tipo inteiro
    # primary_key=True -> chave primária
    # autoincrement=True -> valor gerado automaticamente pelo banco

    nomeProduto = Column(String(100), nullable=False)
    # coluna nomeProduto:
    # String(100) -> varchar(100)
    # nullable=False -> valor obrigatório (NOT NULL)

    descricaoProduto = Column(Text, nullable=True)
    # coluna descricaoProduto:
    # Text -> texto longo (corresponde a TEXT no MySQL)
    # nullable=True -> pode ser nulo

    precoVenda = Column(DECIMAL(10, 2), nullable=True)
    # coluna precoVenda:
    # DECIMAL(10,2) -> armazena valores decimais com precisão (ideal para preços)
    # nullable=True -> pode ser nulo (você pode alterar para False se quiser obrigar)

    precoCompra = Column(DECIMAL(10, 2), nullable=True)
    # coluna precoCompra:
    # mesma lógica de precoVenda (preço de compra do fornecedor)

    estoqueAtual = Column(Integer, nullable=True)
    # coluna estoqueAtual:
    # Integer -> quantidade disponível em estoque
    # nullable=True -> pode estar nulo se preferir (recomendo DEFAULT 0 no DB)

    estoqueMinimo = Column(Integer, nullable=True)
    # coluna estoqueMinimo:
    # Integer -> valor mínimo do estoque que indica necessidade de reposição

    estoqueMaximo = Column(Integer, nullable=True)
    # coluna estoqueMaximo:
    # Integer -> limite superior ou capacidade máxima (opcional)

    unMedida = Column(String(10), nullable=True)
    # coluna unMedida:
    # String(10) -> unidade de medida (ex: "un", "kg", "ml")

    # Relação simples → apenas guarda o ID da categoria
    idCategoria = Column(Integer, ForeignKey("categoria.idCategoria"), nullable=True)
    # coluna idCategoria:
    # Integer -> guarda o id da categoria (chave estrangeira)
    # ForeignKey("categoria.idCategoria") -> cria a FK apontando para
    # a tabela 'categoria' coluna 'idCategoria' (assume que exista)
    # nullable=True -> produto pode não ter categoria atribuída

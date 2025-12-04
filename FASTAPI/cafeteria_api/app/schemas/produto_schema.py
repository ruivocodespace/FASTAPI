from pydantic import BaseModel

# ============================
# SCHEMA BASE
# ============================
# Campos comuns para criação, atualização e resposta
class ProdutoBase(BaseModel):
    nomeProduto: str
    descricaoProduto: str | None = None
    precoVenda: float
    precoCompra: float | None = None
    estoqueAtual: int | None = None
    estoqueMinimo: int | None = None
    estoqueMaximo: int | None = None
    unMedida: str | None = None
    idCategoria: int | None = None


# ============================
# SCHEMA PARA CRIAR (POST)
# ============================
class ProdutoCreate(ProdutoBase):
    pass


# ============================
# SCHEMA PARA ATUALIZAR (PUT/PATCH)
# ============================
class ProdutoUpdate(BaseModel):
    nomeProduto: str | None = None
    descricaoProduto: str | None = None
    precoVenda: float | None = None
    precoCompra: float | None = None
    estoqueAtual: int | None = None
    estoqueMinimo: int | None = None
    estoqueMaximo: int | None = None
    unMedida: str | None = None
    idCategoria: int | None = None


# ============================
# SCHEMA PARA RETORNAR AO CLIENTE
# ============================
class ProdutoResponse(ProdutoBase):
    idProduto: int

    class Config:
        orm_mode = True  # permite retornar objetos SQLAlchemy


# ============================
# SCHEMA OPCIONAL (alias)
# — Se quiser usar ProdutoSchema como nome genérico
# ============================
class ProdutoSchema(ProdutoBase):
    idProduto: int | None = None

    class Config:
        orm_mode = True

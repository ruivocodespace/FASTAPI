# Importa APIRouter para criar grupo de rotas
from fastapi import APIRouter, Depends, HTTPException

from cafeteria_api.app.models.produto_model import Produto
from cafeteria_api.app.schemas.produto_schema import ProdutoSchema
from cafeteria_api.app.database.connection import get_db


# Cria o grupo de rotas /produtos
router = APIRouter(prefix="/produtos", tags=["Produtos"])


# ============================================================
#                   ROTA: CRIAR PRODUTO
# ============================================================
@router.post("/", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    # Cria um objeto Produto com os dados recebidos
    novo_produto = Produto(
        nome=produto.nome,
        preco=produto.preco,
        quantidade=produto.quantidade
    )

    # Adiciona o produto na sessão do banco
    db.add(novo_produto)

    # Salva as mudanças no MySQL
    db.commit()

    # Atualiza o objeto para pegar o ID gerado
    db.refresh(novo_produto)

    # Retorna o produto criado
    return novo_produto


# ============================================================
#                   ROTA: LISTAR TODOS
# ============================================================
@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    # SELECT * FROM produtos
    produtos = db.query(Produto).all()
    return produtos


# ============================================================
#                   ROTA: BUSCAR POR ID
# ============================================================
@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    # Busca um produto pelo ID
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    # Caso não exista, devolve erro HTTP 404
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto


# ============================================================
#                   ROTA: ATUALIZAR PRODUTO
# ============================================================
@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db: Session = Depends(get_db)):
    # Busca o produto no banco
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    # Se não existir, erro 404
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Atualiza os campos
    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade

    # Aplica as alterações no MySQL
    db.commit()
    db.refresh(produto)

    return produto


# ============================================================
#                   ROTA: DELETAR PRODUTO
# ============================================================
@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    # Busca o produto
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    # Se não existir → erro 404
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Remove o registro
    db.delete(produto)
    db.commit()

    return {"mensagem": "Produto removido com sucesso"}

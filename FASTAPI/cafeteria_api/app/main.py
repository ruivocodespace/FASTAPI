from fastapi import FastAPI
from cafeteria_api.app.routers.produto_router import router as produto_router


app = FastAPI()

# registra as rotas /produtos
app.include_router(produto_router)

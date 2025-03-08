from fastapi import FastAPI, HTTPException
from typing import Optional
from typing import List
from pydantic import BaseModel

app = FastAPI()

PRODUTOS = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone inteligente",
        "preco": 1999.99,
        "disponivel": True
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um laptop potente para trabalho e jogos",
        "preco": 4999.99,
        "disponivel": True
    },
    {
        "id": 3,
        "nome": "Fone de Ouvido Bluetooth",
        "descricao": "Fone de ouvido sem fio com cancelamento de ruído",
        "preco": 349.90,
        "disponivel": True
    },
    {
        "id": 4,
        "nome": "Smartwatch",
        "descricao": "Relógio inteligente com monitoramento de saúde",
        "preco": 899.99,
        "disponivel": False
    },
    {
        "id": 5,
        "nome": "Monitor 4K",
        "descricao": "Monitor de alta resolução para trabalho e entretenimento",
        "preco": 1799.00,
        "disponivel": False
    }
]

class Produto(BaseModel):
    """Classe de produto"""

    nome: str
    descricao: Optional[str] = None
    preco: float
    disponivel: Optional[bool] = True

@app.get("/produtos", tags=["produtos"])
def listar_produtos() -> list:
    """Listar produtos"""
    return PRODUTOS

@app.get("/produtos/disponiveis", tags=["produtos"])
def listar_produtos_disponiveis() -> list:
    """Listar apenas os produtos disponíveis."""
    produtos_disponiveis = [produto for produto in PRODUTOS if produto["disponivel"]]
    return produtos_disponiveis      

@app.get("/produtos/{produto_id}", tags=["produtos"])
def obter_produto(produto_id: int) -> dict:
    """Obter produto"""
    for produto in PRODUTOS:
        if produto["id"] == produto_id:
            return produto
    return{}

@app.post("/produto", tags=["produtos"])
def criar_produto(produto: Produto) -> dict:
    """Criar produto."""
    produto = produto.dict()
    produto["id"] = len(PRODUTOS) + 1
    PRODUTOS.append(produto)
    return produto



@app.put("/produtos/{produto_id}", tags=["produtos"])
def atualizar_produto(produto_id: int, produto: Produto) -> dict:
    """Atualizar produto mantendo o ID original."""
    for index, prod in enumerate(PRODUTOS):
        if prod["id"] == produto_id:
            # Atualiza os dados sem remover o ID
            PRODUTOS[index] = {"id": produto_id, **produto.dict()}
            return PRODUTOS[index]
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produtos/{produto_id}", tags=["produtos"])
def deletar_produto(produto_id: int) -> dict:
    """Deletar um produto pelo ID."""
    for index, prod in enumerate(PRODUTOS):
        if prod["id"] == produto_id:
            del PRODUTOS[index]
            return {"message": "Produto removido com sucesso"}
    
    raise HTTPException(status_code=404, detail="Produto não encontrado") 
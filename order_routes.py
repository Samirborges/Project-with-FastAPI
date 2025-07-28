from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Caminho padrão para os pedidos no sistema
    """
    
    return {
        "mensagem": "Você está no caminho padrão para se realizar o pedido"
    }
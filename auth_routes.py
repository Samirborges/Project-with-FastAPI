from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Caminho padrão de autenticação do usuário para o sistema
    """
    
    return {
        "mensagem": "Você está no endpoint de autenticação",
        "autenticado": False
    }
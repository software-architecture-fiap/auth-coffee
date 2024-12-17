import json
import logging
from services.auth_service import AuthService
from utils.response import create_response

# Configuração de logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Instância do serviço de autenticação
auth_service = AuthService()

def lambda_handler(event, context):
    """
    Handler principal para geração de tokens JWT.
    Recebe eventos do API Gateway e autentica o usuário.
    """
    try:
        logger.info("Evento recebido: %s", event)

        # Valida se o método HTTP é POST
        if event['httpMethod'] != 'POST':
            return create_response(405, {"error": "Method Not Allowed"})

        # Valida o corpo da requisição
        if 'body' not in event or not event['body']:
            return create_response(400, {"error": "Request body is required"})

        body = json.loads(event['body'])
        username = body.get('username')
        password = body.get('password')

        # Valida se os campos obrigatórios estão presentes
        if not username or not password:
            return create_response(400, {"error": "Username and password are required"})

        # Chama o serviço para autenticar e gerar o token
        token = auth_service.generate_token(username, password)

        # Retorna o token gerado
        return create_response(200, {"token": token})

    except ValueError as e:
        # Erros de validação
        logger.error("Erro de validação: %s", str(e))
        return create_response(400, {"error": str(e)})

    except Exception as e:
        # Erros genéricos
        logger.error("Erro inesperado: %s", str(e))
        return create_response(500, {"error": "Internal server error"})

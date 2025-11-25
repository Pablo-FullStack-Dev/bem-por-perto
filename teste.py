# import bcrypt

# def gerar_hash(senha: str) -> bytes:
#     senha_bytes = senha.encode()
#     salt = bcrypt.gensalt()  # gera um salt automático
#     hash_senha = bcrypt.hashpw(senha_bytes, salt)
#     print(hash_senha)
#     return hash_senha


# gerar_hash("cobaiA@ro32")
# resposta : '$2b$12$t9aIm9GgYrmtHfuQ9Xocg.xZHLnpVbUu/Ck.RBIDqNlMFvfabM40C'
from .interface import InterfaceInterno
from ..conexao import *
from gerenciamento_software import sql_executar_comando,sql_consultar_dado,criptografar_SHA256_SALT

class Interno(InterfaceInterno):
    def __init__(self,conexao):
        self.database = conexao

    
    def alterar_senha(self,valor_atual:str,novo_valor:str,email:str)->None:
            pegar_salt = f'SELECT {USER_SALT} FROM {TABLE_USER} WHERE {USER_EMAIL}="{email}"'
            salt = sql_consultar_dado(pegar_salt)
            salt = salt[0]
            valor_atual = valor_atual+salt
            hash_final = criptografar_SHA256_SALT(novo_valor)
            novo_valor = hash_final['hashFinal']
            novo_salt = hash_final['salt']
            comando = f'UPDATE {TABLE_USER} SET {USER_SALT}={novo_salt} WHERE {USER_EMAIL}="{email}"'
            sql_executar_comando(comando)


comandos_internos = Interno(conexao)
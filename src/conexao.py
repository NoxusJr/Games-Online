from dotenv import load_dotenv,find_dotenv
from gerenciamento_software import sql_conectar_db
from os import getenv



load_dotenv(find_dotenv())

HOST = getenv('host')
USER = getenv('user')
PASSWORD = getenv('password')
DATABASE = getenv('database')

TABLE_USER = getenv('table_user')
USER_NOME = getenv('user_nome')
USER_EMAIL = getenv('user_email')
USER_SENHA = getenv('user_senha')
USER_SALT = getenv('user_salt')


class Conexao:
    def __init__(self,host:str,user:str,password:str,database:str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        sql_conectar_db(host=self.host,user=self.user,password=self.password,database=self.database)


conexao = Conexao(HOST,USER,PASSWORD,DATABASE)
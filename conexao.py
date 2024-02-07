from dotenv import load_dotenv,find_dotenv
import gerenciamento_software as gs

HOST = ''
USER = ''
PASSWORD = ''
DATABASE = ''


class Conexao:
    def __init__(self,host:str,user:str,password:str,database:str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        gs.sql_conectar_db(host=self.host,user=self.user,password=self.password,database=self.database)


conexao = Conexao(HOST,USER,PASSWORD,DATABASE)
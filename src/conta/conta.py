from .interface import InterfaceConta
from ..conexao import *
from ..interno.interno import comandos_internos
from gerenciamento_software import *

class ContaUsuario(InterfaceConta):
    def __init__(self,conexao):
        self.conexao = conexao


    def criar_conta(self,nome:str,email:str,senha:str) -> bool:
        execucao = sql_criar_conta(criptografar=True,
                                   tabela=TABLE_USER,
                                   coluna_nome=USER_NOME,
                                   coluna_email=USER_EMAIL,
                                   coluna_senha=USER_SENHA,
                                   coluna_salt=USER_SALT,
                                   nome=nome,
                                   email=email,
                                   senha=senha)


    def logar_conta(self,email:str,senha:str) -> bool:
        execucao = sql_logar_conta(criptografar=True,
                                   tabela=TABLE_USER,
                                   coluna_email=USER_EMAIL,
                                   coluna_senha=USER_SENHA,
                                   coluna_salt=USER_SALT,
                                   email=email,
                                   senha=senha)


    def alterar_conta(self,email:str,campo:str,valor_atual:str,novo_valor:str) -> bool:
        campos = [USER_NOME,USER_SENHA]
        if (campo in campos):
            if (campo == USER_SENHA):
                comandos_internos.alterar_senha(valor_atual,novo_valor,email)

            condicao = f'{campo}="{valor_atual}" AND {USER_EMAIL}="{email}"'

            execucao = sql_alterar_conta(tabela=TABLE_USER,
                                        coluna=campo,
                                        valor=novo_valor,
                                        condicao=condicao)
        else:
            False

    def excluir_conta(self,email:str) -> bool:
        condicao = f'{USER_EMAIL}="{email}"'

        execucao = sql_excluir_conta(tabela=TABLE_USER,
                                     condicao=condicao)
        

conta_usuario = ContaUsuario(conexao)
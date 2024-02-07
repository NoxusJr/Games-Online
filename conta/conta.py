from .interface import InterfaceConta
from ..conexao import conexao



class ContaUsuario(InterfaceConta):
    def __init__(self,conexao):
        self.conexao = conexao


    def criar_conta(self,nome:str,email:str,senha:str) -> bool:
        pass


    def logar_conta(self,email:str,senha:str) -> bool:
        pass


    def alterar_conta(self,email:str,campo:str,valor_atual:str,novo_valor:str) -> bool:
        pass


    def excluir_conta(self,email:str) -> bool:
        pass
from .interface import InterfaceConta
from ..conexao import conexao



class ContaUsuario(InterfaceConta):
    def __init__(self,conexao):
        self.conexao = conexao

    
    def criar_conta(self,nome,email,senha):
        pass
    
    
    def logar_conta(self,email,senha):
        pass
    
    
    def alterar_conta(self,email,campo,valor_atual,novo_valor):
        pass
    
    
    def excluir_conta(self,email):
        pass
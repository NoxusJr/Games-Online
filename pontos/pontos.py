from .interface import InterfacePontos
from ..conexao import conexao



class PontosUsuario(InterfacePontos):
    def __init__(self,conexao):
        self.conexao = conexao


    def registrar_ponto(self,email:str,pontuacao:int,jogo:int) -> bool:
        pass


    def retornar_pontos(self,email:str,jogo:int,geral:bool=False) -> dict:
        pass


    def retornar_ranking(self) -> dict:
        pass
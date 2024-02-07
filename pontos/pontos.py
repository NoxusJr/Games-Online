from .interface import InterfacePontos
from ..conexao import conexao



class PontosUsuario(InterfacePontos):
    def __init__(self,conexao):
        self.conexao = conexao


    def registrar_ponto(self):
        pass


    def retornar_pontos(self):
        pass


    def retornar_ranking(self):
        pass
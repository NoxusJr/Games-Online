from abc import ABC, abstractmethod



class InterfacePontos(ABC):
    @abstractmethod
    def registrar_ponto(self):
        pass


    @abstractmethod
    def retornar_pontos(self):
        pass


    @abstractmethod
    def retornar_ranking(self):
        pass
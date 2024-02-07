from abc import ABC, abstractmethod



class InterfaceConta(ABC):
    @abstractmethod
    def criar_conta(self):
        pass

    @abstractmethod
    def logar_conta(self):
        pass

    @abstractmethod
    def alterar_conta(self):
        pass

    @abstractmethod
    def excluir_conta(self):
        pass
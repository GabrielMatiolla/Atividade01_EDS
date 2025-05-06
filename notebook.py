from produto import Produto

class Notebook(Produto):
    def __init__(self, modelo: str, cor: str, preco: float, categoria, tempoDeBateria: int):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria  # fortemente privado

    def getInformacoes(self):
        info = super().getInformacoes()
        info["tempoDeBateria"] = self.__tempoDeBateria
        return info

    def cadastrar(self):
        print("Notebook cadastrado com sucesso!")

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    @tempoDeBateria.setter
    def tempoDeBateria(self, value: int):
        self.__tempoDeBateria = value
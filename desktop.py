from produto import Produto

class Desktop(Produto):
    def __init__(self, modelo: str, cor: str, preco: float, categoria, potenciaDaFonte: int):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte  #fracamente priivado

    def getInformacoes(self):
        info = super().getInformacoes()
        info["potenciaDaFonte"] = self._potenciaDaFonte
        return info

    def cadastrar(self):
        print("Desktop cadastrado com sucesso!")

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte
    
    @potenciaDaFonte.setter
    def potenciaDaFonte(self, value: int):
        self._potenciaDaFonte = value
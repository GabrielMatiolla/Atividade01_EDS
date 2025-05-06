class Categoria:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value: str):
        self._nome = value
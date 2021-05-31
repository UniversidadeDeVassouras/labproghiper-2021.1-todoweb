from datetime import datetime


class ToDo:

    def __init__(self, id: int, titulo: str, descricao: str, data: datetime):
        self.__id = id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data = data

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
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

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def data(self):
        return self.__data

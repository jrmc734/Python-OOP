from enum import Enum, IntEnum, auto
from datetime import date

class Prioridade(IntEnum):
    BAIXA = auto()
    MEDIA = auto()
    ALTA = auto()

    def __str__(self):
        return f'{self.name}'

#Descritores
class NaoVazio:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name
    
    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)     

    def __set__(self, obj, value):
        if not(isinstance(value, str)):
            raise ValueError('Precisa ser string')
        
        if len(value) == 0:
            raise ValueError('Não recebe string vazia')
        
        only_space = 1
        for i in value:
            if i != ' ':
                only_space = 0
        if only_space:
            raise ValueError('Não recebe string só com espaços')
        return setattr(obj, self.private_name, value)

class DataNaoPassada:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name
    
    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        if not(isinstance(value, date)):
            raise ValueError('Precisa ser uma instância datetime.date')
        if date.today() > value:
            raise ValueError('Não aceita datas anteriores a hoje')
        return setattr(obj, self.private_name, value)

class Teste:
    nome = NaoVazio()
    data = DataNaoPassada()

    def __init__(self, nome, data):
        self.nome = nome
        self.data = data

if __name__ == '__main__':
    ...
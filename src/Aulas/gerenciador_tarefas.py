from enum import Enum, IntEnum, auto
from datetime import date
from dataclasses import dataclass, InitVar

class Prioridade(IntEnum):
    BAIXA = auto()
    MEDIA = auto()
    ALTA = auto()

    def __str__(self):
        return f'{self.name}'

#Descritores
class NaoVazio:
    """ 
        Valida strings não vazias 
        Não aceita strings só com espaços
    """
    def __set_name__(self, owner, name):
        self.private_name = '_' + name
    
    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)     

    def __set__(self, obj, value):
        if not(isinstance(value, str)):
            raise ValueError('{self.name} precisa ser do tipo string')

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
    """
        Valida datas (datetime.date) que não estão no passado
        Aceita hoje como válido
    """
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

@dataclass
class Tarefa:
    nome = NaoVazio()
    prazo = DataNaoPassada()

    _nome = InitVar[str]
    _prazo = InitVar[date]

    prioridade: Prioridade = Prioridade.MEDIA
    concluida: bool = False

    def __post_init__(self, _nome: str, _prazo: date):
        if not(isinstance(self.prioridade, Prioridade)):
            raise ValueError('A prioridade deve ser do tipo Prioridade')
        self.nome = _nome
        self.prazo = _prazo
    
    def __str__(self):
        concluida_aux = '✓' if self.concluida else 'x'
        return f'[{self.prioridade.name}] {self.prazo.isoformat()} {self.nome} (concluida: ✓/{concluida_aux} )'

class GerenciadorTarefas:
    def __init__(self):
        self.tarefa = [] #lista de Tarefas

    def adicionar_tarefas(self, tarefa: Tarefa):
        if not(isinstance(tarefa, Tarefa)):
            raise ValueError('A tarefa precisa ser do tipo Tarefa')
        self.tarefa.append(tarefa)
        
    def _parse_bool(s:str) -> bool:
        if not(isinstance(s,str)):
            raise ValueError('A entrada precisa ser do tipo string')
        
        return True if s.lower() in ['s','sim','1','true'] else False

def main():
    ...
    
if __name__ == '__main__':
    main()
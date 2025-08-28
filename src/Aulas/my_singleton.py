class Singleton:
    _instancia = None
    def __new__(cls, *args, **kwargs): # essa função roda no momento em que o objeto está sendo criado
        if cls._instancia == None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
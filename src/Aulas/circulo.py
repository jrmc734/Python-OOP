
pi = 3.14159

def area(raio: int|float) -> float:
    return pi * (raio ** 2)

def circunferencia(raio: int|float) -> float:
    return 2 * pi * raio

def superficie_esfera(raio: int|float) -> float:
    return 4 * area(raio)

def volume_esfera(raio: int|float) -> float:
    return (4.0/3.0) * pi * (raio ** 3)

# Essas linhas somente serão executadas quando circulo.py
# estiver sendo executado diretamente como programa principal

if __name__ == '__main__':
    print(pi)
    print(area(2))
    
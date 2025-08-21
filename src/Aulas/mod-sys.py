import sys

def soma_2():
    if len(sys.argv) != 3:
        print(f'Uso indevido, tem que chamar $python {sys.argv[0]} num1 num2')
        sys.exit(2)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(f'{a} + {b} = {a+b}')
        sys.exit(0)
    except ValueError:
        print('Erro! Os argumentos devem ser numéricos!')
        sys.exit(2)

def soma_n():
    if len(sys.argv) == 1:
        print(f'Uso indevido, voce deve pelo menos chamar $python {sys.argv[0]} num1 ...')
        sys.exit(2)
    
    try:
        numeros = list(map(int, sys.argv[1:]))
        print(sum(numeros))
        sys.exit(0)
    except ValueError:
        print('Erro! Os argumentos devem ser numéricos!')
        sys.exit(2)

def conversor():
    if len(sys.argv) != 3:
        print(f'Uso indevido, voce deve pelo menos chamar $python {sys.argv[0]} ESCALA(ctf,ftc) VALOR')
    try:
        escala = sys.argv[1].strip().lower()
        valor = float(sys.argv[2])
        if escala == 'ctf':
            conv_numb = (9/5 * valor) + 32
            print(f'O valor {valor} em fahhrenheint é: {conv_numb:.3f}')
        elif escala == 'ftc':
            conv_numb = (valor - 32) * 5/9
            print(f'O valor {valor} em celcius é: {conv_numb:.3f}')
        else:
            raise ValueError('A ESCALA deve ser ctf ou ftc')
    except ValueError as e:
        print(e)
   
def ler_arquivo():
    if len(sys.argv) == 1:
        print(f'Uso indevido, voce deve pelo menos chamar $python {sys.argv[0]} caminho_arquivo ...')
        sys.exit(2)  
    try:
        with open(sys.argv[1]) as arq:
            conteudo = arq.read()
        print(conteudo)
        sys.exit(0)
    except FileNotFoundError:
        print('Erro o arquivo não existe!')
        sys.exit(2)

if __name__ == '__main__':
    conversor()

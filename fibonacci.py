def fib(numero):
    ultimoNumero = 0
    numeroAtual = 1
    if numero == 0:
        return True
    while numeroAtual < numero:
        aux = numeroAtual
        numeroAtual = ultimoNumero + numeroAtual
        ultimoNumero = aux
    if numeroAtual == numero:
        return True
    else:
        return False

numero = input("escreva o número que deseja verificar")

print("está na sequencia de Fibonacci" if fib(int(numero)) is True else "Não está na sequencia de Fibonacci")
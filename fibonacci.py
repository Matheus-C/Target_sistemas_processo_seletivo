def fib(numero):
    ultimoNumero = 0 #o numero anterior ao atual encontrado, utilizado para calcular o próximo número atual
    numeroAtual = 1 # o número encontrado na ultima iteração
    if numero == 0:
        return True
    while numeroAtual < numero:
        aux = numeroAtual # guarda o numero atual para colocar na posicao de ultimo numero
        numeroAtual = ultimoNumero + numeroAtual #calcula o novo numero atual
        ultimoNumero = aux
    if numeroAtual == numero:
        return True
    else:
        return False

numero = input("escreva o número que deseja verificar")

print("está na sequencia de Fibonacci" if fib(int(numero)) is True else "Não está na sequencia de Fibonacci")
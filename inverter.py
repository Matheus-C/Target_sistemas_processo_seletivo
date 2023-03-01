

palavra = input("escreva a palavra que você deseja inverter")
invertida = ""
for i in range(len(palavra), 0, -1):
    invertida += palavra[i-1:i]
print(invertida)
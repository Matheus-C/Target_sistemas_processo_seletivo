from json import load

arq = open("dados.json", "r")
dados = load(arq)
arq.close()
cont = 0
total = 0
for i in range(len(dados)):
    if dados[i]['valor'] != 0:
        cont += 1
        total += dados[i]['valor']
print("o valor da média dos faturamentos é: {media:.2f}".format(media = total/cont))

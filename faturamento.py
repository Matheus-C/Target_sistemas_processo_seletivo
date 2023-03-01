from json import load

arq = open("dados.json", "r") # carrega o arquivo json
dados = load(arq) # captura os dados do arquivo e os converte para um dicionário
arq.close()
cont = 0
total = 0
for i in range(len(dados)):
    if dados[i]['valor'] != 0:
        cont += 1 # conta a quantidade de valores válidos para utilizar na media
        total += dados[i]['valor'] # soma todos os valores
print("o valor da média dos faturamentos é: {media:.2f}".format(media = total/cont))

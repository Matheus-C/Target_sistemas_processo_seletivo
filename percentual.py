
# dicionário dos estados e seus respectivos faturamentos
estados = {"nome": "São Paulo", "faturamento": 67836.43}, {"nome": "Rio de Janeiro", "faturamento": 36678.66}, {"nome": "Minas Gerais", "faturamento": 29229.88}, {"nome": "Espirito Santo", "faturamento": 27165.48}, {"nome": "Outros", "faturamento": 19849.53}
total = 0
# calcula o total dos faturamentos, ou seja, 100% dos faturamentos
for estado in estados:
    total += estado["faturamento"]
for estado in estados: # calcula a participação de cada estado individualmente e atribui uma porcentagem com duas casas decimais
    print(f"O percentual de participação do estado {estado['nome']} é de: " + "{:.2f}%".format(estado['faturamento']*100/total))
# importando a biblioteca csv para ler arquivos CSV e armazenar os dados em uma lista de dicionários
# utilizando função built-in open para abrir o arquivo CSV e ler seu conteúdo

import csv

caminho_arquivo: str = 'exemplo.csv'

arquivo_csv: list = []

with open(caminho_arquivo, mode= 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)
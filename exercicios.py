
# 3 Crie um dicionário para armazenar informações de um livro, incluindo título,
#  autor e ano de publicação. Imprima cada informação.

# Criando um dicionário para armazenar informações de um livro


""" from typing import Dict, Any

livro: Dict[str, Any] = {
    "título": "1984",
    "autor": "George Orwell",
    "ano de publicação": 1948
}

# Imprimindo cada informação
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")
print(livro) """

#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado

""" numeros = list(range(1, 11))
for n in numeros:
    print(f"{n}² = {n**2}")
 """

# 2 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

""" linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")   
print(linguagens) """

# 3 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação.
#  Imprima cada informação.

""" livro = {
    "título": "1984",
    "autor": "George Orwell",
    "ano de publicação": 1948,
    "editora": "moderna"
}

for chave, valor in livro.items():
    print(f"{chave}: {valor}")  """

# 4 Escreva um programa que conta o número de ocorrências de cada caractere em uma
#  string usando um dicionário

""" palavra = "banana"
contador = {}
x= len(palavra)
print(x) """

""" def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados")) """

# 5 Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#  calcule o preço total da lista de compras.

""" frutas = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preco_total = sum(precos[fruta] for fruta in frutas)
print(f"Preço total: R$ {preco_total:.2f}") """

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


# 6 Dada uma lista de emails, remover todos os duplicados.

""" emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos) """

""" # 7 Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [15, 22, 17, 30, 18, 12]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas) """

# 8 Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

""" pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Charlie", "idade": 35}
]
pessoas_ordenadas = sorted(pessoas, key=lambda x: x["nome"])
print(pessoas_ordenadas) """

# 9 Dada uma lista de números, calcular a média.

""" numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)
print(f"Média: {media}") """

# 10 Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

""" valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares) """

# 11 Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


""" produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos) """

# 12 Dados dois dicionários, fundi-los em um único dicionário.

""" dicionario1 = {"a": 1, "b": 2}                
dicionario2 = {"c": 3, "d": 4}
dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido) """

#13 Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

""" estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

for produto, quantidade in estoque.items():
    if quantidade > 0:
        print(produto) """


#  14 Dado um dicionário, criar listas separadas para suas chaves e valores.

""" dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values()) 
print("Chaves:", chaves)
print("Valores:", valores) """

# 15 Dada uma string, contar a frequência de cada caractere usando um dicionário.

""" texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia) """

# Lista de exemplo
""" lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
lista_exemplo.sort()
print("Lista ordenada:", lista_exemplo) """


""" def normalizar_nome(nome: str) -> str:
    return nome.strip().lower()

nomes = [" Alice ", "BOB", "Carlos"]
nomes_normalizados = [normalizar_nome(nome) for nome in nomes]
print(nomes_normalizados) """

# 16 Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

""" def somar_numeros(numeros: list) -> int:
    return sum(numeros)

lista_numeros = [1, 2, 3, 4, 5]
resultado = somar_numeros(lista_numeros)
print("Soma:", resultado) """

# 17 Crie uma função que receba um número como argumento e retorne True se
#  o número for primo e False caso contrário.

""" n =3

def eh_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

print(eh_primo(n)) """

#18 Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

""" palavra = input(f'Digite uma palavra: ')

def reverter_string(s: str) -> str:
    return s[::-1]
print(reverter_string(palavra))   """ 

# 19 Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve
#  retornar todas as combinações de pares na lista que somem ao número dado.

""" from itertools import combinations

def encontrar_pares(lista: list, alvo: int):
    pares = []
    for combo in combinations(lista, 2):
        if sum(combo) == alvo:
            pares.append(combo)
    return pares

numeros = [1, 2, 3, 4, 5]
alvo = 6
print(encontrar_pares(numeros, alvo)) """

# 20 Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

""" def ordenar_chaves(dicionario: dict) -> list:
    return sorted(dicionario.keys())        

dicionario_exemplo = {"b": 2, "a": 1, "c": 3}
print(ordenar_chaves(dicionario_exemplo)) """

# desafio tipar codigo abaixo

def main() -> None:
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    # Validação do nome
    while not nome_valido:
        try:
            nome: str = input("Digite seu nome: ")

            # Verifica se o nome está vazio
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            # Verifica se há números no nome
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)

    # Solicita ao usuário que digite o valor do seu salário e converte para float
    try:
        salario: float = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        exit()

    # Solicita ao usuário que digite o valor do bônus recebido e converte para float
    try:
        bonus: float = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        exit()

    bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

    # Imprime as informações para o usuário
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")


if __name__ == "__main__":
    main()

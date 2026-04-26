
# 3 Crie um dicionário para armazenar informações de um livro, incluindo título,
#  autor e ano de publicação. Imprima cada informação.

# Criando um dicionário para armazenar informações de um livro


from typing import Dict, Any

livro: Dict[str, Any] = {
    "título": "1984",
    "autor": "George Orwell",
    "ano de publicação": 1948
}

# Imprimindo cada informação
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")
print(livro)
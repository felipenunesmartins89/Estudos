# def soma(x, y):
#     """
#     Função que soma dois valores
#     """
#     return x + y
#
#



#"""
#EXEMPLO DE FUNÇÃO NOMEADA PARA RETORNAR MAIORES DE 27 COM LAMBDA(ANONIMA)
#"""

users = [
  {
    "id": 1,
    "name": "Allan",
    "age": 27,
    "profile_picture": "http://…",
    "city": "São Paulo"
  },
  {
    "id": 2,
    "name": "Julie",
    "age": 29,
    "profile_picture": "http://…",
    "city": "Curitiba"
  },
  {
    "id": 3,
    "name": "Pedro",
    "age": 31,
    "profile_picture": "http://…",
    "city": "Rio de Janeiro"
  }
]

filtered_users = filter(lambda user: user["age"] > 27, users)

print(list(filtered_users))
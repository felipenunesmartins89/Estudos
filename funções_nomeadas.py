# def soma(x, y):
#     """
#     Função que soma dois valores
#     """
#     return x + y
#
#
# print(soma.__name__) #retorna o nome da função
#
# print(dir(soma)) #retorna métodos e atributos dentro do objeto do tipo função
#
# print(soma.__doc__) #retorna o que tem dentro da nossa função(metadados)
#
# print(soma (2, 2)) #chama função soma e passa 2 parametros
#
#
# def div(x, y):
#     """
#     Função que soma dois valores
#     """
#     return x / y
#
# try:
#     print(div(0, 0)) #nenhum número é divisivel por zero
# except:
#     print(div.__name__) #retornou o nome da função
#
#
# #"""
# #EXEMPLO DE FUNÇÃO NOMEADA PARA RETORNAR MAIORES DE 27
# #"""
#
# users = [
#   {
#     "id": 1,
#     "name": "Allan",
#     "age": 27,
#     "profile_picture": "http://…",
#     "city": "São Paulo"
#   },
#   {
#     "id": 2,
#     "name": "Julie",
#     "age": 29,
#     "profile_picture": "http://…",
#     "city": "Curitiba"
#   },
#   {
#     "id": 3,
#     "name": "Pedro",
#     "age": 31,
#     "profile_picture": "http://…",
#     "city": "Rio de Janeiro"
#   }
# ]
#
#
# # Crie a função que irá filtrar a lista
# def maior_27(pessoas):
#   return pessoas["age"] > 27
#
# # Filtramos os usuários utilizando o método filter
# filtered_users = filter(maior_27, users)
#
# print(list(filtered_users))
#


def externa(id):
    dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en': 'hello'}

    def interna(nome):
        print(f'{dic[id]} {nome}')
    return interna

func = externa('en')
func('Pedro')
func('Julio')
func('Marivaldo')


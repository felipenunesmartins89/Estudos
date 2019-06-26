def soma(x, y):
    """
    Função que soma dois valores
    """
    return x + y


print(soma.__name__) #retorna o nome da função

print(dir(soma)) #retorna métodos e atributos dentro do objeto do tipo função

print(soma.__doc__) #retorna o que tem dentro da nossa função(metadados)

print(soma (2, 2)) #chama função soma e passa 2 parametros


def div(x, y):
    """
    Função que soma dois valores
    """
    return x / y

try:
    print(div(0, 0)) #nenhum número é divisivel por zero
except:
    print(div.__name__) #retornou o nome da função


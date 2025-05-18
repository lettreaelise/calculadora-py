# função soma	
def soma(a:int, b:int):
    return a + b

# função divisão
def divisao(a:int, b:int):
    if b == 0:
        raise ValueError("Não é permitido a divisão por zero!")
    return a / b

def multiplicacao(a:int, b:int):
    return a * b

def subtracao(a:int, b:int): # Função adicionada
    return a - b
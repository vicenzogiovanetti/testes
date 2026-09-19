#soma dos naturais de 1 a n
nome = input("Digite seu nome:")
n = int(input("Digite um número natural:"))
def soma(n):
    return sum(range(1,n+1))
print(f"Olá, {nome}! A soma dos números naturais de 1 a {n} é {soma(n)}.")
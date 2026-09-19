#soma dos naturais de 1 a n
n = int(input("Digite um número natural:"))
def soma(n):
    return sum(range(1,n+1))
print(soma(n))
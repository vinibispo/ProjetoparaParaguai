n = int(input('Digite um número: '))
def sumOfCombinations(n):
    s = 0
    for i in range(0,n):
        s += combination(n, i)
    return s
def factorial(n):
    m = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            m *= i
        return m

def combination(n, p):
    return factorial(n)/(factorial(p) * factorial(n - p))

def averageCombination(n):
    return sumOfCombinations(n)/n

print(f'A média das combinações de {n} é {averageCombination(n)}')

# 2. Verificação de Fibonacci

def verifica_fibonacci(numero):
    a = 0
    b = 1

    fibonacci = [a, b]

    while b < numero:
        a, b = b, a + b
        fibonacci.append(b)
    
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(verifica_fibonacci(numero))
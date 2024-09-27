def Fib(n):
    a = 0
    b = 1
    c = a + b
    while c <= n:
        c = a + b
        a = b
        b = c
        if c == n:
            return "O numero informado pertence a sequencia de Fibonacci"
    return "O numero informado nao pertence a sequencia de Fibonacci"
    
    
if __name__ == "__main__":
    # numero definido pelo usuario
    num = int(input("Digite um numero: "))
    print(Fib(num))
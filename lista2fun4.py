def par_ou_impar(numero):
    if numero%2==0:
        n = "par"
    else:
        n = "ímpar"
    return n

numero = int(input("Digite um número inteiro: "))
print("O número é ", par_ou_impar(numero))
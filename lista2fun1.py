def min(a):
    menor=a[0]
    for i in a:
        if i < menor:
            menor=i
    return menor



def max(a):
    maior=0
    for i in a:
        if i > maior:
            maior=i
    return maior


def media_do_aluno(p1, p2, p3):
    p1 ,p2 ,p3 =faltar(p1, p2,p3)
    return (p1 + p2 + p3)/3


def faltar(p1, p2, p3):
    if p1 == "faltei":
        p1 = 0
    elif p2 == "faltei":
        p2 = 0
    elif p3 == "faltei":
        p3 = 0
    return float (p1, p2, p3)






















p1 = input("Digite a primeira nota: ")
p2 = input("Digite a segunda nota: ")
p3 = input("Digite a terceira nota: ")
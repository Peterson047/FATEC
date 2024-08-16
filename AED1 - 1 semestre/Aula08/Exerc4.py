def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:       
        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Valores incorretos"
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

resultado = verificar_triangulo(lado1, lado2, lado3)
print(resultado)
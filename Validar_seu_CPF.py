# CÁLCULO DO PRIMEIRO E SEGUNDO DIGITO DO CPF
cpf = input("Digite seu CPF (somente números): ")

# Cálculo do primeiro dígito
somar_1 = sum(int(cpf[i]) for i in range(9))
multiplicar_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
multiplicar10_1 = multiplicar_1 * 10
resto_1 = multiplicar10_1 % 11
verificador_1 = int(cpf[9:10])

if resto_1 > 9:
    resultado_1 = 0
else:
    resultado_1 = resto_1

# Cálculo do segundo dígito
somar_2 = sum(int(cpf[i]) for i in range(10))
multiplicar_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
multiplicar10_2 = multiplicar_2 * 10
resto_2 = multiplicar10_2 % 11
verificador_2 = int(cpf[10:11])

if resto_2 > 9:
    resultado_2 = 0
else:
    resultado_2 = resto_2

# Verificador
if resultado_1 != verificador_1 or resultado_2 != verificador_2:
    print("CPF solicitado não é válido")
else:
    print("CPF solicitado é válido")

# Calculation of the first and second CPF digits
cpf = input("Enter your CPF (numbers only): ")

# Calculation of the first digit
somar_1 = sum(int(cpf[i]) for i in range(9))
multiplicar_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
multiplicar10_1 = multiplicar_1 * 10
resto_1 = multiplicar10_1 % 11
verificador_1 = int(cpf[9:10])

if resto_1 > 9:
    resultado_1 = 0
else:
    resultado_1 = resto_1

# Calculation of the second digit
somar_2 = sum(int(cpf[i]) for i in range(10))
multiplicar_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
multiplicar10_2 = multiplicar_2 * 10
resto_2 = multiplicar10_2 % 11
verificador_2 = int(cpf[10:11])

if resto_2 > 9:
    resultado_2 = 0
else:
    resultado_2 = resto_2

# Verifier
if resultado_1 != verificador_1 or resultado_2 != verificador_2:
    print("The entered CPF is not valid")
else:
    print("The entered CPF is valid")

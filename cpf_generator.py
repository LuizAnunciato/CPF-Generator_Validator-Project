import random  # We import the random library

# Generation of the first 9 digits
nove_digitos = ''  # CPF without the last two digits
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

# Calculation of the first verification digit
multiplicar_1 = sum(int(nove_digitos[i]) * (10 - i) for i in range(9))
resto_1 = multiplicar_1 % 11
resultado_1 = 0 if resto_1 < 2 else 11 - resto_1

# Calculation of the second verification digit (including the first calculated digit)
multiplicar_2 = sum(int(nove_digitos[i]) * (11 - i)
                    for i in range(9)) + (resultado_1 * 2)
resto_2 = multiplicar_2 % 11
resultado_2 = 0 if resto_2 < 2 else 11 - resto_2

# Displays the complete CPF
cpf_completo = nove_digitos + str(resultado_1) + str(resultado_2)
print(f"Generated CPF: {cpf_completo}")

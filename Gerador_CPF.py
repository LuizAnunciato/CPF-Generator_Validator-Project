import random  # Importamos a biblioteca random

# Geração dos 9 primeiros dígitos
nove_digitos = ''  # CPF sem os dois últimos dígitos
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

# Cálculo do primeiro dígito verificador
multiplicar_1 = sum(int(nove_digitos[i]) * (10 - i) for i in range(9))
resto_1 = multiplicar_1 % 11
resultado_1 = 0 if resto_1 < 2 else 11 - resto_1

# Cálculo do segundo dígito verificador (incluindo o primeiro dígito calculado)
multiplicar_2 = sum(int(nove_digitos[i]) * (11 - i)
                    for i in range(9)) + (resultado_1 * 2)
resto_2 = multiplicar_2 % 11
resultado_2 = 0 if resto_2 < 2 else 11 - resto_2

# Exibe o CPF completo
cpf_completo = nove_digitos + str(resultado_1) + str(resultado_2)
print(f"CPF gerado: {cpf_completo}")

salario_usuario = float (input ("Qual o seu salário: "))
if salario_usuario >= 5000:
    print("Seu abono salarial será de 10%")
    abono_salarial1 = salario_usuario * 0.10
    print(abono_salarial1 + salario_usuario)
else:
    print("Seu abono salarial será de 15%")
    abono_salarial2 = salario_usuario * 0.15
    print(abono_salarial2 + salario_usuario)
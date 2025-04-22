salariomin= float(input("DIGITE O SALÁRIO MÍNIMO: "))
while True:
    salario = float(input("DIGITE O SALÁRIO QUE VC RECEBE: "))
    if salario == 0:
        print("Programa Terminado!")
        break
    else:
        resultado = salario / salariomin
        print(f"Você recebe {resultado} salários mínimos!")



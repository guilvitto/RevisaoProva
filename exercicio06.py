peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
imc = peso/(altura*altura)
print(imc)
if imc < 18.6:
    print("Abaixo  do peso!")
elif imc >= 18.6 and imc<= 24.9:
    print("Peso ideal!")
elif imc >= 25 and imc <= 29.9:
    print("Levemente acima do peso!")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade Grau I!")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade  Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)!")





repetir="sim"
while repetir=="sim":
    num = float(input('Digite um valor qualquer: '))
    if num%2==0:
        print("É par!",end=" ")
    else:
        print("É impar!",end=" ")
    if num<0:
        print('É negativo!',end=" ")
    else:
        print("É positivo!")
    repetir=input("Deseja repetir? (sim) ou (nao): ")

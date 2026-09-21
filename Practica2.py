S = int(input("Saldo: "))
M = int(input("¿Cuanto va a retirar?: "))
if (M % 50 != 0):
    print("MONTO NO VALIDO")
elif (M > S):
    print("SALDO INSUFICIENTE")
elif (M > 6000):
    print("LIMITE DIARIO EXCEDIDO")
else:
    NS = S-M
    print("ENTREGADO")
    print("Saldo:", NS)

import time

hora = time.localtime()[3]
print("Fecha es: ", time.strftime("%c"))

if hora > time.strptime("19:00"[:2],"%H")[3]:
    print("Hora de ir a casa")
else:
    tiempo_restante = time.strptime("19:00"[:2], "%H")[3] - hora
    print("El tiempo restante es: ", tiempo_restante, " hora/s")
'''
Una compañía de alquiler de automóviles desea adquirir un programa para emitir
sus facturas, con las siguientes consideraciones:
a. Se factura una cantidad fija de 100EUR si no se rebasan los 300 Km.
b. Si la distancia recorrida es mayor que 300 Km, entonces:
i. Si la distancia es menor o igual que 1.000 Km, se cobrarán 100EUR
más el kilometraje que exceda de 300 Km, a razón de 30
céntimos/Km.
ii. Si la distancia es mayor que 1.000 Km, se cobrarán los 100EUR más
el kilometraje a razón de 30 céntimos/Km para los kilómetros entre
el 300 y el 1.000 y 20 céntimos/Km para el resto.
'''
try:
    distancia = float(input("Introduzca la distancia:"))
except:
    print("Vuelva a introducir un valor correcto")

facturacion = 100
facturacion1 = facturacion + (0.30 * (distancia-300))
facturacion2 = facturacion + (700 * 0.30) +(0.20 * (distancia-1000))
if distancia <= 300:
    print(f'Ha facturado {facturacion}€')
else:
    if distancia <= 1000:
        print(f"Ha facturado {facturacion1}€")
    else:
        print(f"Ha facturado {facturacion2}€")




import requests
import time

url = 'https://www.coingecko.com/es/monedas/bitcoin/historical_data/usd?end_date=2021-05-13&start_date=2004-01-01'
r = requests.get(url)
strings = r.text.split('<th class="text-center">Cerrar</th>')[1].split('<div class="dropdown mt-2">')[0].replace(
    '<th scope="row" class="font-semibold text-center">', '#')
strings = strings.replace("\n", " ").replace(" </tr> </thead> <tbody> <tr> ", "").replace('</td> </tr> <tr>',
                                                                                          "\n").replace(
    "</td> </tr> </tbody> </table>", "").replace('</th> <td class="text-center"> ', ';').replace(
    ' </td> <td class="text-center"> ', ';').replace(' </td> </tr>  <tr> ', '\n').replace(
    ' </td>  <td class="text-center"> ', ';').replace(' </td>  </tr> <tr> ', '\n').replace(
    '</th>  <td class="text-center"> ', ';').replace(' #', '#').replace(" $", "")
strings = strings.replace(".", "").replace(" \n", "").replace("N/A", "").split("#")[: :-1]
# Fecha 	Cap. de mercado 	Volumen 	Abrir 	Cerrar
# empezamos a leer
inicio = 0
final = 20
longitud = len(strings)
print(strings)
print("longitud", strings)
while final < longitud :
    patronseleccionado = strings[inicio :final]
    # time.sleep(2)
    inicio = inicio + 1
    final = final + 1
    # patronseleccionado es cada patrón
    # print(str(inicio) + "-" + str(final) + "-" + str(longitud) + " " + str(patronseleccionado))
    # print(patronseleccionado)
    print("---")
    for elemento in patronseleccionado :
        # print (elemento)
        elemento = elemento.split(";")
        fecha = elemento[0]
        capitalizacion = elemento[1]
        volumen = elemento[2]
        apertura = elemento[3]
        cierre = elemento[4]
        print (fecha, capitalizacion, volumen, apertura, cierre)

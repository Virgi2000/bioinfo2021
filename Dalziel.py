# FUNCIÓN 1. Cálculo de infecciones promedio por ciudad

import pandas as pd


# Se crea la función "avgcity" cuyos argumentos son: city, my_csv(a ruta de la lectura del archivo.csv)
def avgcity(city, my_csv):
    """
    función para extraer el valor promedio de infecciones por ciudad
    """
    # primero se crea un directorio vacio 
    citypop = {}
    # se usa el bucle for, para cada una de las lineas que hay en la data "my_csv":
    for line in my_csv:
        # identtifico la linea que correscponde a la localidad
        mycity = line['loc']
        # asegurar que cada linea donde se encuentre la población se transforme en un número real "float"
        pop = float(line['pop'])
        # solamente si el número de casos es diferente al "NA", ejecuta lo siguiente:
        if line['cases'] != "NA":
            # se usa el float para asegurarnos que cada linea de casos sean considerados como números decimales
            case = float(line['cases'])
            # se crea una respuesta que tenga 3 niveles en el diccionario para cada localidad 
            citypop[mycity] = citypop.get(mycity, [0,0,0])
            # el primer nivel "posición 0" donde se suma los valores de población
            citypop[mycity][0] = citypop[mycity][0] + pop
            # el segundo nivel "posición 1" donde se suma y se guarda el número de casos
            citypop[mycity][1] = citypop[mycity][1] + case
            # el tercer nivel "posición 2" donde se guarda el conteo de cuantas veces se cumple esa condición
            citypop[mycity][2] = citypop[mycity][2] + 1
    # ingresar por el identificador "key" los valores que estan en el citypop
    for key in citypop:
        # solamente si el "key" es exactamente correspondiente a la ciudad, entonces:
        if key == city:
            # se calcula el promedio de casos, para que sea un número legible se multiplica por 10^5,
            # lo cual daría un valor por cada 100 mil habitantes.
            avg_case = 100000*citypop[key][1]/citypop[key][0]
            # el resultado retorna el valor de "key" junto al "avg_case"
            return print(key, avg_case)
          
# FUNCIÓN 2. Cáculo de la infecciones promedio por año, la desviación estándar y número de registros

import pandas as pd
import numpy as np

def avgyearr(year, my_csv):
    """
    función para extraer el valor promedio de infecciones por año
    """
    
    yearpop = {}
    for line in my_csv:
        myyear = line['year']
        pop = float(line['pop'])
        if line['cases'] != "NA":
            case = float(line['cases'])
            yearpop[myyear] = yearpop.get(myyear, [0,0,0])
            yearpop[myyear][0] = yearpop[myyear][0] + pop
            yearpop[myyear][1] = yearpop[myyear][1] + case
            yearpop[myyear][2] = yearpop[myyear][2] + 1
    for key in yearpop:
        if key == year:
            avg_year = 100000*yearpop[key][1]/yearpop[key][0]
            return print(key, avg_year)
        
# FUNCIÓN 3. Cálculo de la infecciones promedio por semana, la desviación estándar y número de registros

import pandas as pd

def avgbiweeks(biweek, my_csv):
    """
    función para extraer el valor promedio de infecciones por semana
    """
    biweekpop = {}
    for line in my_csv:
        mycity = line['loc']
        mybiweek= line['biweek']
        pop = float(line['pop'])
        if line['cases'] != "NA":
            case = float(line['cases'])
            biweekpop[mybiweek] = biweekpop.get(mybiweek, [0,0,0])
            biweekpop[mybiweek][0] = biweekpop[mybiweek][0] + pop
            biweekpop[mybiweek][1] = biweekpop[mybiweek][1] + case
            biweekpop[mybiweek][2] = biweekpop[mybiweek][2] + 1
    for key in biweekpop:
        if key == biweek:
            avg_case = 100000*biweekpop[key][2]/biweekpop[key][1]
            return print(key, avg_case)
        



            

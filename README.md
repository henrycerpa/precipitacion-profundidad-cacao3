# PYTHON BASICO 
## PRACTICA 3
## Estudio de condiciones para plantaciones de cacao

En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Para el 2030, se busca luchar contra la desertificación, rehabilitar las tierras y los suelos degradados, incluidas de las tierras afectadas por la desertificación, la sequía y las inundaciones, y procurar lograr un mundo con una degradación neutra del suelo.

El Ministerio de Agricultura y Desarrollo Rural busca recuperar los suelos para el cultivo del cacao. Para poder cumplir con esto han iniciado el análisis para las características del entorno donde se tiene previsto iniciar las plantaciones. Para esta tarea lo requieren a usted y se facilita una tabla que describe si el entorno es apto o no.

| CARACTERISTICAS | SUMAMENTE APTO | MODERADAMENTE APTO | MARGINALMENTE APTO | NO APTO |
| --- | --- | --- | --- | --- |
| Altura sobre el nivel del mar (m.s.n.m) | 400 - 800 | < 400 o 801 - 999 | 1000 - 1200 | > 1200 |
| Temperatura media anual (°C) | 25 - 28 | 29 - 30 o 24 - 21 | 31 - 32 o 20 - 18 | < 18 o > 32 |
| Precipitación anual (mm) | 1800 - 2599 | 2600 - 3199 o 1799 - 1500	| 3200 - 3800 o 1499 - 1200 |	< 1200 o > 3800 |
| Profundidad efectiva del suelo (cm)	| > 100	| 50 - 100	| 25 - 50	| < 25 |

Para esta nueva fase se requiere un estudio más a fondo. Ahora programa leerá dos listados por zonas estudiadas. El primer listado serán valores correspondientes a la precipitación anual y el segundo serán valores correspondientes a la profundidad efectiva del suelo. Para cada listado usted deberá:

-	Calcular el promedio y formatearlo a dos cifras decimales
- Imprimir los promedios calculados en una misma línea separados por espacio

A partir de los promedios se debe realizar el análisis de la calidad del suelo e indicar el conteo de los resultados obtenidos.
El número de zonas que el programa tendrá en cuenta debe ser una variable de entrada.
El criterio para la conclusión será el siguiente:

-	Si ambas variables se encuentran dentro de la misma categoría se escogerá la categoría.
-	Si están en categorías diferentes se escogerá la peor de ellas.


Ejemplo 1:
| Entrada esperada | Salida esperada |
| --- | --- |
| 5	| 1905.50 2265.25 2622.25 2399.25 1903.50 |
| 2700 2069 1591 1262	| 54.50 84.50 47.50 82.75 52.75 |
| 104 56 40 18	| sumamente apto 0 |
| 2726 1472 3724 1139	| moderadamente apto 4 |
| 52 98 79 109	| marginalmente apto 1 |
| 2115 2865 3890 1619	| no apto 0 |
| 27 21 89 53 |  |
| 1432 2161 2469 3535 |  |
| 95 103 35 98 |  |
| 1119 2323 1293 2879 |  |
| 73 50 69 19 |  |


Ejemplo 2:
| Entrada esperada | Salida esperada |
| --- | --- |
| 4	| 2565.25 2429.12 1960.12 2558.75 |
| 3415 2501 3198 2604 3279 1330 2990 1205	| 70.12 51.12 54.75 66.88 |
| 78 76 44 79 53 49 108 74	| sumamente apto 0 |
| 3223 3051 1202 1539 1251 3309 1986 3872	| moderadamente apto 4 |
| 84 20 28 42 100 75 35 25	| marginalmente apto 0 |
| 2888 1838 1719 1609 1183 3301 1531 1612	| no apto 0 |
| 71 27 64 91 46 48 51 40 |  |
| 2516 1364 3247 2498 2535 1794 3928 2588 |  |
| 55 64 109 62 77 30 62 76 |  |

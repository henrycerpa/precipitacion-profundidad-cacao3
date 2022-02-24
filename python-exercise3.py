def analisis():
    
    veces = int(input())
    listafinal_precipitacion=[]
    listafinal_profundidad=[]
    sumamente=0
    moderadamente=0
    marginalmente=0
    noapto=0
    i=1
    
    while(i <= veces):
        
        precipitacion = input()
        lista_precipitacion = precipitacion.split()
        suma_precipitacion=0
        for j in range (0, (len(lista_precipitacion))):
            valor_precipitacion = float(lista_precipitacion[j])
            suma_precipitacion = suma_precipitacion + valor_precipitacion
        promedio_precipitacion = round((suma_precipitacion / (len(lista_precipitacion))),2)
        listafinal_precipitacion.append("{:.2f}".format(promedio_precipitacion))
        
        profundidad = input()
        lista_profundidad = profundidad.split()
        suma_profundidad = 0
        for k in range (0, (len(lista_profundidad))):
            valor_profundidad = (float(lista_profundidad[k]))
            suma_profundidad = suma_profundidad + valor_profundidad
        promedio_profundidad = round((suma_profundidad / (len(lista_profundidad))),2)
        listafinal_profundidad.append("{:.2f}".format(promedio_profundidad))
        i+=1
    for l, m in zip(listafinal_precipitacion,listafinal_profundidad):
        l=float(l)
        m=float(m)
        if (1800.00 <= l <=2599.00) and (m > 100.00):
            sumamente = sumamente + 1
        elif (1800.00 <= l <=2599.00) and (50.00 <= m <= 100.00):
            moderadamente = moderadamente + 1
        elif (1800.00 <= l <=2599.00) and (25.00 <= m < 50.00):
            marginalmente = marginalmente + 1
        elif (1800.00 <= l <=2599.00) and (m < 25.00):
            noapto = noapto + 1
        elif ((2599.01 <= l <=3199.99)or(1500.00 <= l <=1799.99)) and (m > 50.00):
            moderadamente = moderadamente + 1
        elif ((2599.01 <= l <=3199.99)or(1500.00 <= l <=1799.99)) and (25.00 <= m <= 50.00):
            marginalmente = marginalmente + 1
        elif ((2599.01 <= l <=3199.99)or(1500.00 <= l <=1799.99)) and (m < 25.00):
            noapto = noapto + 1
        elif ((3200.00 <= l <=3800.00)or(1200.00 <= l <=1499.99)) and (m >= 25.00):
            marginalmente = marginalmente + 1
        elif ((3200.00 <= l <=3800.00)or(1200.00 <= l <=1499.99)) and (m < 25.00):
            noapto = noapto + 1
        elif ((1200.00 < l)or(l < 3800.00)) and (m < 25.00):
            noapto = noapto + 1
    
    print(*listafinal_precipitacion)
    print(*listafinal_profundidad)
    print("sumamente apto ",sumamente)
    print("moderadamente apto ",moderadamente)
    print("marginalmente apto ",marginalmente)
    print("no apto ",noapto)    
    
if __name__ == '__main__':
    analisis()
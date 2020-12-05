
# Estructura de cada proceso
class proceso:
    def __init__(self, identificador, burst, tiempoDeLlegada):
        self.identificador = identificador
        self.burst = burst
        self.tiempoDeLlegada = tiempoDeLlegada


# Estructura de algoritmo de calendarización Round Robin
class roundRobin:
    def __init__(self, quantum, procesos):
        self.quantum = quantum
        self.procesos = procesos

    # Método que pasa el primer elemento de una lista al 
    # final de la misma.
    # lista -> Lista de la que queremos cambiar los elementos
    # return -> La lista con los indices transformados
    def recorrer(self, lista):
        temp = lista[0]
        for i in range(len(lista)-1):
            lista[i] = lista[i+1]
        lista[len(lista)-1] = temp
        return lista
    
    def calendarizar(self):
        diagrama = []
        cola = []
        tiemposBurst = [0] * len(self.procesos) 
        tiempo = 0
        procesosLlegados = 0
        procesosTerminados = 0
        procesosListos = 0
        inicio = False

        n = len(self.procesos)

        # Se ordenan los procesos por tiempo de llegada
        self.procesos.sort(key=lambda x: x.tiempoDeLlegada)
        # Se hace una copia de los tiempos de ráfaga
        for i in range(n):
            tiemposBurst[i] = self.procesos[i].burst
        
        # Se sigue ejecutando mientras existan procesos sin terminar
        # (Ciclo principal del algoritmo)
        while(procesosTerminados < n):
            # Los procesos se agregan a la cola conforme llegan
            for i in range(procesosLlegados, len(self.procesos)):
                if tiempo >= self.procesos[i].tiempoDeLlegada:
                   cola.append(self.procesos[i])
                   procesosLlegados+=1
                   procesosListos+=1

            # En caso de que no haya procesos en la cola
            if procesosListos < 1:
                diagrama.append('')
                tiempo+=1
                continue

            # Se recorre la cola a donde comienza
            if inicio:
                cola = self.recorrer(cola)

            # Entra si el tiempo de ráfaga del primer elemento 
            # de la cola es mayor a cero
            if cola[0].burst > 0:
                # En el caso que el tiempo de ráfaga sea mayor al quantum
                if cola[0].burst > self.quantum:
                    for i in range(tiempo, tiempo+self.quantum):
                        diagrama.append(cola[0].identificador)
                    tiempo+=self.quantum
                    cola[0].burst-=self.quantum
                # Si es menor o igual al quantum
                else:
                    for i in range(tiempo, tiempo+cola[0].burst):
                        diagrama.append(cola[0].identificador)
                    tiempo+=cola[0].burst
                    cola[0].burst = 0
                    # Se registra el tiempo en que se completan
                    for i in self.procesos:
                        if i.identificador == cola[0].identificador:
                            i.tiempoCompletado = tiempo
                    procesosTerminados+=1
                    procesosListos-=1
                inicio = True
        # Se copian los tiempos de ráfaga de vuelta
        for i in range(n):
            self.procesos[i].burst = tiemposBurst[i]
        
        print(diagrama)

    # Este método calcula los tiempos de espera
    # tiemposEspera   -> Lista con los tiempos de espera de los procesos 
    # tiemposRespueta -> Lista con los tiempos de respuesta de los procesos
    def tiempoEspera(self, tiemposRespuesta, tiemposEspera):
        # Calculamos los tiempos de respuesta
        for i in range(len(self.procesos)): 
            tiemposEspera[i] = tiemposRespuesta[i] - self.procesos[i].burst

    
    # Este método calcula los tiempos de respuesta 
    # tiemposRespueta -> Lista con los tiempos de respuesta de los procesos
    def tiempoRespuesta(self, tiemposRespuesta):
        # Calculamos los tiempos de respuesta
        for i in range(len(self.procesos)): 
            tiemposRespuesta[i] = self.procesos[i].tiempoCompletado - self.procesos[i].tiempoDeLlegada


    # Función principal del algoritmo, calculamos e imprimimo los tiempos de ejecución
    def tiempoPromedio(self, plot_data):

        # Establecemos los tiempos de Espera y de Respuesta actuales
        tiemposEspera = [0] * len(self.procesos) 
        tiemposRespuesta = [0] * len(self.procesos)  

        #Calendarizamos los procesos
        self.calendarizar()

        # Calculamos los tiempos de respuesta  
        self.tiempoRespuesta(tiemposRespuesta) 

        # Calculamos los tiempos de espera 
        self.tiempoEspera(tiemposRespuesta, tiemposEspera)   
    
        # Mostramos los resultados obtenidos 
        total_tiemposEspera = 0
        total_tiemposRespuesta = 0
        print("Resultados algoritmos de calendarización Round-Robin\n")
        print("Procesos IDs\tTiempos de Burst\tTiempos de Llegada\tTiempos de Espera\t\tTiempos de Respuesta")  
        # Para cada proceso
        for i in range(len(self.procesos)):
            # Añadimos su tiempo de espera y de respuesta al tiempo total
            total_tiemposEspera = total_tiemposEspera + tiemposEspera[i]  
            total_tiemposRespuesta = total_tiemposRespuesta + tiemposRespuesta[i]  
            print(str(self.procesos[i].identificador) + "\t\t" + str(self.procesos[i].burst) + "\t\t\t" +  str(self.procesos[i].tiempoDeLlegada) + "\t\t\t" + str(tiemposEspera[i]) + "\t\t\t\t" + str(tiemposRespuesta[i])) 
        print("\nTiempo de espera promedio: \t" +   str(total_tiemposEspera /len(self.procesos)))
        print("Tiempo de respuesta promedio: \t"+ str(total_tiemposRespuesta / len(self.procesos)))
        plot_data.append([total_tiemposEspera / len(self.procesos)]) 
        plot_data.append([total_tiemposRespuesta / len(self.procesos)])

    
# Estructura de algoritmo de Shortest Remaining Time First
class SRTF:
    def __init__(self, procesos):
        self.procesos = procesos
 
    def tiempoEspera(self, tiemposEspera):  
        cantProcesos = len(self.procesos)
        tiempoRestante = [0] * cantProcesos 
    
        # Copiamos los tiempos de ráfaga   
        for i in range(cantProcesos):  
            tiempoRestante[i] = self.procesos[i].burst 

        terminados = 0      # Procesos terminados
        tiempoActual = 0    # Tiempo actual
        minimo = 999999999  # Tiempo restante minimo 
        index = 0           # Indice de proceso seleccionado
        aux = False         # Variable auxiliar para
                            # encontrar el proceso con
                            # el tiempo restante mínimo
    
        # Ciclo principal del algoritmo
        while (terminados != cantProcesos): 
            
            # Encontramos el proceso con el menor tiempo
            # restante de los que han llegado hasta el 
            # tiempo actual
            for j in range(cantProcesos): 
                if ((self.procesos[j].tiempoDeLlegada <= tiempoActual) and (tiempoRestante[j] < minimo) and tiempoRestante[j] > 0): 
                    minimo = tiempoRestante[j] 
                    index = j 
                    aux = True
            if (aux == False): 
                tiempoActual += 1
                continue
                
            # Actualizamos el tiempo restante  
            tiempoRestante[index] -= 1
    
            # Actualizamos el tiempo restante minimo
            minimo = tiempoRestante[index]  
            if (minimo == 0):  
                minimo = 999999999
    
            # Si un proceso termina de ejecutarse 
            if (tiempoRestante[index] == 0):  
    
                # Aumentamos la cantidad de procesos completados  
                terminados += 1
                aux = False

                # Definimos el tiempo de finalización del proceso actual
                tiempoFin = tiempoActual + 1
    
                # Calculamos el tiempo de espera
                tiemposEspera[index] = (tiempoFin - self.procesos[index].burst - self.procesos[index].tiempoDeLlegada) 
    
                if (tiemposEspera[index] < 0): 
                    tiemposEspera[index] = 0
            
            # Aumentamos el tiempo actual  
            tiempoActual += 1
    
    # Este método calcula los tiempos de respuesta 
    # tiemposEspera   -> Lista con los tiempos de espera de los procesos 
    # tiemposRespueta -> Lista con los tiempos de respuesta de los procesos  
    def tiempoRespuesta(self, tiemposEspera, tiemposRespuesta):  
        # Calculamos los tiempos de respuesta 
        for i in range(len(self.procesos)): 
            tiemposRespuesta[i] = self.procesos[i].burst + tiemposEspera[i]  
    
    # Función principal del algoritmo, calculamos e imprimimo los tiempos de ejecución 
    def tiempoPromedio(self, plot_data):  
        tiemposEspera = [0] * len(self.procesos) 
        tiemposRespuesta = [0] * len(self.procesos)   
    
        # Calculamos los tiempos de espera 
        self.tiempoEspera(tiemposEspera)  
        # Calculamos los tiempos de respuesta  
        self.tiempoRespuesta(tiemposEspera, tiemposRespuesta)  
    
        # Mostramos los resultados obtenidos 
        total_tiemposEspera = 0 
        total_tiemposRespuesta = 0  
        print("Resultados de algoritmo de calendarización Shortest Remaining Time First\n")
        print("Procesos IDs\tTiempos de Burst\tTiempos de Llegada\tTiempos de Espera\t\tTiempos de Respuesta") 
        # Para cada proceso
        for i in range(len(self.procesos)):
            # Añadimos su tiempo de espera y de respuesta al tiempo total
            total_tiemposEspera += tiemposEspera[i]  
            total_tiemposRespuesta += tiemposRespuesta[i]  
            print(str(self.procesos[i].identificador) + "\t\t" + str(self.procesos[i].burst) + "\t\t\t" +  str(self.procesos[i].tiempoDeLlegada) + "\t\t\t" + str(tiemposEspera[i]) + "\t\t\t\t" + str(tiemposRespuesta[i])) 
        print("\nTiempo de espera promedio: \t" +   str(total_tiemposEspera /len(self.procesos)))
        print("Tiempo de respuesta promedio: \t"+ str(total_tiemposRespuesta / len(self.procesos))) 
        plot_data[0].append(total_tiemposEspera / len(self.procesos)) 
        plot_data[1].append(total_tiemposRespuesta / len(self.procesos)) 
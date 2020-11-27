
# Estructura de cada proceso
class proceso:
    def __init__(self, identificador, burst, tiempoDeLlegada):
        self.identificador = identificador
        self.burst = burst
        self.tiempoDeLlegada = tiempoDeLlegada
    completado = False


# Estructura de algoritmo de calendarización Round Robin
class roundRobin:
    def __init__(self, quantum, procesos):
        self.quantum = quantum
        self.procesos = procesos

    def tiempoEspera(self, tiemposEspera):
        cantProcesos = len(self.procesos)
        tiemposBurstRestante = [0] * cantProcesos
        tiempoActual = 0 # Tiempo actual 


        # Copiamos los tiempos de ráfaga  
        for i in range(cantProcesos):  
            tiemposBurstRestante[i] = self.procesos[i].burst 
        
    
        # Este ciclo recorre los procesos
        # utilizando el algoritmo Round Robin
        # hasta que todos se encuentran finalizados
        while(True): 
            # Variable para saber si un proceso
            # se encuentra en ejecución
            finalizado = True
    
            # Para cada proceso
            for i in range(cantProcesos): 
                
                # Si el tiempo de ráfaga es mayor a 0
                # sigue el proceso 
                if (tiemposBurstRestante[i] > 0) :
                    
                    # Entramos en proceso de ejecución
                    finalizado = False 
                    
                    if (tiemposBurstRestante[i] > self.quantum) : 
                    
                        # Actualizamos el tiempo actual 
                        tiempoActual += self.quantum  
    
                        # Actualizamos el tiempo de ráfaga restante
                        tiemposBurstRestante[i] -= self.quantum  
                    
                    # Si el tiempo de ráfaga restante es menor
                    # a quantum, el proceso solo necesita un ciclo
                    # más para finalizar  
                    else: 
                    
                        # Actualizamos el tiempo actual 
                        tiempoActual = tiempoActual + tiemposBurstRestante[i]  
    
                        # Actualizamos los tiempos de espera
                        tiemposEspera[i] = tiempoActual - self.procesos[i].burst  
    
                        # Actualizamos el tiempo de ráfaga restante, es 0 ya que
                        # el proceso está terminado
                        tiemposBurstRestante[i] = 0
                    
            # Si todos los procesos han terminado dejamos de ejecutar el algoritmo  
            if (finalizado == True): 
                break

    
    # Este método calcula los tiempos de respuesta 
    # tiemposEspera   -> Lista con los tiempos de espera de los procesos 
    # tiemposRespueta -> Lista con los tiempos de respuesta de los procesos
    def tiempoRespuesta(self, tiemposEspera, tiemposRespuesta):
        # Calculamos los tiempos de respuesta
        for i in range(len(self.procesos)): 
            tiemposRespuesta[i] = self.procesos[i].burst + tiemposEspera[i] 


    # Función principal del algoritmo, calculamos e imprimimo los tiempos de ejecución
    def tiempoPromedio(self):

        # Establecemos los tiempos de Espera y de Respuesta actuales
        tiemposEspera = [0] * len(self.procesos) 
        tiemposRespuesta = [0] * len(self.procesos)  
    
        # Calculamos los tiempos de espera 
        self.tiempoEspera(tiemposEspera)  
    
        # Calculamos los tiempos de respuesta  
        self.tiempoRespuesta(tiemposEspera, tiemposRespuesta)  
    
        # Mostramos los resultados obtenidos 
        total_tiemposEspera = 0
        total_tiemposRespuesta = 0
        print("Resultados algoritmos de calendarización Round-Robin\n")
        print("Procesos\tTiempos de Burst\tTiempos de Llegada\tTiempos de Espera\t\tTiempos de Respuesta") 
        # Para cada proceso
        for i in range(len(self.procesos)):
            # Añadimos su tiempo de espera y de respuesta al tiempo total
            total_tiemposEspera += tiemposEspera[i]  
            total_tiemposRespuesta += tiemposRespuesta[i]  
            print(str(i + 1) + "\t\t\t\t\t" + str(self.procesos[i].burst) + "\t\t\t\t\t\t\t\t\t" +  str(self.procesos[i].tiempoDeLlegada) + "\t\t\t\t\t\t\t\t\t\t" + str(tiemposEspera[i]) + "\t\t\t\t\t\t\t\t\t\t" + str(tiemposRespuesta[i])) 
        print("\nTiempo de espera promedio: \t\t\t" +   str(total_tiemposEspera /len(self.procesos)))
        print("Tiempo de respuesta promedio: \t"+ str(total_tiemposRespuesta / len(self.procesos)))  

    
# Estructura de algoritmo de indexest Remaining Time First
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
    def tiempoPromedio(self):  
        tiemposEspera = [0] * len(self.procesos) 
        tiemposRespuesta = [0] * len(self.procesos)   
    
        # Calculamos los tiempos de espera 
        self.tiempoEspera(tiemposEspera)  
        # Calculamos los tiempos de respuesta  
        self.tiempoRespuesta(tiemposEspera, tiemposRespuesta)  
    
        # Mostramos los resultados obtenidos 
        total_tiemposEspera = 0 
        total_tiemposRespuesta = 0  
        print("Resultados algoritmos de calendarización indexest Remaining Time First\n")
        print("Procesos\tTiempos de Burst\tTiempos de Llegada\tTiempos de Espera\t\tTiempos de Respuesta") 
        # Para cada proceso
        for i in range(len(self.procesos)):
            # Añadimos su tiempo de espera y de respuesta al tiempo total
            total_tiemposEspera += tiemposEspera[i]  
            total_tiemposRespuesta += tiemposRespuesta[i]  
            print(str(i + 1) + "\t\t\t\t\t" + str(self.procesos[i].burst) + "\t\t\t\t\t\t\t\t\t" +  str(self.procesos[i].tiempoDeLlegada) + "\t\t\t\t\t\t\t\t\t\t" + str(tiemposEspera[i]) + "\t\t\t\t\t\t\t\t\t\t" + str(tiemposRespuesta[i])) 
        print("\nTiempo de espera promedio: \t\t\t" +   str(total_tiemposEspera /len(self.procesos)))
        print("Tiempo de respuesta promedio: \t"+ str(total_tiemposRespuesta / len(self.procesos)))  
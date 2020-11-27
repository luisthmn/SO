
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
        print("Procesos\tTiempos de Burst\tTiempos de Espera\t\tTiempos de Respuesta") 
        # Para cada proceso
        for i in range(len(self.procesos)):
            # Añadimos su tiempo de espera y de respuesta al tiempo total
            total_tiemposEspera = total_tiemposEspera + tiemposEspera[i]  
            total_tiemposRespuesta = total_tiemposRespuesta + tiemposRespuesta[i]  
            print(str(i + 1) + "\t\t\t" + str(self.procesos[i].burst) + "\t\t\t\t\t" +  str(tiemposEspera[i]) + "\t\t\t\t\t\t" + str(tiemposRespuesta[i])) 
        print("\nTiempo de espera promedio: \t\t" +   str(total_tiemposEspera /len(self.procesos)))
        print("Tiempo de respuesta promedio: \t"+ str(total_tiemposRespuesta / len(self.procesos)))  

    
# Estructura de algoritmo de Shortest Remaining Time First
class SRTF:
    def __init__(self, procesos):
        self.procesos = procesos

    def tiempoEspera(self, tiemposEspera): 

        cantProcesos = len(self.procesos)
        rt = [0] * cantProcesos 
    
        # Copy the burst time into rt[]  
        for i in range(cantProcesos):  
            rt[i] = self.procesos[i][1] 
        complete = 0
        t = 0
        minm = 999999999
        short = 0
        check = False
    
        # Process until all processes gets  
        # completed  
        while (complete != n): 
            
            # Find process with minimum remaining  
            # time among the processes that  
            # arrives till the current time` 
            for j in range(n): 
                if ((processes[j][2] <= t) and 
                    (rt[j] < minm) and rt[j] > 0): 
                    minm = rt[j] 
                    short = j 
                    check = True
            if (check == False): 
                t += 1
                continue
                
            # Reduce remaining time by one  
            rt[short] -= 1
    
            # Update minimum  
            minm = rt[short]  
            if (minm == 0):  
                minm = 999999999
    
            # If a process gets completely  
            # executed  
            if (rt[short] == 0):  
    
                # Increment complete  
                complete += 1
                check = False
    
                # Find finish time of current  
                # process  
                fint = t + 1
    
                # Calculate waiting time  
                wt[short] = (fint - proc[short][1] -    
                                    proc[short][2]) 
    
                if (wt[short] < 0): 
                    wt[short] = 0
            
            # Increment time  
            t += 1
  
    # Function to calculate turn around time  
    def tiempoEspera(processes, n, wt, tat):  
        
        # Calculating turnaround time  
        for i in range(n): 
            tat[i] = processes[i][1] + wt[i]  
    
    # Function to calculate average waiting  
    # and turn-around times.  
    def tiempoPromedio(processes, n):  
        wt = [0] * n 
        tat = [0] * n  
    
        # Function to find waiting time  
        # of all processes  
        findWaitingTime(processes, n, wt)  
    
        # Function to find turn around time 
        # for all processes  
        findTurnAroundTime(processes, n, wt, tat)  
    
        # Display processes along with all details  
        print("Processes    Burst Time     Waiting",  
                        "Time     Turn-Around Time") 
        total_wt = 0
        total_tat = 0
        for i in range(n): 
    
            total_wt = total_wt + wt[i]  
            total_tat = total_tat + tat[i]  
            print(" ", processes[i][0], "\t\t",  
                    processes[i][1], "\t\t",  
                    wt[i], "\t\t", tat[i]) 
    
        print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
        print("Average turn around time = ", total_tat / n)  

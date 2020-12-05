import random
import clases

#Este método genera una lista de procesos 
# cantidad -> Cantidad de procesos que se generaran
# minBurst -> Tiempo mínimo de ráfaga que puede tener un proceso
# maxBurst -> Tiempo máximo de ráfaga que puede tener un proceso
# maxTime  -> Tiempo de llegada máximo que puede tener un proceso
def generaProcesos(cantidad, minBurst, maxBurst, maxTime):

    listaProc = []
    for i in range(0, cantidad):
        # Generamos un tiempo de llegada y de burst aleatorio
        # para cada proceso
        burstRand = random.randint(minBurst, maxBurst)
        timeRand = random.randint(0, maxTime)

        proceso = clases.proceso(i, burstRand, timeRand)
        # Agregamos nuestro proceso a la lista
        listaProc.append(proceso)

    # Regresamos la lista de los procesos generados
    return listaProc





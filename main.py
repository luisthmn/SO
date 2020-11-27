import numpy
import metodos
import clases

cantidad = 4
minBurst = 1
maxBurst = 5
maxTiempoLlegada = 4
# Generamos nuestra lista de procesos
procesos = metodos.generaProcesos(cantidad, minBurst, maxBurst, maxTiempoLlegada)

# Mostramos la información de los elementos
print("\nProcesos:\n")
for elem in procesos:
    print("id: " + str(elem.identificador) + "\t\t" + " burst: " + str(elem.burst) + "\t\t" + "Tiempo de llegada: " + str(elem.tiempoDeLlegada))
print("\n\n")

quantum = 2
# Utilizamos el algoritmo de calendarización RoundRobin
roundRobin = clases.roundRobin(quantum, procesos)
roundRobin.tiempoPromedio()

# Utilizamos el algoritmo de calendarización Shortest Remaining Time First
srtf = clases.SRTF(procesos)
srtf.tiempoPromedio()
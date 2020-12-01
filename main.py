import numpy
import metodos
import clases

print("Proyecto final para la materia de Sistemas Operativos\n\n")

# Solicitamos información al usuario
cantidad = int(input("Cuantos procesos desea generar: "))
minBurst = int(input("Tiempo de ráfaga mínimo posible para un proceso: "))
maxBurst = int(input("Tiempo de ráfaga máximo posible para un proceso: "))
maxTiempoLlegada = int(input("Máximo tiempo de llegada de un proceso: "))
quantum = int(input("Valor de quantum para el algoritmo de calendarización Round Robin: "))


# Generamos nuestra lista de procesos
procesos = metodos.generaProcesos(cantidad, minBurst, maxBurst, maxTiempoLlegada)

# Mostramos la información de los elementos
print("\nProcesos:\n")
for elem in procesos:
    print("id: " + str(elem.identificador) + "\t\t" + " burst: " + str(elem.burst) + "\t\t" + "Tiempo de llegada: " + str(elem.tiempoDeLlegada))
print("\n\n")

# Utilizamos el algoritmo de calendarización RoundRobin
roundRobin = clases.roundRobin(quantum, procesos)
roundRobin.tiempoPromedio()
print("\n")

# Utilizamos el algoritmo de calendarización Shortest Remaining Time First
srtf = clases.SRTF(procesos)
srtf.tiempoPromedio()
import time
import threading


def sequential_part():
    time.sleep(0.3)  # Simula el 30% del tiempo total


""" Este retraso simula el 70% del tiempo total de procesamiento que se espera que tome esta parte del programa. """


def parallel_part():
    time.sleep(0.7)  # Simula el 70% del tiempo total


def run_program(num_threads):
    start_time = time.time()

    # Parte secuencial
    sequential_part()

    # Parte paralelizable
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=parallel_part)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


def amdahl_speedup(P, S):
    return 1 / ((1 - P) + (P / S))


# Parámetros
P = 0.7
S_values = [2, 4, 8, 16]

# Ejecutar el programa y calcular el speedup
results = []
for S in S_values:
    execution_time = run_program(S)
    speedup = amdahl_speedup(P, S)
    results.append((S, execution_time, speedup))

# Mostrar resultados
print("Procesadores | Tiempo de Ejecución | Speedup (Amdahl)")
for result in results:
    print(f"{result[0]:<12} | {result[1]:<18.4f} | {result[2]:<15.4f}")

# Validar la Ley de Amdahl
for result in results:
    S, execution_time, speedup = result
    expected_time = 1 / speedup
    actual_time = execution_time
    print(
        f"Procesadores: {S}, Tiempo Esperado: {expected_time:.4f}, Tiempo Real: {actual_time:.4f}"
    )
    if abs(expected_time - actual_time) < 0.1:  # Tolerancia para comparación
        print("La Ley de Amdahl se cumple.")
    else:
        print("La Ley de Amdahl no se cumple.")

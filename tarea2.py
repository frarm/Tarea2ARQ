import matplotlib.pyplot as plt

def fcfs_disk_scheduling(requests, initial_position):
    current_position = initial_position
    total_movement = 0
    movement = [initial_position]
    var_time_position = 0

    for request in requests:
        distance = abs(request - current_position)
        total_movement += distance
        current_position = request
        movement.append(current_position)
        var_time_position += 1

    return total_movement, movement, list(range(var_time_position + 1))

def sstf_disk_scheduling(requests, initial_position):
    current_position = initial_position
    total_movement = 0
    movement = [initial_position]
    var_time_position = 0

    while len(requests) > 0:
        # Buscar el siguiente request más cercano
        next_request = min(requests, key=lambda x: abs(x - current_position))
        distance = abs(next_request - current_position)
        total_movement += distance
        current_position = next_request
        movement.append(current_position)
        var_time_position += 1
        requests.remove(next_request)

    return total_movement, movement, list(range(var_time_position + 1))

def scan_disk_scheduling(requests, initial_position):
    current_position = initial_position
    total_movement = 0
    movement = [initial_position]
    var_time_position = 0

    # Ordenar los requests
    requests.sort()

    # Encontrar el índice del request más cercano
    index = requests.index(current_position)

    # Moverse a la derecha
    for i in range(index, len(requests)):
        distance = abs(requests[i] - current_position)
        total_movement += distance
        current_position = requests[i]
        movement.append(current_position)
        var_time_position += 1

    # Moverse a la izquierda
    for i in range(index - 1, -1, -1):
        distance = abs(requests[i] - current_position)
        total_movement += distance
        current_position = requests[i]
        movement.append(current_position)
        var_time_position += 1

    return total_movement, movement, list(range(var_time_position + 1))

def cscan_disk_scheduling(requests, initial_position):
    current_position = initial_position
    total_movement = 0
    movement = [initial_position]
    var_time_position = 0

    # Ordenar los requests
    requests.sort()

    # Encontrar el índice del request más cercano
    index = requests.index(current_position)

    # Moverse a la derecha
    for i in range(index, len(requests)):
        distance = abs(requests[i] - current_position)
        total_movement += distance
        current_position = requests[i]
        movement.append(current_position)
        var_time_position += 1

    # Moverse a la izquierda
    for i in range(0, index):
        distance = abs(requests[i] - current_position)
        total_movement += distance
        current_position = requests[i]
        movement.append(current_position)
        var_time_position += 1

    return total_movement, movement, list(range(var_time_position + 1))

def look_disk_scheduling(requests, initial_position):
    current_position = initial_position
    total_movement = 0
    movement = [initial_position]
    var_time_position = 0

    # Ordenar los requests
    requests.sort()

    # Encontrar el índice del request más cercano
    index = requests.index(current_position)

    # Moverse a la derecha
    for i in range(index, len(requests)):
        distance = abs(requests[i] - current_position)
        total_movement += distance
        current_position = requests[i]
        movement.append(current_position)
        var_time_position += 1

    # Moverse a la izquierda
    for i in range(index - 1, -1, -1):
        distance = abs(requests[i] - current_position)
        total_movement += distance
        current_position = requests[i]
        movement.append(current_position)
        var_time_position += 1

    return total_movement, movement, list(range(var_time_position + 1))


requests = [100, 150, 50, 150, 24, 0, 190]
initial_position = 50

# planificación de disco para FCFS
total_movement_fcfs, movement_fcfs, var_time_position_fcfs = fcfs_disk_scheduling(requests.copy(), initial_position)

# planificación de disco para SSTF
total_movement_sstf, movement_sstf, var_time_position_sstf = sstf_disk_scheduling(requests.copy(), initial_position)

# planificación de disco para SCAN
total_movement_scan, movement_scan, var_time_position_scan = scan_disk_scheduling(requests.copy(), initial_position)

# planificación de disco para CSCAN
total_movement_cscan, movement_cscan, var_time_position_cscan = cscan_disk_scheduling(requests.copy(), initial_position)

# planificación de disco para LOOK
total_movement_look, movement_look, var_time_position_look = look_disk_scheduling(requests.copy(), initial_position)

# imprime los resultados
print('FCFS: ', total_movement_fcfs)
print('SSTF: ', total_movement_sstf)
print('SCAN: ', total_movement_scan)
print('CSCAN: ', total_movement_cscan)
print('LOOK: ', total_movement_look)

# gráficos
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs[0, 0].plot(movement_fcfs, var_time_position_fcfs, 'tab:blue')
axs[0, 0].set_title('FCFS')
axs[0, 0].set(xlabel='Posicion', ylabel='Variacion Tiempo/Posicion')
axs[0, 1].plot(movement_sstf, var_time_position_sstf, 'tab:orange')
axs[0, 1].set_title('SSTF')
axs[0, 1].set(xlabel='Posicion', ylabel='Variacion Tiempo/Posicion')
axs[0, 2].plot(movement_scan, var_time_position_scan, 'tab:green')
axs[0, 2].set_title('SCAN')
axs[0, 2].set(xlabel='Posicion', ylabel='Variacion Tiempo/Posicion')
axs[1, 0].plot(movement_cscan, var_time_position_cscan, 'tab:red')
axs[1, 0].set_title('CSCAN')
axs[1, 0].set(xlabel='Posicion', ylabel='Variacion Tiempo/Posicion')
axs[1, 1].plot(movement_look, var_time_position_look, 'tab:purple')
axs[1, 1].set_title('LOOK')
axs[1, 1].set(xlabel='Posicion', ylabel='Variacion Tiempo/Posicion')
axs[1, 2].axis('off')  # Ocultar el último gráfico
plt.show()
 

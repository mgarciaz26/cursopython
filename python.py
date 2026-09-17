titulo = "Usuario sin acceso al reporte de QlikSense"
dias_abierto = 3
severidad = "Alta"
resuelto = "Listo"
asignado_a = "Equipo BI"

if severidad == "Alta":                             #Nivel 0
    if dias_abierto > 3:                            #Nivel 1
        estado_prioridad = "Crítico"                #Nivel 2
    else:                                           #Nivel 1
        estado_prioridad = "Alta prioridad"         #Nivel 2
else:                                               #Nivel 0
    if dias_abierto > 7:                            #Nivel 1
        estado_prioridad = "Atender esta semana"    #Nivel 2
    else:                                           #Nivel 1
        estado_prioridad = "Puede esperar"          #Nivel 2    

mensaje = f"{titulo} - Severidad: {severidad}, {dias_abierto} días abierto, Ticket asignado al {asignado_a}, Estado: {resuelto}, Prioridad: {estado_prioridad}"

print(mensaje)
print("Niveles de indentación utilizados en la lógica: 2")
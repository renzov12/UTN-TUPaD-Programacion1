# Agenda con tuplas como clave
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:30"): "Gimnasio"
}

# Consultar día y hora
dia = input("Ingrese un día: ").lower()
hora = input("Ingrese una hora (ejemplo 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad agendada: {agenda[clave]}")
else:
    print("No hay actividad en ese día y hora.")

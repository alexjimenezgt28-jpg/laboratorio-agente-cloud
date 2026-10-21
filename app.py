from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
agregar_tarea(tareas, "Preparar exposición", "Laboratorio")
completar_tarea(tareas, 1)

print("Tareas pendientes:")
for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

print("Pendientes de Laboratorio:")
for tarea in pendientes(tareas, "laboratorio"):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

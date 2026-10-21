CATEGORIA_POR_DEFECTO = "General"


def agregar_tarea(tareas, titulo, categoria=CATEGORIA_POR_DEFECTO):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    categoria = categoria.strip()
    if not categoria:
        raise ValueError("La categoría es obligatoria")
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def pendientes(tareas, categoria=None):
    pendientes_actuales = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return pendientes_actuales
    buscada = categoria.strip().lower()
    return [t for t in pendientes_actuales if t["categoria"].strip().lower() == buscada]

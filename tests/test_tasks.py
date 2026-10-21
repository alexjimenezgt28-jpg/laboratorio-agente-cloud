import unittest

from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])


class TestCategorias(unittest.TestCase):
    def test_categoria_valida(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
        self.assertEqual(tarea["categoria"], "Laboratorio")

    def test_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Sin categoría", "   ")
        self.assertEqual(tareas, [])

    def test_filtrado_por_categoria_sin_distinguir_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar", "Estudio")
        agregar_tarea(tareas, "Preparar", "Laboratorio")
        agregar_tarea(tareas, "Exponer", "LABORATORIO")

        resultado = pendientes(tareas, "laboratorio")

        self.assertEqual([t["titulo"] for t in resultado], ["Preparar", "Exponer"])

    def test_filtrado_categoria_inexistente_devuelve_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar", "Estudio")

        self.assertEqual(pendientes(tareas, "Cocina"), [])

    def test_filtrado_categoria_en_blanco_devuelve_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar", "Estudio")

        self.assertEqual(pendientes(tareas, "   "), [])


class TestEliminarTarea(unittest.TestCase):
    def test_eliminar_tarea_existente(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar", "Estudio")
        agregar_tarea(tareas, "Preparar", "Laboratorio")

        eliminada = eliminar_tarea(tareas, 1)

        self.assertEqual(eliminada["titulo"], "Estudiar")
        self.assertEqual([t["id"] for t in tareas], [2])
        self.assertEqual(pendientes(tareas, "Estudio"), [])

    def test_eliminar_tarea_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar", "Estudio")

        with self.assertRaises(ValueError) as contexto:
            eliminar_tarea(tareas, 99)

        self.assertEqual(str(contexto.exception), "Tarea no encontrada")
        self.assertEqual(len(tareas), 1)

    def test_id_no_se_reutiliza_despues_de_eliminar(self):
        tareas = []
        agregar_tarea(tareas, "Uno", "General")
        agregar_tarea(tareas, "Dos", "General")
        eliminar_tarea(tareas, 2)

        nueva = agregar_tarea(tareas, "Tres", "General")

        self.assertEqual(nueva["id"], 3)


if __name__ == "__main__":
    unittest.main()

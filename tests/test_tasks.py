import unittest

from tasks import agregar_tarea, completar_tarea, pendientes


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


if __name__ == "__main__":
    unittest.main()

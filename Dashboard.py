# Dashboard.py

class Proyecto:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__tareas = []

    def agregar_tarea(self, tarea):
        self.__tareas.append(tarea)

    def mostrar_proyecto(self):
        print(f"\n📁 Proyecto: {self.__nombre}")
        for tarea in self.__tareas:
            print(tarea.mostrar_info())


class Tarea:
    def __init__(self, titulo, descripcion):
        self._titulo = titulo
        self._descripcion = descripcion
        self._estado = False

    def completar(self):
        self._estado = True

    def mostrar_info(self):
        estado = "✅ Completada" if self._estado else "❌ Pendiente"
        return f"Tarea: {self._titulo}\nDescripción: {self._descripcion}\nEstado: {estado}\n"


class Subtarea(Tarea):
    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"🔹 Subtarea:\n{base_info}"


if __name__ == "__main__":
    print("📌 Bienvenido a tu Dashboard de Proyectos POO")

    mi_proyecto = Proyecto("Mi Proyecto Final de POO")

    tarea1 = Tarea("Diseñar la estructura", "Definir clases y relaciones")
    tarea2 = Subtarea("Implementar métodos", "Agregar funciones personalizadas")
    tarea3 = Tarea("Documentar el código", "Comentar cada parte del programa")

    tarea2.completar()

    mi_proyecto.agregar_tarea(tarea1)
    mi_proyecto.agregar_tarea(tarea2)
    mi_proyecto.agregar_tarea(tarea3)

    mi_proyecto.mostrar_proyecto()

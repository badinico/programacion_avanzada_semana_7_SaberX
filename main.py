"""
Biblioteca SaberX - Sistema de Registro de Libros
Aplicación con arquitectura DDD y interfaz gráfica Tkinter
"""

from infrastructure.gui_interface import BookRegistrationGUI


def main():
    """Función principal de la aplicación"""
    try:
        # Crear y ejecutar la interfaz gráfica
        app = BookRegistrationGUI()
        app.run()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")


if __name__ == "__main__":
    main()

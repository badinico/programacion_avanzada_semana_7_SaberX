# Biblioteca SaberX - Sistema de Registro de Libros

Sistema de registro de libros con interfaz gráfica desarrollado usando arquitectura Domain-Driven Design (DDD) y Tkinter.

## Características

- **Interfaz gráfica completa** con todos los widgets solicitados
- **Arquitectura DDD** bien estructurada
- **Validaciones robustas** de datos de entrada
- **Diseño responsivo** con scroll para formularios grandes
- **Manejo de errores** comprehensivo

## Estructura del Proyecto

```
programacion_avanzada_semana_7_SaberX/
├── application/
│   ├── __init__.py
│   └── use_cases.py          # Casos de uso de la aplicación
├── domain/
│   ├── __init__.py
│   ├── dto.py               # Data Transfer Objects
│   ├── entities.py          # Entidades del dominio
│   └── value_objects.py     # Objetos de valor del dominio
├── infrastructure/
│   ├── __init__.py
│   ├── cli_input_output.py  # (vacío)
│   └── gui_interface.py     # Interfaz gráfica Tkinter
├── main.py                  # Punto de entrada principal
└── README.md               # Esta documentación
```

## Widgets Implementados

### Frames
- Frame principal con scroll
- Frame para detalles del libro
- Frame para género y categoría
- Frame para estado de disponibilidad
- Frame para número de copias
- Frame para resumen
- Frame para idioma
- Frame para botones de acción

### Labels y Entry
- Título del libro
- Autor
- Año de publicación
- Número de copias

### Radiobuttons
- Género: Ficción / No Ficción
- Estado: Disponible / Prestado

### Checkbuttons
- Categorías: Novela, Ciencia, Historia, Poesía, Biografía, Tecnología

### Text Widget
- Resumen del libro (con scroll automático)

### Menú Desplegable (Combobox)
- Idiomas: Español, Inglés, Francés, Alemán

### Buttons
- "Registrar Libro": Procesa y guarda la información
- "Limpiar": Resetea todos los campos

## Funcionalidades

### Validaciones
- Campos obligatorios
- Validación de tipos de datos
- Rangos permitidos (año 1-2024, copias 0-1000)
- Longitudes máximas de texto
- Al menos una categoría seleccionada

### Registro de Libros
- Al presionar "Registrar Libro", se muestra la información completa en la terminal
- Mensaje de confirmación en la interfaz
- Limpieza automática del formulario tras registro exitoso

### Limpiar Formulario
- Resetea todos los campos a valores por defecto
- Deselecciona todas las categorías
- Restaura valores iniciales de radiobuttons

## Ejecución

   ```bash
   python main.py
   ```

## Arquitectura DDD

### Domain Layer (Dominio)
- **Entities**: `Book` - Entidad principal del sistema
- **Value Objects**: Objetos inmutables como `BookTitle`, `Author`, etc.
- **DTOs**: Para transferencia de datos entre capas

### Application Layer (Aplicación)
- **Use Cases**: `BookRegistrationUseCase` - Lógica de negocio

### Infrastructure Layer (Infraestructura)
- **GUI Interface**: Implementación de la interfaz gráfica con Tkinter

## Ejemplo de Uso

1. **Ejecutar la aplicación**: `python main.py`
2. **Llenar los campos obligatorios**:
   - Título: "Cien años de soledad"
   - Autor: "Gabriel García Márquez"
   - Año: "1967"
   - Copias: "5"
3. **Seleccionar opciones**:
   - Género: Ficción
   - Categorías: Novela
   - Estado: Disponible
   - Idioma: Español
4. **Agregar resumen** (opcional)
5. **Presionar "Registrar Libro"**
6. **Verificar información en la terminal**

## Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter** - Interfaz gráfica
- **Dataclasses** - Estructuras de datos
- **Enums** - Valores constantes
- **Type Hints** - Tipado estático

## Arquitectura Hexagonal

El proyecto sigue los principios de arquitectura hexagonal:
- **Dominio** independiente de la infraestructura
- **Casos de uso** como orquestadores
- **Infraestructura** intercambiable
- **Separación clara de responsabilidades**

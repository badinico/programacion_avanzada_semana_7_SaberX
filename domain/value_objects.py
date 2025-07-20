from enum import Enum
from dataclasses import dataclass
from typing import Set


class Genre(Enum):
    """Género del libro"""
    FICTION = "Ficción"
    NON_FICTION = "No Ficción"


class Category(Enum):
    """Categoría del libro"""
    NOVEL = "Novela"
    SCIENCE = "Ciencia"
    HISTORY = "Historia"
    POETRY = "Poesía"
    BIOGRAPHY = "Biografía"
    TECHNOLOGY = "Tecnología"


class Language(Enum):
    """Idioma del libro"""
    SPANISH = "Español"
    ENGLISH = "Inglés"
    FRENCH = "Francés"
    GERMAN = "Alemán"


class AvailabilityStatus(Enum):
    """Estado de disponibilidad del libro"""
    AVAILABLE = "Disponible"
    BORROWED = "Prestado"


@dataclass(frozen=True)
class BookTitle:
    """Título del libro"""
    value: str
    
    def __post_init__(self):
        if not self.value or not self.value.strip():
            raise ValueError("El título no puede estar vacío")
        if len(self.value.strip()) > 200:
            raise ValueError("El título no puede exceder 200 caracteres")


@dataclass(frozen=True)
class Author:
    """Autor del libro"""
    value: str
    
    def __post_init__(self):
        if not self.value or not self.value.strip():
            raise ValueError("El autor no puede estar vacío")
        if len(self.value.strip()) > 100:
            raise ValueError("El nombre del autor no puede exceder 100 caracteres")


@dataclass(frozen=True)
class PublicationYear:
    """Año de publicación"""
    value: int
    
    def __post_init__(self):
        if self.value < 1 or self.value > 2024:
            raise ValueError("El año de publicación debe estar entre 1 y 2024")


@dataclass(frozen=True)
class CopiesCount:
    """Número de copias"""
    value: int
    
    def __post_init__(self):
        if self.value < 0:
            raise ValueError("El número de copias no puede ser negativo")
        if self.value > 1000:
            raise ValueError("El número de copias no puede exceder 1000")


@dataclass(frozen=True)
class BookSummary:
    """Resumen del libro"""
    value: str
    
    def __post_init__(self):
        if self.value and len(self.value) > 1000:
            raise ValueError("El resumen no puede exceder 1000 caracteres")

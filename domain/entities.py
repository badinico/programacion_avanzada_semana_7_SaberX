from dataclasses import dataclass
from typing import Set
from .value_objects import (
    BookTitle, Author, PublicationYear, Genre, Category, 
    Language, AvailabilityStatus, CopiesCount, BookSummary
)


@dataclass
class Book:
    """Entidad que representa un libro en la biblioteca"""
    title: BookTitle
    author: Author
    publication_year: PublicationYear
    genre: Genre
    categories: Set[Category]
    language: Language
    availability_status: AvailabilityStatus
    copies_count: CopiesCount
    summary: BookSummary
    
    def __post_init__(self):
        if not self.categories:
            raise ValueError("El libro debe tener al menos una categoría")
        if len(self.categories) > 5:
            raise ValueError("El libro no puede tener más de 5 categorías")
    
    def is_available(self) -> bool:
        """Verifica si el libro está disponible"""
        return self.availability_status == AvailabilityStatus.AVAILABLE
    
    def has_copies(self) -> bool:
        """Verifica si hay copias disponibles"""
        return self.copies_count.value > 0
    
    def get_display_info(self) -> str:
        """Obtiene información del libro para mostrar"""
        categories_str = ", ".join([cat.value for cat in self.categories])
        return (
            f"Título: {self.title.value}\n"
            f"Autor: {self.author.value}\n"
            f"Año: {self.publication_year.value}\n"
            f"Género: {self.genre.value}\n"
            f"Categorías: {categories_str}\n"
            f"Idioma: {self.language.value}\n"
            f"Estado: {self.availability_status.value}\n"
            f"Copias: {self.copies_count.value}\n"
            f"Resumen: {self.summary.value}"
        )

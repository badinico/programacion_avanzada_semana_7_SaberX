from typing import Set
from domain.entities import Book
from domain.value_objects import (
    BookTitle, Author, PublicationYear, Genre, Category,
    Language, AvailabilityStatus, CopiesCount, BookSummary
)
from domain.dto import BookRegistrationRequest, BookRegistrationResponse


class BookRegistrationUseCase:
    """Caso de uso para registrar un libro en la biblioteca"""
    
    def execute(self, request: BookRegistrationRequest) -> BookRegistrationResponse:
        """Ejecuta el registro de un libro"""
        try:
            # Convertir strings a enums y objetos de valor
            title = BookTitle(request.title)
            author = Author(request.author)
            publication_year = PublicationYear(request.publication_year)
            
            genre = self._convert_genre(request.genre)
            categories = self._convert_categories(request.categories)
            language = self._convert_language(request.language)
            availability_status = self._convert_availability_status(request.availability_status)
            
            copies_count = CopiesCount(request.copies_count)
            summary = BookSummary(request.summary or "")
            
            # Crear entidad Book
            book = Book(
                title=title,
                author=author,
                publication_year=publication_year,
                genre=genre,
                categories=categories,
                language=language,
                availability_status=availability_status,
                copies_count=copies_count,
                summary=summary
            )
            
            # Simular guardado (en una implementación real aquí iría el repositorio)
            book_info = book.get_display_info()
            
            return BookRegistrationResponse(
                success=True,
                message="Libro registrado exitosamente",
                book_info=book_info
            )
            
        except Exception as e:
            return BookRegistrationResponse(
                success=False,
                message=f"Error al registrar el libro: {str(e)}"
            )
    
    def _convert_genre(self, genre_str: str) -> Genre:
        """Convierte string a enum Genre"""
        for genre in Genre:
            if genre.value == genre_str:
                return genre
        raise ValueError(f"Género no válido: {genre_str}")
    
    def _convert_categories(self, categories_list: list) -> Set[Category]:
        """Convierte lista de strings a set de Category enums"""
        categories = set()
        for cat_str in categories_list:
            for category in Category:
                if category.value == cat_str:
                    categories.add(category)
                    break
            else:
                raise ValueError(f"Categoría no válida: {cat_str}")
        return categories
    
    def _convert_language(self, language_str: str) -> Language:
        """Convierte string a enum Language"""
        for language in Language:
            if language.value == language_str:
                return language
        raise ValueError(f"Idioma no válido: {language_str}")
    
    def _convert_availability_status(self, status_str: str) -> AvailabilityStatus:
        """Convierte string a enum AvailabilityStatus"""
        for status in AvailabilityStatus:
            if status.value == status_str:
                return status
        raise ValueError(f"Estado de disponibilidad no válido: {status_str}")

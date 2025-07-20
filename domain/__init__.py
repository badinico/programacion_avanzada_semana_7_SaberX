"""
Módulo de dominio - Contiene las entidades, objetos de valor y DTOs del negocio
"""

from .entities import Book
from .value_objects import (
    Genre, Category, Language, AvailabilityStatus,
    BookTitle, Author, PublicationYear, CopiesCount, BookSummary
)
from .dto import BookRegistrationRequest, BookRegistrationResponse
from .services import BookValidationService, LibraryManagementService

__all__ = [
    'Book',
    'Genre', 'Category', 'Language', 'AvailabilityStatus',
    'BookTitle', 'Author', 'PublicationYear', 'CopiesCount', 'BookSummary',
    'BookRegistrationRequest', 'BookRegistrationResponse',
    'BookValidationService', 'LibraryManagementService'
]

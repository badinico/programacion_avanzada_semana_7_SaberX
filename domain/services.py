from typing import Set
from .value_objects import Category, Genre, Language, AvailabilityStatus


class BookValidationService:
    """Servicio para validaciones específicas de libros"""
    
    @staticmethod
    def validate_categories_combination(categories: Set[Category], genre: Genre) -> bool:
        """Valida que las categorías seleccionadas sean coherentes con el género"""
        fiction_categories = {Category.NOVEL, Category.POETRY}
        non_fiction_categories = {Category.SCIENCE, Category.HISTORY, Category.BIOGRAPHY, Category.TECHNOLOGY}
        
        if genre == Genre.FICTION:
            # Para ficción, debe tener al menos una categoría de ficción
            return any(cat in fiction_categories for cat in categories)
        else:
            # Para no ficción, debe tener al menos una categoría de no ficción
            return any(cat in non_fiction_categories for cat in categories)
    
    @staticmethod
    def validate_availability_and_copies(availability: AvailabilityStatus, copies: int) -> bool:
        """Valida que la disponibilidad sea coherente con el número de copias"""
        if availability == AvailabilityStatus.AVAILABLE and copies == 0:
            return False  # No puede estar disponible si no hay copias
        return True
    
    @staticmethod
    def suggest_language_for_author(author_name: str) -> Language:
        """Sugiere un idioma basado en el nombre del autor (lógica simple)"""
        spanish_indicators = ['garcía', 'márquez', 'allende', 'borges', 'vargas', 'llosa']
        english_indicators = ['smith', 'johnson', 'brown', 'davis', 'miller', 'wilson']
        
        author_lower = author_name.lower()
        
        for indicator in spanish_indicators:
            if indicator in author_lower:
                return Language.SPANISH
                
        for indicator in english_indicators:
            if indicator in author_lower:
                return Language.ENGLISH
        
        # Por defecto, español
        return Language.SPANISH


class LibraryManagementService:
    """Servicio para gestión general de la biblioteca"""
    
    @staticmethod
    def calculate_shelf_location(genre: Genre, categories: Set[Category]) -> str:
        """Calcula la ubicación sugerida en la biblioteca"""
        if genre == Genre.FICTION:
            if Category.NOVEL in categories:
                return "Sección A - Novelas"
            elif Category.POETRY in categories:
                return "Sección B - Poesía"
            else:
                return "Sección C - Ficción General"
        else:
            if Category.SCIENCE in categories:
                return "Sección D - Ciencias"
            elif Category.HISTORY in categories:
                return "Sección E - Historia"
            elif Category.BIOGRAPHY in categories:
                return "Sección F - Biografías"
            elif Category.TECHNOLOGY in categories:
                return "Sección G - Tecnología"
            else:
                return "Sección H - No Ficción General"
    
    @staticmethod
    def estimate_reading_time(summary_length: int, genre: Genre) -> str:
        """Estima el tiempo de lectura basado en el resumen y género"""
        if summary_length < 50:
            base_time = "Corta"
        elif summary_length < 200:
            base_time = "Media"
        else:
            base_time = "Larga"
        
        # Ajustar por género
        if genre == Genre.FICTION:
            if base_time == "Corta":
                return "1-2 horas"
            elif base_time == "Media":
                return "3-5 horas"
            else:
                return "6+ horas"
        else:
            if base_time == "Corta":
                return "2-3 horas"
            elif base_time == "Media":
                return "4-6 horas"
            else:
                return "8+ horas"

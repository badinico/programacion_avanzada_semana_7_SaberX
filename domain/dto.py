from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BookRegistrationRequest:
    """DTO para solicitud de registro de libro"""
    title: str
    author: str
    publication_year: int
    genre: str
    categories: List[str]
    language: str
    availability_status: str
    copies_count: int
    summary: Optional[str] = ""


@dataclass
class BookRegistrationResponse:
    """DTO para respuesta de registro de libro"""
    success: bool
    message: str
    book_info: Optional[str] = None

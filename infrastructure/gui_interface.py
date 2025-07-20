import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import List
from application.use_cases import BookRegistrationUseCase
from domain.dto import BookRegistrationRequest
from domain.value_objects import Genre, Category, Language, AvailabilityStatus


class BookRegistrationGUI:
    """Interfaz gráfica para registro de libros"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.use_case = BookRegistrationUseCase()
        self._setup_window()
        self._create_widgets()
        
    def _setup_window(self):
        """Configuración inicial de la ventana"""
        self.root.title("Biblioteca SaberX - Registro de Libros")
        self.root.geometry("800x900")
        self.root.resizable(True, True)
        
        # Centrar ventana
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (900 // 2)
        self.root.geometry(f"800x900+{x}+{y}")
    
    def _create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal con scrollbar
        main_canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk.Frame(main_canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame para detalles del libro
        self._create_book_details_frame(scrollable_frame)
        
        # Frame para género y categoría
        self._create_genre_category_frame(scrollable_frame)
        
        # Frame para estado de disponibilidad
        self._create_availability_frame(scrollable_frame)
        
        # Frame para número de copias
        self._create_copies_frame(scrollable_frame)
        
        # Frame para resumen
        self._create_summary_frame(scrollable_frame)
        
        # Menú de idioma
        self._create_language_frame(scrollable_frame)
        
        # Botones de acción
        self._create_action_buttons(scrollable_frame)
        
        # Configurar grid del canvas y scrollbar
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        main_canvas.bind("<MouseWheel>", _on_mousewheel)
    
    def _create_book_details_frame(self, parent):
        """Frame para detalles del libro"""
        details_frame = ttk.LabelFrame(parent, text="Detalles del Libro", padding="10")
        details_frame.pack(fill="x", padx=10, pady=5)
        
        # Título
        ttk.Label(details_frame, text="Título:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.title_entry = ttk.Entry(details_frame, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Autor
        ttk.Label(details_frame, text="Autor:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.author_entry = ttk.Entry(details_frame, width=50)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Año de publicación
        ttk.Label(details_frame, text="Año de Publicación:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.year_entry = ttk.Entry(details_frame, width=20)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        details_frame.columnconfigure(1, weight=1)
    
    def _create_genre_category_frame(self, parent):
        """Frame para género y categoría"""
        genre_cat_frame = ttk.LabelFrame(parent, text="Género y Categoría", padding="10")
        genre_cat_frame.pack(fill="x", padx=10, pady=5)
        
        # Género
        ttk.Label(genre_cat_frame, text="Género:").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        
        genre_frame = ttk.Frame(genre_cat_frame)
        genre_frame.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        self.genre_var = tk.StringVar(value=Genre.FICTION.value)
        
        ttk.Radiobutton(genre_frame, text=Genre.FICTION.value, 
                       variable=self.genre_var, value=Genre.FICTION.value).pack(anchor="w")
        ttk.Radiobutton(genre_frame, text=Genre.NON_FICTION.value, 
                       variable=self.genre_var, value=Genre.NON_FICTION.value).pack(anchor="w")
        
        # Categorías
        ttk.Label(genre_cat_frame, text="Categorías:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        
        categories_frame = ttk.Frame(genre_cat_frame)
        categories_frame.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        self.category_vars = {}
        for i, category in enumerate(Category):
            var = tk.BooleanVar()
            self.category_vars[category.value] = var
            ttk.Checkbutton(categories_frame, text=category.value, variable=var).grid(
                row=i//2, column=i%2, sticky="w", padx=5, pady=2
            )
    
    def _create_availability_frame(self, parent):
        """Frame para estado de disponibilidad"""
        availability_frame = ttk.LabelFrame(parent, text="Estado de Disponibilidad", padding="10")
        availability_frame.pack(fill="x", padx=10, pady=5)
        
        self.availability_var = tk.StringVar(value=AvailabilityStatus.AVAILABLE.value)
        
        ttk.Radiobutton(availability_frame, text=AvailabilityStatus.AVAILABLE.value,
                       variable=self.availability_var, value=AvailabilityStatus.AVAILABLE.value).pack(anchor="w")
        ttk.Radiobutton(availability_frame, text=AvailabilityStatus.BORROWED.value,
                       variable=self.availability_var, value=AvailabilityStatus.BORROWED.value).pack(anchor="w")
    
    def _create_copies_frame(self, parent):
        """Frame para número de copias"""
        copies_frame = ttk.LabelFrame(parent, text="Número de Copias", padding="10")
        copies_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(copies_frame, text="Copias:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.copies_entry = ttk.Entry(copies_frame, width=10)
        self.copies_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.copies_entry.insert(0, "1")  # Valor por defecto
    
    def _create_summary_frame(self, parent):
        """Frame para resumen del libro"""
        summary_frame = ttk.LabelFrame(parent, text="Resumen del Libro", padding="10")
        summary_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        ttk.Label(summary_frame, text="Resumen:").pack(anchor="nw", padx=5, pady=5)
        
        self.summary_text = scrolledtext.ScrolledText(summary_frame, height=6, width=70)
        self.summary_text.pack(fill="both", expand=True, padx=5, pady=5)
    
    def _create_language_frame(self, parent):
        """Frame para selección de idioma"""
        language_frame = ttk.LabelFrame(parent, text="Idioma", padding="10")
        language_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(language_frame, text="Idioma:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.language_var = tk.StringVar(value=Language.SPANISH.value)
        language_combobox = ttk.Combobox(language_frame, textvariable=self.language_var, 
                                        values=[lang.value for lang in Language], 
                                        state="readonly", width=20)
        language_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    def _create_action_buttons(self, parent):
        """Frame para botones de acción"""
        buttons_frame = ttk.Frame(parent)
        buttons_frame.pack(fill="x", padx=10, pady=20)
        
        # Botón Registrar
        register_btn = ttk.Button(buttons_frame, text="Registrar Libro", 
                                 command=self._register_book, style="Accent.TButton")
        register_btn.pack(side="left", padx=10)
        
        # Botón Limpiar
        clear_btn = ttk.Button(buttons_frame, text="Limpiar", command=self._clear_form)
        clear_btn.pack(side="left", padx=10)
    
    def _register_book(self):
        """Registrar un nuevo libro"""
        try:
            # Validar campos requeridos
            if not self.title_entry.get().strip():
                messagebox.showerror("Error", "El título es obligatorio")
                return
            
            if not self.author_entry.get().strip():
                messagebox.showerror("Error", "El autor es obligatorio")
                return
            
            if not self.year_entry.get().strip():
                messagebox.showerror("Error", "El año de publicación es obligatorio")
                return
            
            if not self.copies_entry.get().strip():
                messagebox.showerror("Error", "El número de copias es obligatorio")
                return
            
            # Obtener categorías seleccionadas
            selected_categories = [
                category for category, var in self.category_vars.items() 
                if var.get()
            ]
            
            if not selected_categories:
                messagebox.showerror("Error", "Debe seleccionar al menos una categoría")
                return
            
            # Validar año
            try:
                year = int(self.year_entry.get())
            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número válido")
                return
            
            # Validar copias
            try:
                copies = int(self.copies_entry.get())
            except ValueError:
                messagebox.showerror("Error", "El número de copias debe ser un número válido")
                return
            
            # Crear request
            request = BookRegistrationRequest(
                title=self.title_entry.get().strip(),
                author=self.author_entry.get().strip(),
                publication_year=year,
                genre=self.genre_var.get(),
                categories=selected_categories,
                language=self.language_var.get(),
                availability_status=self.availability_var.get(),
                copies_count=copies,
                summary=self.summary_text.get("1.0", tk.END).strip()
            )
            
            # Ejecutar caso de uso
            response = self.use_case.execute(request)
            
            if response.success:
                # Mostrar información en terminal (consola)
                print("\n" + "="*50)
                print("LIBRO REGISTRADO EXITOSAMENTE")
                print("="*50)
                print(response.book_info)
                print("="*50 + "\n")
                
                messagebox.showinfo("Éxito", "Libro registrado exitosamente. Verifique la información en la terminal.")
                self._clear_form()
            else:
                messagebox.showerror("Error", response.message)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def _clear_form(self):
        """Limpiar todos los campos del formulario"""
        # Limpiar entries
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
        self.copies_entry.insert(0, "1")  # Valor por defecto
        
        # Resetear radiobuttons
        self.genre_var.set(Genre.FICTION.value)
        self.availability_var.set(AvailabilityStatus.AVAILABLE.value)
        
        # Limpiar checkbuttons
        for var in self.category_vars.values():
            var.set(False)
        
        # Resetear idioma
        self.language_var.set(Language.SPANISH.value)
        
        # Limpiar texto
        self.summary_text.delete("1.0", tk.END)
    
    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop() 
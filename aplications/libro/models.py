from django.db import models
from aplications.autor.models import Author
from .managers import BookManager,CategoryManager
# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(
        'Categoria',
        max_length=30)
    objects=CategoryManager()
    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.categoryName
    
class Book(models.Model):
    objects = BookManager()
    category = models.ForeignKey(
        Category, 
        related_name='categoria_libro',
        on_delete=models.CASCADE,
        default=None  # Cambiado de True a None, ya que no tiene sentido tener True como valor predeterminado para una ForeignKey
    )
    authors = models.ManyToManyField(
        Author,
        related_name='categoria_autor',
    )
    title = models.CharField(
        'Titulo',
        max_length=50
    )
    date = models.DateField(
        "Fecha De Lanzamiento",
        auto_now=False,
        auto_now_add=False,
        default=None  # Cambiado de True a None, ya que no tiene sentido tener True como valor predeterminado para una fecha
    )
    background = models.ImageField(
        'Imagen De Portada', 
        upload_to='media/book',
        default=None,  # Cambiado de True a None, ya que no tiene sentido tener True como valor predeterminado para una imagen
        blank=True        
    )
    views = models.PositiveIntegerField(
        default=0,
        blank=True
    )
    class Meta:
        verbose_name = ("Libro")
        verbose_name_plural = ("Libros")

    
    def __str__(self):
        return str(self.id)+' '+self.title

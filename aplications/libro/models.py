from django.db import models
from aplications.autor.models import Author
# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(
        'Categoria',
        max_length=30)
    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.categoryName
class Book(models.Model):
    category = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)
    title = models.CharField(
        'Titulo',
        max_length=50
        )
    date=models.DateField(
        "Fecha De Lanzamiento",
        auto_now=False,
        auto_now_add=False,
        default=None,
        blank=None
        )
    background= models.ImageField(
        'Imagen De Portada', 
        upload_to='media/book',
        default=None ,
        blank=True,
        null=True,
        
        )
    views= models.PositiveIntegerField(
        default=0,
        blank=True,
    )
    class Meta:
        verbose_name = ("Libro")
        verbose_name_plural = ("Libros")

    
    def __str__(self):
        return self.title

  
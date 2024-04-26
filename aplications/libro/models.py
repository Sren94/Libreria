from django.db import models
from aplications.autor.models import Author
# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(
        'Libro',
        max_length=30)
    class Meta:
        verbose_name = ("Libro")
        verbose_name_plural = ("Libros")

    def __str__(self):
        return self.categoryName
class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        )
    authors = models.ManyToManyField(Author)
    title = models.CharField(
        'Titulo',
        max_length=50
        )
    date=models.DateField(
        "Fecha De Lanzamiento",
        auto_now=False,
        auto_now_add=False
        )
    background= models.ImageField(
        'Imagen De Portada', 
        upload_to='media/book'
        ,height_field=None, 
        width_field=None,
        max_length=None
        )
    views= models.PositiveIntegerField()
    class Meta:
        verbose_name = ("Libro")
        verbose_name_plural = ("Libros")

    
    def __str__(self):
        return self.title

  
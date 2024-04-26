from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(
        'Nombre',max_length=50,
        )
    lastName=models.CharField(
        'Apellido',
        max_length=50,
        )
    nationality = models.CharField(
        'Nacionalidad', 
        max_length=50,
        )
    age= models.PositiveIntegerField(
        'Edad',
    )
    class Meta:
        verbose_name = ("Autor")
        verbose_name_plural =("Autores")

    def __str__(self):
        return self.firstName+' '+self.lastName+' '+self.nationality

    
from django.db import models

# Create your models here.
from aplications.libro.models import Book

class Reader(models.Model):
    firstName=models.CharField(
        'Nombre',
        max_length=50
        )
    lastName=models.CharField(
        'Apellido',
        max_length=50
        )
    nationality=models.CharField(
        'Nacionalidad',
        max_length=50
        )
    age=models.PositiveIntegerField('edad',default=0)
    class Meta:
        verbose_name = "Lector"
        verbose_name_plural ="Lectores"

    def __str__(self):
        return self.firstName+' '+self.lastName+' '+self.nationality
class Loan(models.Model):
    reader = models.ForeignKey(
        Reader, 
        
        on_delete=models.CASCADE
        )
    book= models.ForeignKey(
        Book,
        on_delete=models.CASCADE
        )
    date_loan= models.DateField(
        'Fecha De Prestamo',
        )
    date_return= models.DateField(
        'Fecha De Devolucion',
        blank=True,
        null=True,
        )
    bookReturn=models.BooleanField()
    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural ="Prestamos"
        
    def __str__(self):
        return str(self.reader.firstName)+' '+self.book.title+' '+str(self.date_loan)

   
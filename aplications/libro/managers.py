import datetime
from django.db import models
from django.db.models import Q

class BookManager(models.Manager):
    
    def searchBookDate(self,var,date,dateEnd):
        d1=datetime.datetime.strptime(date,'%Y-%m-%d').date()
        d2=datetime.datetime.strptime(dateEnd,'%Y-%m-%d').date()
        
        found= self.filter(
            title__icontains=var,
            date__range=(d1,d2)
        )
        return found
    def searchBook(self,var):
        found= self.filter(
            title__icontains=var,

        )
        return found
    def addAuthorBook(self,id_book,author):
        #agregar de un modelo many to many
        #aqui vamos a agregar elementos del libro 
        #se agregara un author 
        #como es una relacion many to many se empleara asi
        book=self.get(id=id_book)
        #modelo.atributoManyToMany.funcion(llave primaria del modelo conectado)
        #aqui se agrega
        
        book.authors.add(author)
        return book     
        
class CategoryManager(models.Manager):
    def category_author(self, author_id):
        categories = self.filter(
            categoria_libro__authors__id=author_id
            ).distinct()
        return categories
    
        
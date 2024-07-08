from django.db import models
from django.db.models import Q 
class AuthorManager(models.Manager):
    """Managers para el modelo autor"""
    
    #aqui se hacen metodos para la personalizacion de los modelos y el modo que se retorna
    def listAuthors(self):
        return self.all()
    def searchAuthors(self,var):
        found= self.filter(
            #esto sirve para buscar algo parecido que este en la variable varS
            firstName__icontains=var
            )
        return found
    def searchAuthorsMatches(self,var):
        found= self.filter(
            #La funcion de Q funciona para los queries de la base de datos asi que 
            #por lo tanto funciona los metodos de los queries asi que 
            #nos ayuda a mantener codigo mas legible
            #esta funcion de aqui nos ayuda a buscar las similitudes
            Q(firstName__icontains=var) | Q(lastName__icontains=var)
            )
        return found
    def searchAuthorsMatches(self,var):
        found= self.filter(
            #La funcion de Q funciona para los queries de la base de datos asi que 
            #por lo tanto funciona los metodos de los queries asi que 
            #nos ayuda a mantener codigo mas legible
            #esta funcion de aqui nos ayuda a buscar las similitudes
            Q(firstName__icontains=var) | Q(lastName__icontains=var)
            )
        return found
    """
     def searchAuthorsMatches(self,var):
        found= self.filter(
            #La funcion de Q funciona para los queries de la base de datos asi que 
            #por lo tanto funciona los metodos de los queries asi que 
            #nos ayuda a mantener codigo mas legible
            #esta funcion de aqui nos ayuda a buscar las similitudes
            Q(firstName__icontains=var) | Q(lastName__icontains=var)
            ).exclude(age=60)
            #lo de arriba que es exclude hace que si la condicion que recibe 
            #si se cumple excluya los resultados que sean iguales a la condicion 
            
            #tambien para mayor que y menor que se usa la siguiente sintaxis
            resultado=self.filter(
                edad__gt=40,
                edad__gt=50
            ).order_by('lastName','nombres','id')
        return found
        
    """
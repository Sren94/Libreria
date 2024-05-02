from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Author
# Create your views here.
class authorList(ListView):
    #el retorno del objeto que se usa en la vista
    context_object_name = 'autor'
    template_name='autor/listAutor.html'
    #la sobreescritura y retorno de lo que se va a usar en la lista
    def get_queryset(self):
        #uso del manager directamene
        return Author.objects.listAuthors()
class SearchAuthoorList(ListView):
    context_object_name = 'autor'
    template_name='autor/searchAuthor.html'
    
    def get_queryset(self):
        var=self.request.GET.get('searchAuthor','')
        return Author.objects.searchAuthorsMatches(var)    
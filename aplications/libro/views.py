from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .models import Book

# Create your views here.
class bookList(ListView):
    #el retorno del objeto que se usa en la vista
    context_object_name = 'book'
    template_name='libro/listaLibros.html'
   
    #la sobreescritura y retorno de lo que se va a usar en la lista
    def get_queryset(self):
        #uso del manager directamene
        var = self.request.GET.get('searchBook','')
        date= self.request.GET.get('date','')
        dateEnd=self.request.GET.get('dateEnd','')
        if date and dateEnd:
            return Book.objects.searchBookDate(var,date,dateEnd)
        else:  
            return Book.objects.searchBook(var)

class BookDetailView(DetailView):
    model = Book
    template_name = "libro/detalleLibro.html"
    

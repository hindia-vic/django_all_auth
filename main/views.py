from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Books

# Create your views here.
def home(request):
    return render(request,'home.html')

class BooksView(ListView):
    model=Books
    template_name='book.html'

class BookDetail(DetailView):
    model=Books
    template_name='detail.html'

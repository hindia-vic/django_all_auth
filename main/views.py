from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from . models import Books

# Create your views here.
def home(request):
    return render(request,'home.html')

class BooksView(LoginRequiredMixin,ListView):
    model=Books
    template_name='book.html'

class BookDetail(LoginRequiredMixin,DetailView):
    model=Books
    template_name='detail.html'

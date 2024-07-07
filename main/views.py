from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from . models import Books

# Create your views here.
def home(request):
    return render(request,'home.html')

class BooksView(LoginRequiredMixin,ListView):
    model=Books
    template_name='book.html'

class BookDetail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model=Books
    template_name='detail.html'
    permission_required = 'books.special_status'

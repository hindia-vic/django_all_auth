from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q
from . models import Books

# Create your views here.
def home(request):
    return render(request,'home.html')

class BooksView(LoginRequiredMixin,ListView):
    model=Books
    template_name='book.html'

class BookDetail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model=Books
    context_object_name='book'
    template_name='detail.html'
    permission_required = 'main.special_status'

class SearchResultView(ListView):
    model=Books
    context_object_name='book_list'
    template_name='search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Books.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

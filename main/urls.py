from django.urls import path
from .views import home,BooksView,BookDetail

urlpatterns=[
    path('',home,name='home'),
    path('book/',BooksView.as_view(),name='books'),
    path('book/<uuid:pk>/',BookDetail.as_view(),name='detail'),
]
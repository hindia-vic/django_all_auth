from django.urls import path
from .views import home,BooksView,BookDetail,SearchResultView

urlpatterns=[
    path('',home,name='home'),
    path('book/',BooksView.as_view(),name='books'),
    path('book/<uuid:pk>/',BookDetail.as_view(),name='detail'),
    path('search/',SearchResultView.as_view(),name='search_result'),
]
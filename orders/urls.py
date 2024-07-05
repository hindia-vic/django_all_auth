from django.urls import path
from .views import OrdersPage

urlpatterns=[
    path('',OrdersPage.as_view(),name='order'),
]
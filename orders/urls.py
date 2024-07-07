from django.urls import path
from .views import OrdersPage,charge

urlpatterns=[
    path('',OrdersPage.as_view(),name='order'),
    path('charge/',charge,name='charge')
]
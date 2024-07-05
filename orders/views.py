from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings


class OrdersPage(TemplateView):
    template_name='orders.html'
    def get_context_data(self, **kwargs): # new
       context = super().get_context_data(**kwargs)
       context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
       return context
    
# Create your views here.

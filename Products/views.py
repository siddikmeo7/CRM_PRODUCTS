from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *
from templates import *

class Registration (TemplateView):
    template_name = "registration.html"


class Login (TemplateView):
    template_name = "login.html"


def Homepage (request):
  users = Person.objects.all()
  
  return render(request,"crmpage.html",context={"users":users})
    
class Crmmm (TemplateView):
    template_name = "Crmmm.html"

class Products (TemplateView):
    template_name = "Products.html"

class Customers (TemplateView):
    template_name = "Customers.html"

class Orders (TemplateView):
    template_name = "Orders.html"

class Reports (TemplateView):
    template_name = "Reports.html"


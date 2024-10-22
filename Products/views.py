from django.views.generic import TemplateView
from templates import *

class Registration (TemplateView):
    template_name = "registration.html"


class Login (TemplateView):
    template_name = "login.html"

class Crm (TemplateView):
    template_name = "crmpage.html"

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


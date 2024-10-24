from django.urls import path
from  .views import * # new 

urlpatterns = [
    path("register",Registration.as_view(),name="Register"),
    path("login/",Login.as_view(),name="Login"),
    path("crmpage/",Homepage,name="CrmPage"),
    path("products/",Products.as_view(),name="Products"),
    path("customers/",Customers.as_view(),name="Customers"),
    path("orders/",Orders.as_view(),name="Orders"),
    path("reports",Reports.as_view(),name="Reports"),
    path("crmmm/",Crmmm.as_view(),name="Crmmm")

]

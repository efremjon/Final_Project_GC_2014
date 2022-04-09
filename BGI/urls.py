
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Account.urls')),
    path('BGI/',include('Company.urls')),
    path('Agent/',include('Agent.urls')),
    path('Customer/',include('Customer.urls')),
]

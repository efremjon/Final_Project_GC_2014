from django.urls import path
from .import views
urlpatterns = [
    path('',views.Admin_dashboard,name="admin_dashbord"),
    
    
]

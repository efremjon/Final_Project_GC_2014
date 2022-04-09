from urllib import request
from django.shortcuts import render

# Create your views here.

def Admin_dashboard(request):
    return render(request,'Company/admin.html',{})
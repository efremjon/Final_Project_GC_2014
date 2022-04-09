from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        a=user.groups.all()[0].name
        if a == 'Admin':
            login(request,user)
            return HttpResponseRedirect(reverse('admin_dashbord',))
        elif a == 'Agent':
            login(request,user)
            return HttpResponseRedirect(reverse('agent_dashbord'))
        elif a == 'Customer':
            login(request,user)
            return redirect('customer_page')
    return render(request,'Account/pages-login.html',{})

def register_view(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username taken')
                return render(request,'Account/pages-register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken ')
                return render(request,'Account/pages-register.html')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,password=password1)
                user.save()
                group = Group.objects.get(name='Customer')
                user.groups.add(group)
                messages.info(request, 'Sucssesfull Create User')
                return redirect ('/')
        else:
            print('user is not crated')
            return render(request,'Account/pages-register.html')
    else:
        # raise ValidationError("User Already Exist")
        messages.info(request, 'password not match') 
      
    return render(request,'Account/pages-register.html',{})
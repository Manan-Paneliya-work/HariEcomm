from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect



# Create your views here.
def login(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)
        # print(user_obj.exists())
        
        if not user.exists():
            messages.warning(request, "Account not found")
            return HttpResponseRedirect(request.path_info)
     
        user_obj = authenticate(username = email, password = password)
        if user_obj:
            auth_login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, "Invalid credentials")
        return HttpResponseRedirect(request.path_info)
        
        
   
    return render(request, 'accounts/login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
        # if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            messages.warning(request, "Email is already taken.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(
            first_name = first_name, 
            last_name = last_name or '', 
            email = email,
            username = email
        )
        user_obj.set_password(password)
        user_obj.save()
        
 
        messages.success(request, "Account created successfully.")
        return HttpResponseRedirect(request.path_info)
    

    return render(request, 'accounts/register.html')

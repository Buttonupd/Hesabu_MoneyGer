from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import numpy as np
# login view page
def home(request):
    return render(request, 'home.html', {})

# registration view
def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.validate_unique()
            messages.success(request, "Account was created for " + username)
            return redirect ('DairyManagement:login')

    context = {'form': form}
    return render(request, 'register.html', context)

# login view
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("DairyManagement:user")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'login.html', context)

# logout view
def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('home')

# after login userpage
@login_required
def userPage(request):
    context = {}
    return render(request, 'user.html', context)

# user products
@login_required
def add_product(request):
    current_user = request.user
    profiles = UserProfile.get_profile()
    productinfo = request.POST.get("product")
    for profile in profiles: 
        if profile.profile_name.id == current_user.id:
            if request.method == 'POST':
                form = ProductForm(request.POST)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    messages.success(request, f'Hello! {productinfo} has successfully been updated' )
                    return redirect('addProduct')
            else:
                form = ProductForm()
            return render(request,'addProduct.html',{"user":current_user,"form":form})

# users can either add products or milk collection
@login_required
def show_options(request):
    return render(request, 'show_options.html')

# add milk collection data
@login_required
def add_milk(request):
    current_user = request.user
    profiles = UserProfile.get_profile()
    name =  request.POST.get("profile_name")
    for profile in profiles:
        if profile.profile_name.id == current_user.id:
            if request.method == 'POST':
                form = MilkCollectionForm(request.POST)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    messages.success(request, f'Hi {name}, Your data has successfully been updated' )
                    return redirect('addProduct')
            else:
                form = MilkCollectionForm()
            return render(request,'addProduct.html',{"user":current_user,"form":form})

# show or display user products
@login_required(login_url="login")
def products(request):
    products2 = Project.objects.filter(posted_by=request.user)
    return render(request, 'products.html', { "products2": products2})

# display user total expenditure
@login_required(login_url="login")
def SalaryModel(request):
        empobj = Project.get_projects().filter(posted_by=request.user)
        return render(request, 'total.html', {"Project":empobj} )

# display current margin not currently working!!!!!
@login_required(login_url="login")
def margin(request):
        empobj = MadeSale.get_sales().filter(juror=request.user)
        return render(request, 'margin.html', {"MadeSale":empobj} )

# calculate user margin
@login_required
def add_user_sales(request , pk):
    current_user = request.user
    user_id = MadeSale.objects.get(id=pk)
    profiles = UserProfile.get_profile()
    for profile in profiles:
        if profile.profile_name.id == current_user.id:
            if request.method == 'POST':
                form = SalesForm(request.POST)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    messages.success(request, f'Hi, Your data has successfully been updated' )
                    return redirect('addProduct')
            else:
                form = SalesForm()
            return render(request,'addProduct.html',{"user":current_user,"form":form})

@login_required
def get_total_month(request):
    empobj = MilkCollection.objects.get_or_create(juror=request.user)
    return render(request, 'monthly_total.html', {"MilkCollection":empobj} )



        

























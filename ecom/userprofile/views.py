from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.utils.text import slugify

from .models import Userprofile

from store.forms import ProductForm
from store.models import Product 

def vendor_detail(request,pk):
    user = User.objects.get(pk=pk)

    return render(request, 'vendor_detail.html',{
        'user':user
    })


@login_required
def my_store(request): 
    return render(request, 'my_store.html')

@login_required
def add_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
 
            product = form.save(commit=False)  
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            return redirect('my_store')
    else:
        form = ProductForm()
  
    return render(request, 'add_product.html', {
        'form':form
    })

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {
        'form': form
    })




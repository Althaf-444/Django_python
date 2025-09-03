from django.shortcuts import render , redirect
from .forms import ProductForm
from .models import Product
# Create your views here.

def home(request):
    return render(request ,'App/home.html')

def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request , 'App/product_form.html',{'form' : form})

def read_view(request):
    products = Product.objects.all()
    return render(request , 'App/product_list.html',{'products':products})


def update_view(request , product_id):
    product = Product.objects.get(product_id = product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
           form.save()
           return redirect('list')
    return render(request , 'App/product_form.html',{'form' : form})

def delete_view(request , product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('list')
    return render(request , 'App/product_confirm_delete.html',{'product':product})


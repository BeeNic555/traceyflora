from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def products(request):
    return render(request, 'main/products.html')

def testimonials(request):
    return render(request, 'main/testimonials.html')

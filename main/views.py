from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    image_list = [
        'main/images/1.png',
        'main/images/2.png',
        'main/images/3.png',
        'main/images/4.png',
        # 添加更多图片路径
    ]
    return render(request, 'main/home.html', {'image_list': image_list})


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def products(request):
    return render(request, 'main/products.html')

def showcase(request):
    image_list = [
        'main/images/1.png',
        'main/images/2.png',
        'main/images/3.png',
        'main/images/4.png',
        'main/images/1.png',
        'main/images/2.png',
        'main/images/3.png',
        'main/images/4.png',
        # 添加更多图片路径
    ]
    return render(request, 'main/showcase.html', {'image_list': image_list})


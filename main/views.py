from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    image_list = [
        'main/images/1.png',
        'main/images/2.png',
        'main/images/4.png',
        'main/images/15.png',
        'main/images/14.png',
        'main/images/16.png',
        'main/images/17.png',
        'main/images/19.png',
        'main/images/21.png',
        'main/images/24.png',
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
        'main/images/5.png',
        'main/images/6.png',
        'main/images/7.png',
        'main/images/8.png',
        'main/images/9.png',
        'main/images/10.png',
        'main/images/11.png',
        'main/images/12.png',
        'main/images/13.png',
        'main/images/14.png',
        'main/images/15.png',
        'main/images/16.png',
        'main/images/17.png',
        'main/images/18.png',
        'main/images/19.png',
        'main/images/20.png',
        'main/images/21.png',
        'main/images/22.png',
        'main/images/23.png',
        'main/images/24.png'
        # 添加更多图片路径
    ]
    return render(request, 'main/showcase.html', {'image_list': image_list})

def faq(request):
    return render(request, 'main/faq.html')
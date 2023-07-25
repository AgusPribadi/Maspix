from django.shortcuts import render
from .models import Portfolio, Gallery, Blog

def index(request):
    return render(request, 'aplikasi_maspix/index.html')

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'aplikasi_maspix/portfolio.html', {'portfolios': portfolios})

def gallery(request):
    galleries = Gallery.objects.all()
    return render(request, 'aplikasi_maspix/gallery.html', {'galleries': galleries})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'aplikasi_maspix/blog.html', {'blogs': blogs})
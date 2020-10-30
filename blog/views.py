from django.shortcuts import render


def home_view(request):
    return render(request, 'blog/home.html')

def detail_view(request):
    return render(request, 'blog/detail_view.html')

def about_view(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    return render(request, 'blog/contact.html')
from django.http import HttpResponse
from django.shortcuts import render

def home(request):   # I can name those methods / functions whatever I want for page routing
    # return HttpResponse("Hello boss, Home!")
    return render(request, 'website/home.html')

def about(request):   # I can name those methods / functions whatever I want for page routing
    # return HttpResponse("Hello boss, About!")
    return render(request, 'website/about.html')

def contact(request):   # I can name those methods / functions whatever I want for page routing
    # return HttpResponse("Hello boss, Contact!")
    return render(request, 'website/contact.html')

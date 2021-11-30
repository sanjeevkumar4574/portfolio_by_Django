from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request,'app1/about.html')

def Portfolio(request):
    return render(request,'app1/portfolio.html')

def blog(request):
    return render(request,'app1/blog.html')

def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name']
            e = fm.cleaned_data['email']
            s = fm.cleaned_data['subject']
            m = fm.cleaned_data['message']
            data = Contact(name=n,email=e,subject=s,message=m)
            data.save()
            
        fm = ContactForm()
    else:
        fm = ContactForm()
        
    return render(request,'app1/contact.html',{'form':fm})




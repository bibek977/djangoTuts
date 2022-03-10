from django.shortcuts import render,HttpResponse
from webpage.models import Contact
from django.contrib import messages

def index(request):
    # context = {
    #     'title' : "Index"
    # }
    return render(request, "index.html",)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        contact = Contact(email=email, pw=pw)
        contact.save()

        messages.success(request, 'Profile details updated.')

    return render(request, 'contact.html')

def shop1(request):
    return HttpResponse("Shop 1")

def shop2(request):
    return HttpResponse("Shop 2")
    
def shop3(request):
    return HttpResponse("Shop 3")

# Create your views here.

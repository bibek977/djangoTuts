from django.shortcuts import render,HttpResponse

def index(request):
    context = {
        'title' : "Index"
    }
    return render(request, "index.html",context)

def about(request):
    return HttpResponse("About")

def shop1(request):
    return HttpResponse("Shop 1")

def shop2(request):
    return HttpResponse("Shop 2")
    
def shop3(request):
    return HttpResponse("Shop 3")

# Create your views here.

from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'index.html')
def product(request):
    return render(request, 'products.html')
def store(request):
    return render(request, 'store.html')
# def getstart(request):
#     return render(request, 'getstart.html')
def contact(request):
    return render(request, 'contact.html')


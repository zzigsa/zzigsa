from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product.html')

def productedit(request):
    return render(request, 'productedit.html')
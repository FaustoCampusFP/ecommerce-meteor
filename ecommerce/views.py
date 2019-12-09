from django.shortcuts import render
from .models import Item

# Create your views here.
def home(request):
    return render(request, 'home.html')

def catalog(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'catalog.html', context)

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'product.html', context)
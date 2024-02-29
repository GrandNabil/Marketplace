from django.shortcuts import render
from item.models import Categorie, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(vendu=False)[0:6]
    categories = Categorie.objects.all()
    return render(request, 'market/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'market/contact.html')

def signup(request):
    form = SignupForm()

    return render(request, 'market/signup.html', {
        'form': form
    })

from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
        
    else:
        form = SignupForm()

    return render(request, 'market/signup.html', {
        'form': form
    })

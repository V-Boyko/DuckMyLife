
from django.shortcuts import render
from .forms import DuckEntry

# Create your views here.

def frontpage(request):
    return render(request, "fowl/frontpage.html")

def editor(request):
    context = {}
    form = DuckEntry(request.POST)
    context['form'] = form
    print(form)
    return render(request, 'fowl/editor.html', context)

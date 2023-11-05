
from django.shortcuts import render
from .forms import DuckEntry
from django.http import HttpResponse

# Create your views here.

def frontpage(request):
    return render(request, "fowl/frontpage.html")


def editor(request):
   form = DuckEntry(request.POST)
   text = request.POST.get('text-box', "")
   print(type(text))
   return render(request, 'fowl/editor.html') 

'''
def editor(request):
    if request.method == 'POST':
        form = DuckEntry(request.POST)
        if form.is_valid():
            print(request.get)
            return HttpResponse("I made a request")
    else:
        form = DuckEntry()
    return render(request, 'fowl/editor.html', {"form":form})
'''

'''
def editor(request):
    context = {}
    form = DuckEntry(request.POST)
    context['form'] = form
    print(form)
    return render(request, 'fowl/editor.html', {'context':context})
'''
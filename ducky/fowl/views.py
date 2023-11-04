
from django.shortcuts import render
from .forms import DuckEntry
from django.http import HttpResponse

# Create your views here.

def frontpage(request):
    return render(request, "fowl/frontpage.html")


def editor(request):
    if request.method == 'POST':
        form = DuckEntry(request.POST)
        if form.is_valid():
            print(form.cleaned_data["my_form_field_name"])
            return HttpResponse("I made a request")
    else:
        form = DuckEntry()
    return render(request, 'fowl/editor.html', {"form":form})


'''
def editor(request):
    context = {}
    form = DuckEntry(request.POST)
    context['form'] = form
    print(form)
    return render(request, 'fowl/editor.html', {'context':context})
'''
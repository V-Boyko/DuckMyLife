from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, "fowl/frontpage.html")

def editor(request):
    return render(request, 'fowl/editor.html')

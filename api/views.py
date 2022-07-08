from django.shortcuts import render

def home(request):
    context = {'var' : 'Hello Django'}
    return render(request, 'index.html', context)

        
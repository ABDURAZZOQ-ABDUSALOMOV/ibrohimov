from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_code(request):
    return render(request, 'get-code.html')


def enter_code(request):
    return render(request, 'enter-code.html')
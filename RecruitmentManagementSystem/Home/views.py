from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'header':'RECHECK!!!!'}
    return render(request, 'home/home.html', context)


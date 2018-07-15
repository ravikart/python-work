from django.http import HttpResponse

# Create your views here.


def companyIndex(request, companyCode):
    print(companyCode)
    return HttpResponse("<h2>Otha ulla vanthutan da</h2")

from django.urls import path
from . import views


urlpatterns = [
    path('<companyCode>/', views.companyIndex),
]

from django.shortcuts import render
from django.http import HttpResponse


# вывод содержимого generator/home.html
def home(request):
    lst = list(range(6, 15))  # создаем список с диапозоном для пароля и передадим его ниже в render что бы в хоме цикл использовал этот список
    return render(request, 'generator/home.html', {'lst': lst})


# вывод содержимого generator/password.html
def password(request):

    return render(request, 'generator/password.html')
from django.shortcuts import render
from django.http import HttpResponse
import random

# то что на home.html обрабатывается тут и выводитя
# вывод содержимого generator/home.html
def home(request):
    # создаем список с диапозоном для пароля и передадим его ниже в render что бы в хоме цикл использовал этот список
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})


# вывод содержимого generator/password.html
def password(request):
    # создаем символы для пароля из кодировки символов с помощью функции которая по коду символа показывает сам символ
    char = [chr(i) for i in range(97, 123)]  # сначало формируются символы и далее будем прибавлять различные варианты ввода пароля

    # далее добавим возможность выбирать символы верхнего и нижнего регистра сюда приходит uppercase
    if request.GET.get("uppercase"):  # если там галочка отмеченна
        char.extend([chr(i) for i in range(65, 91)])  # дополняем переменную функционалом
    # добавим цифры в пароль
    if request.GET.get("numbers"):
        char.extend([chr(i) for i in range(48, 58)])  # дополняем переменную
    # добавим спецсимволы в пароль
    if request.GET.get("special"):
        char.extend([chr(i) for i in range(33, 48)])  # дополняем переменную

    psw = ''
    print(char)
    length = int(request.GET.get('length'))
    #  из символов в рандомном порядке формируем пароль из заданного количества символов
    for i in range(length):
        psw += random.choice(char)
    # формируем путь и отправляем переменную по этому пути
    return render(request, 'generator/password.html', {'password': psw})


def infa(request):

    return render(request, 'generator/infa.html')

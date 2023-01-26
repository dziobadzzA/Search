from django.http import HttpResponse
from django.shortcuts import render

from .adapter import Model

library = Model()


def response_help(request):
    return render(request, 'public/help.html')


def response_map(request):

    if request.method == "POST":
        name_file = request.POST['path']
        command = int(request.POST['command'])
        if command == 0:
            # TODO читаем из файла настроек необходимые данные (входные данные)
            # обрабатываем через модель
            # выводим результат через JSON response
            pass
        else:
            # TODO читаем из файла настроек необходимые данные (входные данные)
            # обрабатываем через модель
            # выводим результат через JSON response
            pass

    return render(request, 'public/example.html')

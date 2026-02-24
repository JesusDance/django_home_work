import os

from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.template import loader
from django.views.generic import TemplateView


def index(request):
    return render(request,"index.html")


def luc(request):
    return HttpResponse(
        'Люк Скайуокер — один из главных персонажей вселенной '
        '«Звёздных войн», джедай, сын сенатора с Набу Падме '
        'Амидалы Наберри и рыцаря-джедая Энакина Скайуокера', status=200)


def leya(request):
    return HttpResponse(
        'Лея Органа — дочь рыцаря-джедая Энакина Скайуокера '
        'и сенатора Падме Амидалы Наберри', status=200)


def han(request):
    return HttpResponse('Хан Соло — пилот космического корабля '
                        '«Тысячелетний сокол», его бортмехаником и вторым'
                        'пилотом является вуки по имени Чубакка.', status=200)


class PeopleView(TemplateView):
    template_name = "people_list.html"

    def get_context_data(self, **kwargs):
        return {"people": [
            {"name": "Adam", "surname": "King"},
            {"name": "Alice", "surname": "King"},
            {"name": "Steven", "surname": "King"},
        ]}


# def people_view(request):
#     people = [
#         {"name": "Adam", "surname": "King"},
#         {"name": "Alice", "surname": "King"},
#         {"name": "Steven", "surname": "King"},
#     ]
#     template = loader.get_template(template_name='people_list.html')
#     context = {"people": people}
#     return HttpResponse(template.render(context, request))


def lets_do_it(request):
    lets_do_it = [
        {"priority": 100, "task": "make a list of to do"},
        {"priority": 150, "task": "learn Django"},
        {"priority": 1, "task": "think about universe"},
    ]
    template = loader.get_template(template_name='todo_list.html')
    context = {"lets_do_it": lets_do_it}
    #lets_do_it.sort(key=lambda item: item["priority"], reverse=True)

    return HttpResponse(template.render(context, request))


def file(request):
    new_file = os.path.join(settings.BASE_DIR, 'lesson_4',
                            'static', 'file', '002.txt')
    return FileResponse(open(new_file, 'rb'))


def new_file(request):
    response = HttpResponse(
        "here's your file", content_type="text/plain", status=227
    )
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    return response
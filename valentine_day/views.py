from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView


class MyTemplateView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        return {"photos": [
            {"id": 1, "title": "Best", "file": "1.jpg"},
            {"id": 2, "title": "woman", "file": "2.jpg"},
            {"id": 3, "title": "i've", "file": "3.jpg"},
            {"id": 4, "title": "ever", "file": "4.jpg"},
            {"id": 5, "title": "had!", "file": "5.jpg"},
        ]}


def get_photo(request, photo_id):
        photos = MyTemplateView().get_context_data()["photos"]

        for photo in photos:
            if photo["id"] == photo_id:
                return render(request, "detail.html",
                              {"photo": photo})

        raise Http404("Photo not found")
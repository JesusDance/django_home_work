from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


class MyTemplateView(TemplateView):
    template_name = "post_view.html"

    def get_context_data(self, **kwargs):
        return {"latest_question_list": [
            {"id": 1, "question_text": "first question"},
            {"id": 2, "question_text": "second question"},
            {"id": 5, "question_text": "fifth question"},
            {"id": 3, "question_text": "third question"},
        ]}

# def index_post(request):
#     latest_question_list = [
#         {"id": 1, "question_text": "first question"},
#         {"id": 2, "question_text": "second question"},
#         {"id": 5, "question_text": "fifth question"},
#         {"id": 3, "question_text": "third question"},
#     ]
#     template = loader.get_template(template_name='post_view.html')
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))


def detail(request, question_id):
    if question_id == 1:
        return HttpResponse("Answer to the question 1!")
    elif question_id == 2:
        return HttpResponse("Answer to the question 2!")
    elif question_id == 3:
        return HttpResponse("Answer to the question 3!")
    else:
        return HttpResponse("Question does not exist!")

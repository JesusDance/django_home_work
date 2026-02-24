from django.views.generic import FormView
from lesson_8.forms import MyModelForm, ProductsForm, ClientResponseForm, ClientRegisterForm, GameForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


class MyFormView(FormView):
    form_class = MyModelForm
    template_name = 'home.html'
    success_url = '/lesson_8/products/'

    def form_valid(self, form: MyModelForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)


def product_view(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('product-view')

    return render(request, 'products.html', {'form': form})


def game_view(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('game-view')

    return render(request, 'home.html', {'form': form})


class ClientResponseView(FormView):
    form_class = ClientResponseForm
    template_name = 'home.html'
    success_url = '/lesson_8/'

    def form_valid(self, form: ClientResponseForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class ClientRegisterView(FormView):
    form_class = ClientRegisterForm
    template_name = 'home.html'
    success_url = '/lesson_8/'

    def form_valid(self, form: ClientRegisterForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)



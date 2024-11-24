from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def store_func(request):
    title = 'Товары'
    name = 'Магазин'
    product1 = 'Atomic Heart'
    product2 = 'Cyberpunk 2077'
    product3 = 'PlayDay 2'
    context = {
        'title': title,
        'name': name,
        'product1': product1,
        'product2': product2,
        'product3': product3
    }
    return render(request, 'store_page.html', context)


def basket_func(request):
    title = 'Корзина'
    name = 'Корзина'
    context = {
        'title': title,
        'name': name
    }
    return render(request, 'basket_page.html', context)


def main_func(request):
    title = 'Игровая платформа'
    name = 'Главная'
    store_menu = 'Магазин'
    basket_menu = 'Корзина'
    context = {
        'title': title,
        'name': name,
        'store_menu': store_menu,
        'basket_menu': basket_menu
    }
    return render(request, 'main_page.html', context)

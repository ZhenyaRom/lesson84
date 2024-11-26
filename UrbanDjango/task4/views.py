from django.shortcuts import render


# Create your views here.
def store_func(request):
    title = 'Товары'
    name = 'Магазин'
    plays = ["Atomic Heart", "Cyberpunk 2077", 'PlayDay 2']
    context = {
        'title': title,
        'name': name,
        'plays': plays
    }
    return render(request, 'store_page.html', context)


def basket_func(request):
    title = 'Корзина'
    name = 'Корзина'
    products = []
    context = {
        'title': title,
        'name': name,
        'products': products
    }
    return render(request, 'basket_page.html', context)


def main_func(request):
    title = 'Игровая платформа'
    name = 'Главная'
    context = {
        'title': title,
        'name': name,
    }
    return render(request, 'main_page.html', context)

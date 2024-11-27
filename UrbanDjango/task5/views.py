from django.shortcuts import render
from .forms import UserRegister

users = []


def sign_up_by_django(request):
    info = {'error': ''}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info['form'] = form
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', info)
            try:
                if int(age) < 18:
                    info['error'] = 'Вы должны быть старше 18'
                    return render(request, 'registration_page.html', info)
                else:
                    for user in users:
                        if user['username'] == username:
                            info['error'] = 'Пользователь уже существует'
                            return render(request, 'registration_page.html', info)
                users.append({'username': username, 'password': password, 'age': age})
                print(users)
                info['hi'] = f'Приветствуем, {username}!'
            except ValueError:
                info['error'] = 'Возраст введите арабскими цифрами'
                return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
        info['form'] = form
    return render(request, 'registration_page.html', info)


# Create your views here.
def sign_up_by_html(request):
    info = {'error': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)
        try:
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', info)
            else:
                for user in users:
                    if user['username'] == username:
                        info['error'] = 'Пользователь уже существует'
                        return render(request, 'registration_page.html', info)
            users.append({'username': username, 'password': password, 'age': age})
            print(users)
            info['hi'] = f'Приветствуем, {username}!'
            return render(request, 'registration_page.html', info)
        except ValueError:
            info['error'] = 'Возраст введите арабскими цифрами'
            return render(request, 'registration_page.html', info)
    return render(request, 'registration_page.html')

# python manage.py runserver
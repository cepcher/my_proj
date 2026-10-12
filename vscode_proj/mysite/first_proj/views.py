from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def home_page(request):
    return render(request, 'main.html')

def catalog_page(request):
    return render(request, 'catalog.html')

def cart_page(request):
    return render(request, 'cart.html')

def contacts_page(request):
    # Если пользователь нажал на кнопку и отправил форму (запрос POST)
    if request.method == 'POST':
        # Заполняем форму теми данными, которые прислал пользователь
        form = FeedbackForm(request.POST)
        
        # Проверяем, правильно ли заполнены поля (валидация)
        if form.is_valid():
            # Сохраняем данные в базу данных!
            form.save()
            
            # После успешного сохранения перенаправляем пользователя на эту же страницу,
            # чтобы при обновлении экрана данные не отправились повторно.
            return redirect('contacts')
            
    # Если пользователь просто зашел на страницу (запрос GET)
    else:
        # Создаем пустую чистую форму
        form = FeedbackForm()

    # Передаем форму в HTML-шаблон, чтобы использовать её
    return render(request, 'contacts.html', {'form': form})
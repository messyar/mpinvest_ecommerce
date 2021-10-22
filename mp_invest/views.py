import os.path

from django.shortcuts import render
from mp_invest.requisites import OUR_PHONE
from django.conf import settings

from oscar.apps.catalogue.search_handlers import get_product_search_handler_class

from django import forms
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


class CallbackForm(forms.Form):
    name = forms.CharField(max_length=50, label='name',
                           widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    phone = forms.CharField(max_length=25, label='phone',
                            widget=forms.TextInput(attrs={'placeholder': 'Введите телефон'}))


def index(request):
    context_object_name = 'Products'
    search_handler = get_product_search_handler_class()

    search_handler = search_handler(request.GET, request.get_full_path(), [])
    search_context = search_handler.get_search_context_data(
        context_object_name=context_object_name)

    products = search_context['Products']
    if products:
        products = products[0:10]

    dir_to_partners = 'img/partners'
    path_to_partners = os.path.join(settings.STATICFILES_DIRS[0], dir_to_partners)
    partners_paths = []
    for root, dirs, files in os.walk(path_to_partners):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                partners_paths.append(os.path.join(dir_to_partners, file))

    if request.method == 'POST':
        callback_form = CallbackForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if callback_form.is_valid():
            name = callback_form.cleaned_data['name']
            phone = callback_form.cleaned_data['phone']
            subject = 'Заказ обратного звонка с сайта mp-ivnest.ru'
            message = 'Имя: {}\n' \
                      'Телефон: {}' \
                      .format(name, phone)

            recipients = ['mpinvest.info@yandex.ru']

            try:
                print('Start to send email')
                response_email = send_mail(subject, message, 'mpinvest.info@yandex.ru', recipients, fail_silently=False)
            except BadHeaderError:  # Защита от уязвимости
                print('Invalid header found')
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            print('Email response: ', response_email)
            return render(request, 'html/index.html', {'our_phone': OUR_PHONE, 'products': products,
                                                       'partners_paths': partners_paths, 'callback_form': callback_form})
    else:
        # Заполняем форму
        callback_form = CallbackForm()

    return render(request, 'html/index.html', {'our_phone': OUR_PHONE, 'products': products,
                                               'partners_paths': partners_paths, 'callback_form': callback_form})

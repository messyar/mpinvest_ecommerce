import os.path

import django.conf
from django.shortcuts import render
from mp_invest.requisites import OUR_PHONE
from django.conf import settings

from oscar.apps.catalogue.search_handlers import get_product_search_handler_class


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

    return render(request, 'html/index.html', {'our_phone': OUR_PHONE, 'products': products,
                                               'partners_paths': partners_paths})

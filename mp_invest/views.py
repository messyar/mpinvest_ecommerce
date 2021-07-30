
from django.shortcuts import render
from mp_invest.requisites import OUR_PHONE

from oscar.apps.catalogue.search_handlers import get_product_search_handler_class


def index(request):
    context_object_name = 'Products'
    search_handler = get_product_search_handler_class()

    search_handler = search_handler(request.GET, request.get_full_path(), [])
    search_context = search_handler.get_search_context_data(
        context_object_name=context_object_name)

    products = search_context['Products']
    if products:
        products = products[0:4]

    return render(request, 'html/index.html', {'our_phone': OUR_PHONE, 'products': products})

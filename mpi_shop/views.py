
from django.shortcuts import render
from mpi_shop.requisites import OUR_PHONE


def index(request):
    return render(request, 'html/index.html', {'our_phone': OUR_PHONE})

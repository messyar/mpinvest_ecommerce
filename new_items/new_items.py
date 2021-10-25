import pandas as pd
from django.conf import settings
from os import environ
from django.core.wsgi import get_wsgi_application
import django

django.setup()

from oscar.apps.catalogue.models import Product, Category, ProductCategory, ProductClass
from oscar.core.loading import get_model


def read_sheet(sheet_name):
    category = get_model('catalogue', 'Category')
    product_class = get_model('catalogue', 'ProductClass')

    try:
        new_top_level_category = category.objects.get(name=sheet_name)
    except Exception as exc:
        print(exc)
        new_top_level_category = category.add_root(name=sheet_name, depth=1)

    try:
        product_class = product_class.objects.get(name=sheet_name)
    except Exception as exc:
        print(exc)
        product_class = ProductClass()
        product_class.name = sheet_name
        product_class.save()

    new_items_df = pd.read_excel('new_items.xlsx', sheet_name=sheet_name)

    was_group_name = ''
    second_level_category = ''
    for item in new_items_df.iterrows():
        curr_item = item[1]
        curr_group = curr_item['group']
        if was_group_name != curr_group:
            category_2_level = get_model('catalogue', 'Category')
            try:
                second_level_category = category_2_level.objects.get(name=curr_group)
            except Exception as exc:
                second_level_category = new_top_level_category.add_child(name=curr_group)

        product_model = get_model('catalogue', 'Product')
        try:
            product_model.objects.get(title=curr_item['name'])
        except Exception as exc:
            new_product = product_model()
            print(exc)
            new_product.title = curr_item['name']
            new_product.product_class_id = product_class.id
            new_product.save()
            product_category = ProductCategory()
            product_category.category_id = second_level_category.id
            product_category.product_id = new_product.id
            product_category.save()


read_sheet('АРМАТУРА')
# read_sheet('ТРУБЫ')
# read_sheet('ЛИСТОВОЙ ПРОКАТ')
# read_sheet('СОРТОВОЙ ПРОКАТ')
# read_sheet('ПРОВОЛОКА И СЕТКА')
# read_sheet('КВАДРАТЫ')
# read_sheet('КРУГИ')
# read_sheet('ШЕСТИГРАННИКИ')
# read_sheet('ПРОФНАСТИЛ, МЧ')

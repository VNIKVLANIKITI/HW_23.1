import os
import json
from django.core.management import BaseCommand
from catalog.models import Category, Product
from config.settings import FIXTURES_ROOT

filename_category = "categories.json"
filename_product = "catalog.json"
file_path = os.path.join(FIXTURES_ROOT, 'catalog')

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        file_category = os.path.join(file_path, filename_category)
        with open(file_category, "r", encoding="utf-8") as file:
            data = json.load(file)
            categories = []
            for item in data:
                categories.append(item)
            return categories

    @staticmethod
    def json_read_products():
        file_product = os.path.join(file_path, filename_product)
        with open(file_product, "r", encoding="utf-8") as file:
            data = json.load(file)
            products = []
            for item in data:
                products.append(item)
            return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения
        # информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                    Category(pk=category["pk"], name=category["fields"]["title"],
                             description=category["fields"]["description"], ))
            # Создаем объекты в базе с помощью метода bulk_create()
            Category.objects.bulk_create(category_for_create)

            # Обходим все значения продуктов из фиктсуры для получения
            # информации об одном объекте
            for product in Command.json_read_products():
                product_for_create.append(
                    Product(
                        title=product["fields"]["title"],
                        description=product["fields"]["description"],
                        image=product["fields"]["image"],
                        category=Category.objects.get(pk=product['fields']
                                                      ['category']),
                        price=product["fields"]["price"],
                        create_at=product["fields"]["create_at"],
                        update_at=product["fields"]["update_at"],
                    )
                )

            # Создаем объекты в базе с помощью метода bulk_create()
            Product.objects.bulk_create(product_for_create)

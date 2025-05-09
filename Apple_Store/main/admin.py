from django.contrib import admin
from .models import *
# Регистрируем наши модели в админке

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display позволяет нам указать поля, которые будут отображаться в таблице
    list_display = ('name', 'category', 'price')
    # list_filter позволяет нам фильтровать данные по конкретному полю, в нашем случае это по категориям
    list_filter = ('category',)
    # list_filter позволяет нам искать данные по конкретному полю, в нашем случае это по названию товара
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'display_status')
    search_fields = ('product__name',)
    # функция, которая будет вызываться перед тем, как отобразить данные в таблице
    # используется метод get_status(), который прописан в models.py для красивого отображения
    def display_status(self, obj):
        return obj.get_status()
    # Даем название колонки
    display_status.short_description = 'Статус наличия'
from django.shortcuts import render, get_object_or_404
from .models import * # Импорт всех моделей из текущего приложения (main)

# Представление для отображения страницы с остатками товаров на складе
def StorePage(request):
    # Получение всех остатков товаров на складе, у которых quantity больше 0
    # По умолчанию Джанго не загружает связанные объекты вместе с основным запросом, 
    # поэтому мы делаем это самостоятельно с помощью select_related()
    # Нам нужны категории и количество, поэтому мы загружаем связанные модели category и store
    products = Product.objects.filter(store__quantity__gt=0).select_related('category', 'store')
    # Рендерим шаблон Warehouse.html с переданным контекстом (списком товаров)
    return render(request, 'Warehouse.html', {'products': products})

# Представление для отображения страницы с подробным описанием товара
def ProductDetail(request, pk):
    # Получаем товар по его id (pk) или по умолчанию возвращает ошибку 404, если товар не найден
    product = get_object_or_404(Product.objects.filter(store__quantity__gt=0), pk=pk)
    # Получаем информацию о quantity через product.store
    quantity = product.store
    # Рендерим шаблон Details.html с переданным контекстом (информация о товаре и его количестве)
    return render(request, 'Details.html', {
        'product': product,
        'quantity': quantity,
    })
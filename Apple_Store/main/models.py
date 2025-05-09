from django.db import models
# Создание наших моделей или же таблиц БД

# Создание модели Category (Категория товара)
class Category(models.Model):
    # поле name - название категории с максимальной длиной 100 символов
    name = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        # Настройки для отображения в админ панели
        # verbose_name - Единственное число
        # verbose_name_plural - Множественное число
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

# Создание модели Product (Товар)
class Product(models.Model):
    # поле name - название товара с максимальной длиной 150 символов
    name = models.CharField(max_length=150, verbose_name="Название")
    # поле price - цена, всего 10 цифр и 2 из них после запятой 
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    # поле category - категория товара. ForeignKey - это многие-к-одному, связь с таблицей Category.
    # on_delete=models.CASCADE - при удалении категории удаляться все товары связанные с этой категорией
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    # поле image - изображение товара. Сохраняется автоматические в папку media, 
    # но у нас также указан путь products/, поэтому внутри media, 
    # есть также папка products, в которой храняться все изображения
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    
# Создание модели Store (Склад)
class Store(models.Model):
    # поле product - связь один-к-одному с таблицей Product. 
    # related_name='store' - позволяет нам обращаться из Product к Store простым способом product.store
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Товар",related_name='store')
    # поле quantity - название количество товара на складе, по умолчанию 0
    quantity = models.IntegerField(default=0, verbose_name="Количество на складе")
    
    class Meta:
        verbose_name = "Складской остаток"
        verbose_name_plural = "Складские остатки"

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."
    
    # Данный метод позволяет нам красиво отображать остатки на складе. 
    # Можно использовать как в админке, так и в шаблоне. 
    # В нашем случае мы используем в админке, добавляя новый столбец 'Статус наличия'
    def get_status(self):
        # Если количество товаров 0 - "Нет в наличии"
        if self.quantity == 0:
            return "Нет в наличии"
        # Если количество товаров меньше 10 - "Осталось х шт."
        elif self.quantity < 10:
            return f"Осталось {self.quantity} шт."
        # Если количество товаров 10 и больше - "В наличии (х шт.)"
        return f"В наличии ({self.quantity} шт.)"
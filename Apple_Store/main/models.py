from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    
class Store(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Товар",related_name='store')
    quantity = models.IntegerField(default=0, verbose_name="Количество на складе")
    
    class Meta:
        verbose_name = "Складской остаток"
        verbose_name_plural = "Складские остатки"

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."
    
    def get_status(self):
        if self.quantity == 0:
            return "Нет в наличии"
        elif self.quantity < 10:
            return f"Осталось {self.quantity} шт."
        return f"В наличии ({self.quantity} шт.)"
    get_status.short_description = "Статус"
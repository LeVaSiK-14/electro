from django.db import models


from apps.products.configs import TYPE_DRIVE, FRONT

class Category(models.Model):
    image = models.ImageField(upload_to='categories/images/', verbose_name='Основная картинка')
    name = models.CharField(
        max_length=127, verbose_name='Название'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Активна ли категория?'
    )
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryAuto(models.Model):
    image = models.ImageField(upload_to='categories_auto/images/', verbose_name='Основная картинка')
    name = models.CharField(
        max_length=127, verbose_name='Название'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Активна ли категория?'
    )
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория авто'
        verbose_name_plural = 'Категории авто'


class ProductAuto(models.Model):
    category = models.ForeignKey(CategoryAuto, on_delete=models.CASCADE, related_name='products_auto', verbose_name='Категория')
    name = models.CharField(max_length=127, verbose_name='Название')
    image = models.ImageField(upload_to='product_auto/main/images/', verbose_name='Основная картинка')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    power_reserve = models.CharField(max_length=127, verbose_name='Запас хода')
    battery_capacity = models.CharField(max_length=127, verbose_name='Ёмкость батареи')
    price = models.CharField(max_length=127, verbose_name='Цена')
    torque = models.CharField(max_length=127, verbose_name='Крутящий момент')
    max_speed = models.CharField(max_length=127, verbose_name='Максимальная скорость')
    type_body = models.CharField(max_length=127, verbose_name='Тип кузова')
    type_drive = models.CharField(max_length=127, choices=TYPE_DRIVE, default=FRONT, verbose_name='Тип привода')
    mileage = models.CharField(max_length=127, verbose_name='Пробег')
    year_issue = models.PositiveIntegerField(default=2020, verbose_name='Год выпуска')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт (Транспорт)'
        verbose_name_plural = 'Продукты (Транспорт)'


class ProductAutoImage(models.Model):
    product = models.ForeignKey(ProductAuto, on_delete=models.CASCADE, related_name='images')
    image=models.ImageField(upload_to='product_auto/more/images/', verbose_name='Доп. картинка')

    def __str__(self):
        return self.product.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=127, verbose_name='Название')
    image = models.ImageField(upload_to='product/main/images/', verbose_name='Основная картинка')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    price = models.CharField(max_length=127, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image=models.ImageField(upload_to='product/more/images/', verbose_name='Доп. картинка')

    def __str__(self):
        return self.product.name

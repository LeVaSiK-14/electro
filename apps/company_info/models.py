from django.db import models


class CompanyInfo(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    logo = models.ImageField(upload_to='company_info/logo/image/', verbose_name='Логотип')
    about_image = models.ImageField(upload_to='company_info/about/image/', verbose_name='Картинка в блок "о нас"')
    about_image2 = models.ImageField(upload_to='company_info/about/image/', verbose_name='Картинка в блок "о нас"')
    about_image3 = models.ImageField(upload_to='company_info/about/image/', verbose_name='Картинка в блок "о нас"')
    text = models.TextField(verbose_name='О нас (Описание)')
    phone_number = models.CharField(max_length=127, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Почта')
    telegram = models.URLField(verbose_name='Ссылка на telegram')
    whatsapp = models.URLField(verbose_name='Ссылка на whats app')
    instagram = models.URLField(verbose_name='Ссылка на instagram')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компания'


class Slider(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='company_info/slider/images/', verbose_name='Картинки для слайдера')

    def __str__(self):
        return self.company.name

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Tagam(models.Model):
    title = models.CharField('Тағам аты:', max_length=100)
    photo = models.ImageField('Фото:', upload_to="move/")
    definition = models.TextField('Анықтама:', )
    money = models.PositiveIntegerField('Ақшасы:', default=0)

    def __str__(self):
        return self.title


class Un(models.Model):
    title = models.CharField('Тағам аты:', max_length=100)
    photo = models.ImageField('Фото:', upload_to="un/")
    definition = models.TextField('Анықтама:', )
    money = models.PositiveIntegerField('Ақшасы:', default=0)

    def __str__(self):
        return self.title


class Negizgi(models.Model):
    title = models.CharField('Тағам аты:', max_length=100)
    photo = models.ImageField('Фото:', upload_to="negizgi/")
    definition = models.TextField('Анықтама:', )
    money = models.PositiveIntegerField('Ақшасы:', default=0)

    def __str__(self):
        return self.title


class Susyn(models.Model):
    title = models.CharField('Тағам аты:', max_length=100)
    photo = models.ImageField('Фото:', upload_to="Susyn/")
    definition = models.TextField('Анықтама:', )
    money = models.PositiveIntegerField('Ақшасы:', default=0)

    def __str__(self):
        return self.title


class Tatty(models.Model):
    title = models.CharField('Тағам аты:', max_length=100)
    photo = models.ImageField('Фото:', upload_to="Tatty/")
    definition = models.TextField('Анықтама:', )
    money = models.PositiveIntegerField('Ақшасы:', default=0)

    def __str__(self):
        return self.title


class Salat(models.Model):
    title = models.CharField('Тағам аты:', max_length=100)
    photo = models.ImageField('Фото:', upload_to="Salat/")
    definition = models.TextField('Анықтама:', )
    money = models.PositiveIntegerField('Ақшасы:', default=0)

    def __str__(self):
        return self.title


class Commentary(models.Model):
    name = models.CharField('Aты:', max_length=150)
    email = models.EmailField('Поштасы:', )
    text = models.TextField('Пікір:',)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tapsyrys(models.Model):
    name = models.CharField('Aты:', max_length=150)
    number = models.CharField('Нөмері:', max_length=50)
    adres = models.CharField('Адрес:', max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
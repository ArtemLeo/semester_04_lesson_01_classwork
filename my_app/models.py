# Створення моделей
from django.db import models


# Модель Person для зберігання інформації про людину.
class Person(models.Model):
    first_name = models.CharField(max_length=30)  # Ім'я (до 30 символів)
    last_name = models.CharField(max_length=30)  # Прізвище (до 30 символів)


# Модель Musician для зберігання інформації про музикантів.
class Musician(models.Model):
    first_name = models.CharField(
        max_length=50)  # Ім'я музиканта (до 50 символів)
    last_name = models.CharField(
        max_length=50)  # Прізвище музиканта (до 50 символів)
    instrument = models.CharField(
        max_length=100)  # Інструмент, яким володіє музикант (до 100 символів)


# Модель Album для зберігання інформації про музичні альбоми.
class Album(models.Model):
    artist = models.ForeignKey(Musician,
                               on_delete=models.CASCADE)  # Посилання на музиканта (використовується ForeignKey)
    name = models.CharField(max_length=100)  # Назва альбому (до 100 символів)
    release_date = models.DateField()  # Дата випуску альбому
    num_stars = models.IntegerField()  # Рейтинг альбому у вигляді кількості зірок

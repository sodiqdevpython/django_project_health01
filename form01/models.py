from django.db import models

# Create your models here.
class User(models.Model):
    fio = models.CharField(max_length=100,verbose_name="Ф.И.О")
    data_rojdeniya = models.CharField(max_length=10, verbose_name='Возраст')
    pol = models.CharField(max_length=20, verbose_name='Пол')
    resultn = models.CharField(max_length=100,verbose_name='Результат')
    def __str__(self):
        return self.fio
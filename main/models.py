from django.db import models


class Device(models.Model):
    name = models.CharField('Название', max_length=20)
    group = models.CharField('Группа', max_length=20)
    protocol = models.CharField("Протокол", max_length=10)
    type = models.CharField("Тип", max_length=10, default="Датчик")

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return self.name
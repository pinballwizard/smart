from django.db import models


class Device(models.Model):
    device_type_choices = (
        ('sensor', 'Датчик'),
        ('switcher', 'Реле'),
    )
    name = models.CharField('Название', max_length=20, default="")
    group = models.CharField('Группа', max_length=20, blank=True)
    device_type = models.CharField("Тип", max_length=10, choices=device_type_choices, default="sensor")
    location = models.CharField("Местоположение", max_length=20, blank=True)


class ModbusDevice(Device):
    role_choices = (
        ('main', 'main'),
        ('subordinate', 'subordinate'),
    )
    data_type_choices = (
        ('coils', 'Coils'),
        ('discrete_inputs', 'Discrete Inputs'),
        ('input_registers', 'Input Registers'),
        ('holding_registers', 'Holding Registers'),
    )
    modbus_type_choices = (
        ('tcp', 'TCP'),
        ('ascii', 'ASCII'),
        ('rtu', 'RTU'),
    )
    modbus_type = models.CharField("Вид протокола", max_length=10, choices=modbus_type_choices, default='tcp')
    role = models.CharField("Роль устройства", max_length=10, choices=role_choices, default='subordinate')
    data_type = models.CharField("Тип данных", max_length=20, choices=data_type_choices, default='coils')
    
    class Meta:
        verbose_name = "Устройство modbus"
        verbose_name_plural = "Устройства modbus"

    def __str__(self):
        return self.name


class MQTTDevice(Device):
    mqtt_type_choices = (
        ('mqtt', 'MQTT'),
        ('mqtt-sn', 'MQTT-SN'),
    )
    role_choices = (
        ('publisher', 'Publisher'),
        ('consumer', 'Consumer'),
    )
    mqtt_type = models.CharField("Видпротокола",max_length=10, choices=mqtt_type_choices, default='mqtt')
    role = models.CharField("Роль устройства", max_length=10, choices=role_choices, default='subordinate')

    class Meta:
        verbose_name = "Устройство MQTT"
        verbose_name_plural = "Устройства MQTT"

    def __str__(self):
        return self.name
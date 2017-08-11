from django.shortcuts import render
from main.models import ModbusDevice, MQTTDevice


def device_list(request):
    devices = ModbusDevice.objects.all()
    data = {
        'devices': devices,
    }
    return render(request, 'main/device_list.html', data)
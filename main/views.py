from django.shortcuts import render
from main.models import Device


def device_list(request):
    devices = Device.objects.all()
    data = {
        'devices': devices,
    }
    return render(request, 'main/device_list.html', data)
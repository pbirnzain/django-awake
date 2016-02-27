from django.shortcuts import render
from django.http import HttpResponse
import awake

# Create your views here.
def fractal_awake(request):
    try:
        mac = 'ff-ff-ff-ff-ff-ff'
        awake.wol.send_magic_packet(mac, broadcast='255.255.255.255')

        return HttpResponse('Done')
    except Exception as e:
        return HttpResponse('Fail')

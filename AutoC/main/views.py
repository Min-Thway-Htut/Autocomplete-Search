from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from .models import *
from faker import Faker
from django.template import loader
fake = Faker()

def generate_data(request):
    for i in range(0, 100):
        FakeAddress.objects.create(address=fake.address())
    return JsonResponse({'status':200})

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def search_address(request):
    address = request.GET.get('address')
    payload = []
    if address:
        fake_address_objs = FakeAddress.objects.filter(address__icontains=address)
    
        for fake_address_obj in fake_address_objs:
            payload.append(fake_address_obj.address)

    return JsonResponse({'status':200, 'data': payload})
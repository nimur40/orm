from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Customer

def home(request):
    customers=Customer.objects.all()
    result=customers.values()
    return JsonResponse({'data':list(result)})

# Create your views here.

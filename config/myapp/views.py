from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Customer
from django.core.serializers import serialize
import json
from django.forms.models import model_to_dict
'''
def home(request):
    customers=Customer.objects.all()
    result=customers.values()
    return JsonResponse({'data':list(result)})
def home(request):
    customers=Customer.objects.all().values()
    return JsonResponse({'data':list(customers)})
def home(request):
    customers=Customer.objects.all().values('id','name')
    return JsonResponse({'data':list(customers)})
#serialize
def home(request):
    customers=Customer.objects.all()
    result=serialize('json',customers)
    return JsonResponse({'data':result})
import json
def home(request):
    customers=Customer.objects.all()
    result=serialize('json',customers,fields=('id','mobile'))
    #return JsonResponse({'data':result})
    return JsonResponse({'data':json.loads(result)})
'''
'''
#Fetch a single value
def home(request):
    customers=Customer.objects.get(id=1)
    return JsonResponse({'id':customers.id,'name':customers.name})
def home(request):
    customers=Customer.objects.get(id=1)
    coustomer_data=({'id':customers.id,'name':customers.name})
    return  JsonResponse(coustomer_data)
def home(request):
    customers=Customer.objects.get(id=1)
    #coustomer_data=({'id':customers.id,'name':customers.name})
    return  JsonResponse(model_to_dict(customers))
'''
'''
#First Row
def home(request):
    customers=Customer.objects.first()
    return JsonResponse({'id':customers.id,'name':customers.name})
    
#last row
def home(request):
    customers=Customer.objects.last()
    return JsonResponse({'id':customers.id,'name':customers.name})
'''
'''
#Filtering Records
def home(request):
    #name__icontains=case-insensitive searches
    #name__contains=case-sensitive searches
    customers=Customer.objects.filter(name__contains='Abdullah').values()
    return JsonResponse({"date":list(customers)})
def home(request):
    #name__icontains=case-insensitive searches
    #name__contains=case-sensitive searches
    customers=Customer.objects.filter(name__icontains='Abdullah').values()
    return JsonResponse({"date":list(customers)})
#Exclude all data
def home(request):
    #name__icontains=case-insensitive searches
    #name__contains=case-sensitive searches
    customers=Customer.objects.exclude(name__icontains='Abdullah').values()
    return JsonResponse({"date":list(customers)})
'''
'''
#Sorting Records
def home(request):
    #ASC Name
    customers=Customer.objects.all().order_by('name').values()
    return JsonResponse({"date":list(customers)})
def home(request):
    #DESc Name
    customers=Customer.objects.all().order_by('-name').values()
    return JsonResponse({"date":list(customers)})
'''
'''
#Limit
def home(request):
    customers=Customer.objects.all()[0:2].values()
    return JsonResponse({"date":list(customers)})
'''
'''
#Range
def home(request):
    customers=Customer.objects.all()[5:10].values()
    return JsonResponse({"date":list(customers)})

'''

''''
#count records
def home(request):
    customers=Customer.objects.count()
    return JsonResponse({'total_customers:' :customers})
'''
'''
#Distinct records
def home(request):
    customers=Customer.objects.values('name').distinct()
    return JsonResponse({'total_customers:' :list(customers)})
'''

#Distinct records
"""def home(request):
    customers=Customer.objects.values('name').distinct()
    return JsonResponse({'total_customers:' :list(customers)})"""
#values query
'''def home(request):
    customers=Customer.objects.values('name','email')
    return JsonResponse({'customer': list(customers)})'''
#values list query
'''def home(request):
    customers=Customer.objects.values_list('name',flat=True)
    return JsonResponse({'customer': list(customers)})'''

#chaining query
'''def home(request):
    customers=Customer.objects.filter(name__icontains='nimur').order_by('id')
    return JsonResponse({'customer': list(customers)})'''
#Raw Sql Query
def home(request):
    query="select * from myapp_customer where name =%s"
    customerts=Customer.objects.raw(query,['Rahim Uddin'])
    result=[{'id':customer.id,'name':customer.name} for customer in customerts]
    return JsonResponse({'customers':result})



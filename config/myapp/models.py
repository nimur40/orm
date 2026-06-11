from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class OTP(models.Model):
    code=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='otps')
class Category(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='categorys')
    
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    unit=models.CharField(max_length=255)
    img_url=models.URLField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")
    #user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="product")
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="product",
    null=True,
    blank=True
)
class Customer(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(null=True,blank=True)
    mobile=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='customers')
class Invoice(models.Model):
    total=models.DecimalField(max_digits=10,decimal_places=2)
    discount=models.DecimalField(max_digits=10,decimal_places=2)
    vat=models.DecimalField(max_digits=10,decimal_places=2)
    payable=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='invoices')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='invoices')
   
class InvoiceProduct(models.Model):
    qty=models.IntegerField()
    sale_price=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='invoiceProduct')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='invoiceProduct')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='invoiceProduct')
    
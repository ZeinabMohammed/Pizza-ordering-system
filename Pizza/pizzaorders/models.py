from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save, post_save, m2m_changed
from decimal import Decimal

SIZES=(
		('MEDIUM','M'),
	    ('LARGE','L'),
	  )
TYPES=(
	('MEET','M'),
	('CHICKEN','CH'),
	('MIXCHEESE','MIX'),
	)
ORDER_STATUS =(
		('DELIVERED','DELIVERED'),
		('ORDERED','ORDERED'),
	)
class Customer(models.Model):
	name    = models.CharField(max_length=20,blank=True,null=True)
	phone   = PhoneNumberField()
	address = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return self.name



class Pizza_Types(models.Model):
	name     = models.CharField(choices=TYPES,max_length=10,blank=True,null=True)
	size     = models.CharField(choices=SIZES,max_length=10,null=True)
	price    = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	
	def __str__(self):
		return str(self.name)
class Pizza_Sizes(models.Model):
	Pizza_type = models.ForeignKey(Pizza_Types, on_delete=models.CASCADE)
	size_name  = models.CharField(choices=SIZES, max_length=10,blank=True,null=True)
	price      = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	
	def __str__(self):
		return str(self.size)

class Order(models.Model):
	customer    = models.ForeignKey(Customer,on_delete=models.CASCADE)
	pizzas      = models.ManyToManyField(Pizza_Types)
	# pizzas_size = models.ManyToManyField(Pizza_Sizes)
	quantity    = models.IntegerField(default=1)
	total_price = models.DecimalField(decimal_places=2, max_digits=20, default=00.00)
	status      = models.CharField(choices=ORDER_STATUS,max_length=10,blank=True,null=True)

	def __str__(self):
		return str(self.id)

def m2m_changed_order_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        pizzas_ordered = instance.pizzas.all()
        total_price = 0
        for x in pizzas_ordered:
            total_price += x.price
            # total_price.save()
        # if instance.subtotal != total:
        #     instance.subtotal = total
        # instance.save()

m2m_changed.connect(m2m_changed_order_receiver, sender=Order.pizzas.through)

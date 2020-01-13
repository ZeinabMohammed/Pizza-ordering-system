from rest_framework import serializers
from .models import Order, Pizza_Types

#Serializing pizza data
class Ordered_Pizzas(serializers.ModelSerializer):
	class Meta:
		model = Pizza_Types
		fields= '__all__'


#Serializing order data
class OrderSerializer(serializers.ModelSerializer):
	items=Ordered_Pizzas(many=True)
	class Meta:
		model  = Order
		fields = ['items','customer','quantity','total_price','status']



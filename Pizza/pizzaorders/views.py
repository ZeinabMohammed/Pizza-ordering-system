from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import APIException
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters import rest_framework as filters
#Creating order view
class CreateOrder(CreateAPIView):
	serializer_class   = OrderSerializer
	
	def post(self,request, format=None):
		serializer = OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderView(APIView):
	""" order CRUD operations"""

	def get_order(self,pk):
		try:
			return Order.objects.get(pk=pk)
		except Order.DoesNotExist:
			raise Http404
	#Retrieve order by its PK
	def get(self, request,pk, format=None):
		order = self.get_order(pk)
		serializer = OrderSerializer(order,context={'request': request})
		return Response(serializer.data)
	def put(self, request,pk, format=None):
		order = self.get_order(pk)
		serializer = OrderSerializer(order, data=request.data)
		if serializer.is_valid():
			status=serializer.data['status']
			#confirming that order not in deivery before updating
			if status == 'DELIVERED':
				raise APIException("Couldn't apply changes order already Delivered")
			serializer.save()
			return Response(serializer.data)
	def delete(self, request, pk, format=None):
		order = self.get_order(pk)
		order.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


#ORDERs LIST & Create using Viewsets
class OrderList(viewsets.ModelViewSet):
	queryset		   = Order.objects.all()
	serializer_class   = OrderSerializer
	filterset_fields   = ['customer','status',]#Filtering by customer &/ status
	search_fields 	   = '__all__'
	#Override update function
	def update(self,  request, pk=None):
		response = super(OrderList,self).update(request, pk=None)
		order=Order.objects.get(id=pk)
		serializer = OrderSerializer(order, data=request.data)
		if serializer.is_valid():
			status=serializer.data['status']
			# check status to prevent delivered orders updating
			if status == 'DELIVERED':
				raise APIException("Couldn't apply changes order already Delivered")
			serializer.save()
			return Response(serializer.data)
	
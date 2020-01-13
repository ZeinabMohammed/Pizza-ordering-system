from .views import (CreateOrder,OrderView,OrderList)
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.urls import path,include

app_name='pizzaorders'
router = routers.DefaultRouter()
router.register('orders-list', OrderList)

urlpatterns = [
	path('', include(router.urls)),
	path('order/<int:pk>',OrderView.as_view(), name='order'),
	path('createorder/',CreateOrder.as_view(),name='creatingorder'),

	]

# urlpatterns = format_suffix_patterns(urlpatterns)
from django.contrib import admin
from .models import (Customer,
					Pizza_Types,
					Order,
					)


admin.site.register(Customer)
admin.site.register(Pizza_Types)
admin.site.register(Order)
# admin.site.register(Pizza_Sizes)

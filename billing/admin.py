from django.contrib import admin
from .models import Category, Item, Bill, BillItem

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Bill)
admin.site.register(BillItem)
from django.contrib import admin

from .models import bill_Data

# class bill(admin.ModelAdmin):
#     list_display = ['user_id','room_number', 'rent', 'electricity', 'water', 'food', 'parking']
#     ordering = ['id']

admin.site.register(bill_Data)

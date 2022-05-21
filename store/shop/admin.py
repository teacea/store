
from django.contrib import admin
from .models import Item, Group

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'photo',
        'price',
        'group',
        'created'
    )
    list_editable = ('group',)
    search_fields = ('name',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(Group)
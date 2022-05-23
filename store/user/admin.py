from django.contrib import admin
from .models import Cart, User


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'holder',
        'itemcart'
    )
    list_editable = ('holder','itemcart')
    search_fields = ('holder',)
    list_filter = ('holder',)
    empty_value_display = '-пусто-'


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'middle_name',
        'second_name',
        
    )
    list_editable = ('first_name','middle_name','second_name',)
    search_fields = ('second_name',)
    list_filter = ('second_name',)
    empty_value_display = '-пусто-'

admin.site.register(Cart, CartAdmin)
admin.site.register(User, UserAdmin)

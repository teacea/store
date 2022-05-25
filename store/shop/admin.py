
from django.contrib import admin
from .models import Item, Group, Collection

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'photo',
        'price',
        'group',
        'created',
        'collection',
    )
    list_editable = ('group','collection','name','price','photo')
    search_fields = ('name',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
        'image',
    )
    list_editable = ('image','title','slug','description',)
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'

class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    list_editable = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'

admin.site.register(Item, ItemAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Collection, CollectionAdmin)
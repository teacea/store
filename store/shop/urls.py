from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'shop'


urlpatterns = [
    path('', views.index, name="index"),
    path('group/<slug:slug>/', views.group, name='group'),
    path('group/<slug:slug>/item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('collection/<slug:slug>/', views.col, name='collection'),

    ]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
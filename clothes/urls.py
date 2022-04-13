from . import views
from django.urls import include, path
app_name='clothes'
urlpatterns = [
    path('',views.view_clothes,name='view_clothes'),
    path('create_clothes_form/',views.create_clothes_form,name='create_clothes_form'),
    path('save_clothes/',views.save_clothes,name='save_clothes'),
    path('update_clothes_form/(?P<ID>/D+)',views.update_clothes_form,name='update_clothes_form'),
    path('update_clothes/',views.update_clothes,name='update_clothes'),
    path('delete/(?P<ID>\D+)',views.delete_clothes,name='delete_clothes'),
]

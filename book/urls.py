from . import views
from django.urls import include, path
app_name='book'
urlpatterns = [
    path('',views.view_book,name='view'),
    path('create_book_form/',views.create_book_form,name='create_form'),
    path('save_book/',views.save_book,name='save_book'),
    path('update_book_form/(?P<ISBN>\D+)',views.update_book_form,name='update_book_form'),
    path('update_book/',views.update_book,name='update_book'),
    path('delete/(?P<ISBN>\D+)',views.delete_book,name='delete_book'),



    path('view_bookItem/',views.view_bookItem,name='view_bookItem'),
    path('create_bookItem_form/',views.create_bookItem_form,name='create_bookItem_form'),
    path('save_bookItem/',views.save_bookItem,name='save_bookItem'),
    path('update_bookItem_form/(?P<ID>\D+)',views.update_bookItem_form,name='update_bookItem_form'),
    path('update_bookItem/',views.update_bookItem,name='update_bookItem'),
    path('delete_bookItem/(?P<ID>\D+)',views.delete_bookItem,name='delete_bookItem'),




    path('view_bookStats/',views.view_bookStats,name='view_bookStats'),
    path('create_bookStats_form/',views.create_bookStats_form,name='create_bookStats_form'),
    path('save_bookStats/',views.save_bookStats,name='save_bookStats'),
    path('update_bookStats_form/(?P<ID>\D+)',views.update_bookStats_form,name='update_bookStats_form'),
    path('update_bookStats/',views.update_bookStats,name='update_bookStats'),
    path('delete_bookStats/(?P<ID>\D+)',views.delete_bookStats,name='delete_bookStats'),


]

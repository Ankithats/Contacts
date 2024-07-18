from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('upadte/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('details/<int:id>',views.details,name='details'),
    path('call/<int:id>',views.call,name='call')
    
]
from django.urls import path,include
from . import views 

urlpatterns = [
       path('',views.index,name='index'),
       path('adduser/',views.adduser,name='adduser'),
       path('login/',views.login,name='login'),
       path('logout/',views.logout,name='logout'),
       path('edit/<int:pk>/',views.edit,name='edit'),
       path('delete/<int:pk>/',views.delete,name='delete'),
]
from django.urls import include, path

from . import views 

urlpatterns = [
   path('create.html/', views.create, name='create.html'),
   path('list.html/', views.post_list, name='list.html'),
]
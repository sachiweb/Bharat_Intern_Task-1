from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('post-detail/<int:pk>', views.PostDetail, name='post_detail'),
    path('add', views.add, name='add'),
]

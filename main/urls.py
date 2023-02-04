from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.index1, name="index1"),
    path('2', views.index2, name="index2"),
    path('3', views.index3, name="index3"),
    path('4', views.index4, name="index4"),
    path('5', views.index5, name="index5"),
    path('6', views.index6, name="index6"),
    path('7', views.index7, name="index7"),
    path('8', views.index8, name="index8"),
    path('9', views.index9, name='index9'),
    path('review/', views.Com.as_view(), name='add_review'),
    path('rev/', views.Tap.as_view(), name='add_rev'),
]

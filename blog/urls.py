from django.urls import path
from .views import blog,post

urlpatterns=[
    path('',blog,name='blog'),
    path('post/<str:title>/',post,name='post')
]
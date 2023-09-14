from django.urls import path, include

from ..api import views

urlpatterns = [
    path('api', views.UserCreate.as_view(), name='user-create'),
    path('api/<str:name>', views.UserDetail.as_view(), name='user-detail'),

]
from django.urls import path, include

from ..api import views

urlpatterns = [
    path('user', views.UserCreate.as_view(), name='user-create'),
    path('user/<str:name>', views.UserDetail.as_view(), name='user-detail'),

]
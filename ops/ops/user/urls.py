from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/login_register', views.login_regester, name='login_regester'),
    # path('index/', views.dbtest, name='dbtest'),
]


from django.urls import path
from gaurabapp import views
urlpatterns = [
    path('login/', views.login_view, name='login' ),
    path('',  views.index, name='home')
]

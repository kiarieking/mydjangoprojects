from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login2/', LoginView.as_view(template_name='users/login.html'), name='login2'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('create_user/', views.create_user, name='create_user'),
    path('login_user/', views.login_user, name='login_user'),
]
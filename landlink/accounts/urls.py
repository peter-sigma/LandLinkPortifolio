from django.urls import path
from . import views

urlpatterns = [
            path('register/', views.register, name='register'),
            path('login/', views.login_view, name='login'),
            path('logout/', views.logout_view, name='logout'),
            path('password_reset/', views.password_reset_view, name='password_reset'),
            path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
            path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
            path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
        ]

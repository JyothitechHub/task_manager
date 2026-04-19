from django.urls import path
from . import views

urlpatterns = [
    path('',             views.login_view,    name='login'),
    path('login/',       views.login_view,    name='login'),
    path('register/',    views.register_view, name='register'),
    path('logout/',      views.logout_view,   name='logout'),
    path('dashboard/',   views.dashboard,     name='dashboard'),
    path('add/',         views.add_task,      name='add_task'),
    path('edit/<int:pk>/',   views.edit_task,   name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
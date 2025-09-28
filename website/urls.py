from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_def,name='login'),
    path('logout/',views.logged_out, name='logout'),
    path('register/',views.registered,name='signup'),
]

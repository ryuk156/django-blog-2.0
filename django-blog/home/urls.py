from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
  
    path('signup', views.handlesignup, name='signup'),
    path('login', views.handlelogin, name='login'),
    path('logout', views.handlelogout, name='logout'),
    path('userpage', views.userpage, name='userpage'),
    path('user', views.user, name='user'),
   
]
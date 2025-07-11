"""
URL configuration for dcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    # here logout_user is calling the method from views.py
    path('register/',views.register_user,name='register'),
    path ('record/<int:pk>',views.customer_record,name='record'),
    path ('delete_record/<int:pk>',views.delete_record,name='delete_record'),
    path ('add_record/',views.add_record,name='add_record'),
    
    path ('update_record/<int:pk>',views.update_record,name='update_record'),
    # name='record' is the name of the path?
# here <int:pk> means passing the primary key of the record
    

]

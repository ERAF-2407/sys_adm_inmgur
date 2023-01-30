"""sys_adm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('registers/', views.registers, name='registers'),
    path('registers_completed/', views.registers_completed, name='registers_completed'),
    path('registers/create/', views.create_register, name='create_register'),
    path('registers/<int:register_id>/', views.register_detail, name='register_detail'),
    path('registers/<int:register_id>/complete', views.complete_register, name='complete_register'),
    path('registers/<int:register_id>/delete', views.delete_register, name='delete_register'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]

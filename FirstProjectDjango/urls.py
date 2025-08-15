"""
URL configuration for FirstProjectDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import home,demo,jagan
from demoapp.views import run_migrations
# from demoapp.views import home
# from demoapp.views import fapp
from django.conf.urls.static import static
from django.conf import  settings
from demoapp.views import blogpage,blogVideo,delete_blog




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("jagan",jagan,name="jagan"),
    # path("jagan/",demo,name="demo"),
    # path("siri/",home,name="home"),
    # path("jagan",fapp,name="jagan"),
    path("blog",blogpage,name="blog"),
    path("blogvideo",blogVideo,name="blogvideo"),
    path('delete_blog/<int:pk>/', delete_blog, name='delete_blog'),
    path('run-migrations/', run_migrations),

]

    
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

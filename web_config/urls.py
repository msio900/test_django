"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views
from maps import views as mapsviews
from board import views as boardviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index),
    path('', views.index),
    path('index01', views.index01),
    path('index02', views.index02),
    path('maps/home', mapsviews.home),
    path('board/list', boardviews.list),
    path('board/list_paginator', boardviews.list_paginator),
]

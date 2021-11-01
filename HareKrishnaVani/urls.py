"""HareKrishnaVani URL Configuration

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
from os import name
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from Vani import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('harekrishnavani/admin/superuserlogin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('artits/', views.artists, name='ars'),
    path('artits/prabhu/<slug:product_slug>/', views.artists_single, name='arss'),
    path('podcasts/', views.podcasts, name='podcasts'),
    path('release/<int:prabhu>', views.release, name='release'),
    path('release/<int:prabhu>/<int:name>', views.track, name='track'),
    path('add_playlist/<int:id>/', views.playlist_a, name='add_playlist'),
    path('remove_song_playlist/<int:id>', views.playlist_remove, name='remove_playlist'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contact, name='contact'),
    path('contactus/thanks/', views.c_thanks, name='c_thanks'),
    path('ajax/', views.more_todo, name='ajax')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
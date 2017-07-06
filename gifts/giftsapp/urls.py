from django.conf.urls import include, url
from giftsapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^odiwali/([0-9])$', views.odiwali, name = 'odiwali'),
    url(r'^Anniversary1/([0-9])$', views.anniversary, name = 'anniversary'),
    url(r'^quest/([0-9])$', views.quest, name = 'quest'),
    url(r'^quest1/([0-9])/([0-9])$', views.quest1, name = 'quest'),
    url(r'^quest2/([0-9])/([0-9])$', views.quest2, name = 'quest'),
    url(r'^teen_images/([0-9])/([0-9])/([0-9])$', views.teen_images, name = 'images'),
    url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^logout/$', auth_views.logout, name = 'logout'),
    url(r'^output/$', views.output, name = 'output'),
]



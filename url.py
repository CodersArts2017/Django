# Django-SettingUrl
from django.contrib import admin
from django.urls import path
from helloworld.views import Index
from helloworld.views import Hello

urlpatterns = [
  path('admin/', admin.site.urls),
  path('helloworld/',Index),
  path('helloworld/',Hello)
  ]

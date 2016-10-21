from django.conf.urls import url, include
from django.contrib import admin

from lists import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^lists/', include('lists.urls')),
    url(r'^admin/', admin.site.urls),
]

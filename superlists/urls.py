from django.conf.urls import url, include
from django.contrib import admin
from lists.views import HomePageView

from lists import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^admin/', admin.site.urls),
]

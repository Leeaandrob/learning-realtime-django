# coding: utf-8
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from chat.views import (HomeView)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^chats/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

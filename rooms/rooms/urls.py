# coding: utf-8
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from chat.views import (AboutView, NewRoomView, ChatRoomView, HomeView)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^new/$', NewRoomView.as_view(), name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', ChatRoomView.as_view(), name='chat_room'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

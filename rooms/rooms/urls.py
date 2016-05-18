# coding: utf-8
from django.conf.urls import url
from django.contrib import admin

from chat.views import (AboutView, NewRoomView, ChatRoomView)

urlpatterns = [
    url(r'^$', AboutView.as_view(), name='about'),
    url(r'^new/$', NewRoomView.as_view(), name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', ChatRoomView.as_view(), name='chat_room'),
    url(r'^admin/', admin.site.urls),
]

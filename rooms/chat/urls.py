# coding: utf-8
from django.conf.urls import url
from .views import (ChatRoomView, NewRoomView, AboutView)

urlpatterns = [
    url(r'^new/$', NewRoomView.as_view(), name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', ChatRoomView.as_view(), name='chat_room'),
    url(r'^about/$', AboutView.as_view(), name='about'),
]

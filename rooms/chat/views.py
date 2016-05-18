# coding: utf-8
import hashlib
import random
import logging

from django import http
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View, RedirectView

from .models import Room


logger = logging.getLogger("django")


class HomeView(View):
    template_name = 'chat/base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class AboutView(View):
    template_name = 'chat/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ChatRoomView(View):
    template_name = "chat/room.html"

    def get(self, request, *args, **kwargs):
        label = self.kwargs.get("label")
        room, created = Room.objects.get_or_create(label=label)

        messages = reversed(room.messages.order_by('-timestamp')[:50])

        return render(request, self.template_name, {
            'room': room,
            'messages': messages,
        })


class NewRoomView(RedirectView):
    permanent = True
    pattern_name = 'chat_room'

    def get(self, request, *args, **kwargs):
        room = str(random.randrange(10000)) + hashlib.md5(
            "banana").hexdigest()

        url = Room.objects.filter(label=room)

        if url.exists():
            if self.permanent:
                return http.HttpResponsePermanentRedirect(self.pattern_name, {
                    "label": url})
        elif not url.exists():
            url = Room.objects.create(label=room)
            return http.HttpResponseRedirect(reverse(self.pattern_name,
                                                     kwargs={'label': url}))
        else:
            logger.warning('Gone: %s', self.request.path,
                           extra={
                               'status_code': 410,
                               'request': self.request
                           })
            return http.HttpResponseGone()

        return super(NewRoomView,
                     self).get_redirect_url(*args, **kwargs)

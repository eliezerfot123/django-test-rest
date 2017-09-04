from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView
    )

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
    #esto es para hacer explicito en lo que necesito para mostrar un camp en especifico
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    #url(r'^create/$', post_create),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
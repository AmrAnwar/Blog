from django.conf.urls import url, include
from posts.views import post_detail, post_list, post_create


urlpatterns = [
    url(r'^create/', post_create, name="create"),

    url(r'^$', post_list, name="list"),

    url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),

]
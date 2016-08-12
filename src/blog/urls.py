from django.conf.urls import url

from .views import (
    index,
    lend_list,
    lend_detail,
    lend,
    my_page,
    lend_edit,
    )


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^lend_list/$', lend_list, name="lend_list"),
    url(r'^lend/$', lend, name="lend"),
    url(r'^lend_list/(?P<lend_id>\d+)/$', lend_detail, name="lend_detail"),
    url(r'^lend_list/(?P<lend_id>\d+)/edit/$', lend_edit, name="lend_edit"),
    url(r'^my/(?P<pk>\d+)/$', my_page, name="my_page"),

]

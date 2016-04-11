from django.conf.urls import include, url, patterns
from django.contrib import admin

from api.views import ShipList, ShipDetail
# from api.views import InviteList, InviteDetail
from api.views import JanuszList, JanuszDetail
from api.views import render_invite, save_invite, get_invite_by_key, get_wiki

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/ships/$', ShipList.as_view()),
    url(r'^v1/ships/(?P<pk>[0-9]+)/$', ShipDetail.as_view()),
    # url(r'^v1/invite/$', InviteList.as_view()),
    # url(r'^v1/invite/(?P<key>.+)/$', InviteList.as_view()),
    # url(r'^v1/invite/(?P<pk>[0-9]+)/$', InviteDetail.as_view()),
    url(r'^v1/janusz/$', JanuszList.as_view()),
    url(r'^v1/janusz/(?P<pk>[0-9]+)/$', JanuszDetail.as_view()),
    # url(r'^$', post_list, name='post_list'),
    url(r'^v1/send/invite/$', render_invite, name='render_invite'),
    url(r'^v1/save/invite/$', save_invite, name='save_invite'),
    url(r'^v1/invite/$', get_invite_by_key, name='get_invite_by_key'),

    url(r'^v1/wiki/$', get_wiki, name='get_wiki'),
    
]

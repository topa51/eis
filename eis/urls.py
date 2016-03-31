from django.conf.urls import include, url, patterns
from django.contrib import admin

from api.views import ShipList, ShipDetail
from api.views import InviteList, InviteDetail
from api.views import JanuszList, JanuszDetail

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/ships/$', ShipList.as_view()),
    url(r'^v1/ships/(?P<pk>[0-9]+)/$', ShipDetail.as_view()),
    url(r'^v1/invite/$', InviteList.as_view()),
    url(r'^v1/invite/(?P<pk>[0-9]+)/$', InviteDetail.as_view()),
    url(r'^v1/janusz/$', JanuszList.as_view()),
    url(r'^v1/janusz/(?P<pk>[0-9]+)/$', JanuszDetail.as_view()),
    
]

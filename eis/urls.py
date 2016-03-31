from django.conf.urls import include, url, patterns
from django.contrib import admin

from api.views import ShipList

urlpatterns = [
    # Examples:
    # url(r'^$', 'eis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^v1/ships/$', ShipList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]

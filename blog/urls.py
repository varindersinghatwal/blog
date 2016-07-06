from django.conf.urls import include, url
from django.contrib import admin
from web.views import (home, add_article, view_article,
                       comments)

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_article/', add_article, name='add_article'),
    url(r'^article/(?P<article_id>\d+)/$', view_article),
    url(r'^comments/$', comments),
]

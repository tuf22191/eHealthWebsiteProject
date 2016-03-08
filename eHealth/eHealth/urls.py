from django.conf.urls import patterns, include, url
from django.contrib import admin
#from eHealth import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eHealth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^generalSite/', include('generalSite.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('generalSite.urls')),
)

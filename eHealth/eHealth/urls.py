from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

#from eHealth import views

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/generalSite/'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^generalSite/', include('generalSite.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

)


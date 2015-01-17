from django.conf.urls import patterns, include, url
from django.contrib import admin

from carriage_ninja.views import HomeView, FAQView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^faq$', FAQView.as_view(), name='faq'),
    # url(r'^blog/', include('blog.urls')),

    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
